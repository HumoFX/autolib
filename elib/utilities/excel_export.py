from io import BytesIO
from typing import List
from numbers import Number
from django.db import models

import openpyxl as xl
from openpyxl.writer.excel import save_virtual_workbook


def export_from_queryset(queryset: models.QuerySet, fields: List[str]) -> BytesIO:
    workbook = xl.Workbook()
    worksheet = workbook.active

    header = []
    for field in fields:
        subfields: List[str] = field.split('.')
        header.append(subfields.pop())

    worksheet.append(header)

    for item in queryset:
        row = []
        for field in fields:
            subfields: List[str] = field.split('.')
            first_field = subfields.pop(0)
            if hasattr(item, first_field):
                subitem = getattr(item, first_field)
                for subfield in subfields:
                    subitem = getattr(subitem, subfield)
                if not isinstance(subitem, Number):
                    row.append(str(subitem))
                else:
                    row.append(subitem)
            else:
                row.append('')
        worksheet.append(row)

    virtual_workbook = save_virtual_workbook(workbook)
    return BytesIO(virtual_workbook)
