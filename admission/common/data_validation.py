from datetime import datetime

import re
import sys

class DataValidation(object):

    def __init__(self):
        self.invalid_param = []
        pass

    def primary_data_validation(self,pattern, value, param):
        pattern_select = {'name_space': '^[a-zA-Z]*[a-zA-Z]$', 'date': '^[0-9]{4}-[0-9]{2}-[0-9]{2}$',
                          'blood_grp': '^[a-bA-BoO]+[+-]$', 'occupation':'^[a-zA-Z ]*[a-zA-Z]$',
                          'income': '^[0-9]+$', 'phone_num': '^[+0-9]{10}$'}
        self.__pattern = pattern_select[pattern]
        self.__value = value
        self.__param = param
        if self.__value != None and self.__value != '':
            if re.findall(self.__pattern, self.__value) != []:
                return self.__value
            else:
                self.invalid_param.append(self.__param)
                return ""
        else:
            self.invalid_param.append(self.__param)
            return ""

    def specific_data_validation(self, data_list, value, param):
        self.__data_list = data_list
        self.__value = value
        self.__param = param
        if self.__value in self.__data_list:
            return self.__value
        else:
            self.invalid_param.append(self.__param)
            return ""

    def age_calculate(self,DOB):
        print DOB
        print self.invalid_param
        self.__DOB = DOB
        b_date = datetime.strptime(self.__DOB, '%Y-%m-%d')
        self.age = (datetime.today() - b_date).days/365
        return self.age

    def class_validate(self,admit_to):
        self.__admit_to = admit_to
        if admit_to == 'LKG':
            self.__class_enum = -1
        elif admit_to == 'UKG':
            self.__class_enum = 0
        else:
            self.__class_enum = eval(re.findall('Class([\d]+)',admit_to)[0])

        if (self.age - (self.__class_enum + 1)) < 5:
            self.invalid_param.append("Under Aged")