import pytest
from src import pour_tea

@pytest.mark.parametrize('with_milk,with_sugars,expected_string', [
    (False, 0, 'Black tea'),
    (True, 0, 'White tea'),
    (False, 1, 'Black tea and 1 sugar'),
    (True, 1, 'White tea and 1 sugar'),
    (True, 2, 'White tea and 2 sugars'),
])
def test_tea_machine_test_cases(with_milk, with_sugars, expected_string):
    output = pour_tea(with_milk=with_milk, sugars=with_sugars)
    assert output == expected_string

if __name__ == '__main__':
    path = os.path.abspath(__file__).replace('\\', '/')
    pytest.main('-q --tb=native ' + path)
