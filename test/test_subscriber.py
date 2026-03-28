import pytest

from subscriber import Subscriber


@pytest.fixture(scope="module")
def sub():
    sub_obj = Subscriber("102030", "Pierre", "Mulamba", 19690205)
    yield sub_obj


@pytest.mark.parametrize("test_input", ["Pierre", "Abraham", "Mutombo"])
# return the Subscriber first name
def test_ge_first_name(sub, test_input):
    result = sub.get_first_name
    assert result == test_input


# return the Subscriber last name
@pytest.mark.parametrize("test_input", ["John", "Mulamba", "Cena"])
def test_get_last_name(sub, test_input):
    result = sub.get_last_name
    assert result == test_input
