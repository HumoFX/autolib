from pymarc import MARCReader, JSONReader
reader = MARCReader(open('../media/file/marc/1.ISO', 'rb'), to_unicode=True,  file_encoding='utf-8')
for record in reader:
    print(record.as_json())