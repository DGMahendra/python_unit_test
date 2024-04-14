import pytest
from src.general_example import GeneralExample



@pytest.mark.parametrize('content,output',[({'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]},[0, 1, 2, 3, 10, 22, 42, 55])])
def test_flatten_dictionary(content,output):
    assert GeneralExample.flatten_dictionary(content)==output

@pytest.mark.parametrize('input_list,output_list',[(['emp001', 'Sam', '100000'],['emp001', 'Sam', '100000'])])
def test_load_employee_rec_from_database(input_list,output_list):
    assert GeneralExample.load_employee_rec_from_database(input_list)==output_list

@pytest.mark.parametrize("emp_id, emp_name, emp_salary, expected_result", [
    (22, "Mahi", 20000, {'empId': 22, 'empName': "Mahi", 'empSalary': 20000}),
    # Add more test cases here as needed
])
def test_fetch_emp_details(mocker, emp_id, emp_name, emp_salary, expected_result):
    mocker.patch('src.general_example.GeneralExample.load_employee_rec_from_database',
                 return_value=[emp_id, emp_name, emp_salary])

    general_example_instance = GeneralExample()

    # Calling the fetch_emp_details method on the instance
    result = general_example_instance.fetch_emp_details()

    assert result == expected_result

