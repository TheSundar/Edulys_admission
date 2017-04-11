"""

File is used to create base and data to run the school app

"""
# python imports
import os
import json
import sys

PROJDIR = os.path.abspath(r"..\..")
if PROJDIR not in sys.path:
    sys.path.append(PROJDIR)

os.environ["DJANGO_SETTINGS_MODULE"] = "edulys.settings"

import django

django.setup()

from admission.models import ClassDetails

BASE_DATA_FOLDER = os.path.join(os.getcwd(), 'data')


def fill_class():
    """
     fills the class to the models
    :return: None
    """
    with open(BASE_DATA_FOLDER + '/class.json', 'r') as classdata:
        data = json.loads(classdata.read())
        print data
        for i in data['data']:
            try:
                cl_data = ClassDetails.objects.get(class_name=i)
            except:
                cl_data = ClassDetails(class_name=i)
                cl_data.save()


def main():
    fill_class()


if __name__ == '__main__':
    main()
