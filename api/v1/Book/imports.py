import csv
from typing import List

from .models import *
from django.core.files.storage import default_storage
from django.db.transaction import atomic
from django.http import HttpResponse
from rest_framework import status
from .convert import converter


# def check_departments(department_names) -> str:
    # old_depots = set(
    #     Department.objects.values_list("short_name", flat=True)
    # )
    # if difference := set(department_names) - old_depots:
    #     return f"Following Departments don't exist: {difference}"


# def check_registration_no(registrations, cars) -> List:
    # reg_errors = []
    # if incorrect_reg_no := [number for number in registrations if len(number) > 7]:
    #     reg_errors.append(
    #         f"Following registration numbers are too long: {incorrect_reg_no}"
    #     )
    # if common := set(Car.objects.values_list("registration_no", flat=True)) & set(
    #     cars.keys()):
    #     reg_errors.append(f"Following registration numbers already exists: {common}")
    # return reg_errors


@atomic
def import_process(file_name):
    cars = []
    # departments = {}
    # department_names = []
    # registration_numbers = []
    # errors = []

    file = default_storage.open(converter(file_name))
    print(file)
    decoded_file = file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(decoded_file)

    for row in reader:
        car = Book(
            university_id=1,
            title=row["title"],
            isbn=row["isbn"],
            note=row["note"],
            # authors.set(row["author"]),
            # publisher=row["publisher"],
            publication_date=row["pubyear"],
        )
         # car.department_name = row["department"]
        # department_names.append(row["department"])
        # registration_numbers.append(row["registration_no"])
        # cars[row["registration_no"]] = car
        cars.append(car)
        # departments[row["registration_no"]] = row["department"]

    # if departments_errors := check_departments(department_names):
    #     errors.append(departments_errors)
    #
    # if reg_errors := check_registration_no(registration_numbers, cars):
    #     errors.append(reg_errors)
    #
    # if errors:
    #     return HttpResponse(errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    #
    # db_departments = Department.objects.filter(short_name__in=department_names).in_bulk(field_name="short_name")

    # for name, car in cars.items():
    #     car.department = db_departments[car.department_name]
    #     delattr(car, "department_name")
    try:
        Book.objects.bulk_create(cars)
    except Exception as e:
        return HttpResponse(e, status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse("Your file has been successfully uploaded", status=status.HTTP_200_OK)
