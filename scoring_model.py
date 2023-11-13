import numpy as np
import re


class main_class:
    def __init__(self, param):
        """
        Function takes parameters (param) as JSON and transforms tham into str and int for each parameter
        PIN_CODE - str, UNICAL_CODE - int, APP_ID - str
        """
        self.param = str(param)
        
        PIN_CODE_match = re.search(r"PIN_CODE='(\d+)'", self.param)
        UNICAL_CODE_match = re.search(r"UNICAL_CODE=(\d+)", self.param)
        APP_ID_match = re.search(r"APP_ID='(\{[\w\d]+\})'", self.param)

        self.PIN_CODE = PIN_CODE_match.group(1) if PIN_CODE_match else None
        self.UNICAL_CODE = int(UNICAL_CODE_match.group(1)) if UNICAL_CODE_match else None
        self.APP_ID = APP_ID_match.group(1) if APP_ID_match else None

    def check(self):
        """
        Function checks if PIN_CODE's length is 7, UNICAL_CODE's length is 11, APP_ID's length is 25 
        and it starts and ends with {}. It returns True and None if everything is right and False 
        and the name of parameter if not
        """
        if (len(self.PIN_CODE) != 7) or (not isinstance(self.PIN_CODE, str)):
            return (False, 'PIN_CODE')
        
        if  (not isinstance(self.UNICAL_CODE, int)) or (len(str(self.UNICAL_CODE)) != 10):
            return (False, 'UNICAL_CODE')
        
        if (not isinstance(self.APP_ID, str)) or (self.APP_ID is None) or (len(self.APP_ID) != 25) or (self.APP_ID[0] != "{") or (self.APP_ID[-1] != "}"):
            return (False, 'APP_ID')
        
        return (True, None)
    
    def random(self):
        """
        Function creates random number and returns it
        """
        num = np.random.randint(1, 101)
        return num



def scoring_func(param):
    """
    Main function that takes parameters (param), checks if 'check' function returns True
    and if TRUE it gets random number from 'random' function, if FALSE returns a mistake message 
    """
    my_object = main_class(param)
    check_res, error = my_object.check()
    if check_res == True:
        rand_num = my_object.random()
        print(rand_num)
        return rand_num
    else:
        print('smth wrong')
        print(error)
        return error


    

