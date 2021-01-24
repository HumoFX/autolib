from django.core.files.storage import default_storage
from import_export.tmp_storages import TempFolderStorage
from pymarc import MARCReader
import csv, os
import re

# from elib.settings import MEDIA_ROOT
from elib import settings
from django.conf import settings

from elib.settings import MEDIA_ROOT


def converter(filename, university_id):
    # for filename in os.listdir('data/mrc/'):
    #     if os.path.isdir('data/mrc/' + filename) or filename[0] == '.':
    #         continue
    print(12212)
    reader = MARCReader(open(MEDIA_ROOT + '/file/marc/' + filename, 'rb'), to_unicode='utf-8',
                        force_utf8=True)
    with open(MEDIA_ROOT + '/file/marc/csv/' + os.path.splitext(filename)[0] + '.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'author', 'isbn',
                         'publisher', 'pubplace', 'publication_date',
                         'extent', 'dimensions', 'subject', 'inclusiondate',
                         'source', 'note', 'university', 'is_partial_publication_date'])
        print(2)
        # print(writer.dialect)
        for record in reader:
            address = clean(record['260']['a']) if '260' in record else None
            extent = clean(re.findall(r'\d+', record['300']['a'])[0], True) if '300' in record else None
            dimensions = record['300']['c'] if '300' in record else None
            subject = record['650']['a'] if '650' in record else None
            inclusiondate = record['988']['a'] if '988' in record else None
            source = record['906']['a'] if '906' in record else None
            university = university_id
            is_partial_publication_date = True
            # library = record['690']['5'] if '690' in record else None
            note = " ".join([field['a'] for field in record.notes() if 'a' in field])
            # author = clean(record[])
            # print(record)
            writer.writerow([get_title(record), clean(record.author(), True), record.isbn(),
                             clean(record.publisher()), address, clean(record.pubyear()),
                             extent, dimensions, subject, inclusiondate,
                             source, note, university, is_partial_publication_date])
    # default_storage.delete('/file/marc/' + filename)
    # print(MEDIA_ROOT + '/file/marc/csv/' + os.path.splitext(filename)[0] + '.csv')
    return MEDIA_ROOT + '/file/marc/csv/' + os.path.splitext(filename)[0] + '.csv'


def get_title(record):
    # pymarc has a title() method that is similar to this, but it doesn't
    # concatenate subtitle and title properly
    if '245' in record and 'a' in record['245']:
        title = clean(record['245']['a'])
        if 'b' in record['245']:
            title += ' ' + clean(record['245']['b'])
        return title
    else:
        return None


def clean(element, isAuthor=False):
    if element is None or not element.strip():
        return None
    else:
        element = element.strip()

        for character in [',', ';', ':', '/']:
            if element[-1] == character:
                return element[:-1].strip()

        if not isAuthor and element[-1] == '.':
            # don't strip trailing periods from author names
            return element[:-1].strip()

        return element.strip()


if __name__ == "__main__":
     converter("USMARC UTF - 8.ISO")
