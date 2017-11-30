from employee import Employee

test_employee = Employee(0, 'daniela', '1993', 'sql;python;powerbi')
test_employee.add_supervisor('juraj')

def test_init():
    assert isinstance(test_employee.name, str)
    assert isinstance(test_employee.birth_year, int)
    assert isinstance(test_employee.age, int)
    assert isinstance(test_employee.skills, list)


def test_add_supervisor():
    assert isinstance(test_employee.supervisor, str)