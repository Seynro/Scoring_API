from scoring_model import main_class
import pytest
import json


user_1 = "PIN_CODE='1234567', UNICAL_CODE=1234567890, APP_ID='{AaBb123456789CcDddEefq1}'"
user_2 = "PIN_CODE='123456', UNICAL_CODE=1234567890, APP_ID='{abcdef123456789012345}'"
user_3 = "PIN_CODE='1234567', UNICAL_CODE=123456789, APP_ID='{abcdef123456789012345}'"
user_4 = "PIN_CODE='1234567', UNICAL_CODE=1234567890, APP_ID='{abcdef1234567890125}'"

True_value = True


@pytest.mark.parametrize("input_user, expected_output", [
    (user_1, True_value),
    (user_2, True_value),
    (user_3, True_value),
    (user_4, True_value)
])
class TestModel:
    def test_check(self, input_user, expected_output):
        my_object = main_class(input_user)
        check_res, error = my_object.check()
        print(check_res)
        print(error)
        assert check_res == expected_output

pytest.main(["-v", "-s"])
