import pytest
from os import getenv
from dotenv import load_dotenv
from manager import Manager

load_dotenv()
DATABASE = getenv("DATABASE")


@pytest.mark.parametrize(
    "search_args",
    ["pa", "rand", "uan", "and", "cos", "eles", "loza", "Loza", "jor"],
)
def test_find_contact(search_args: str):
    mger = Manager(DATABASE)
    result = mger.find_contact(search_args)
    assert result == []


@pytest.mark.parametrize("contact_id", [1, 2, 3, 4, 5])
def test_find_address(contact_id: int):
    mger = Manager(DATABASE)
    result = mger.find_address(contact_id)
    assert result != []


@pytest.mark.parametrize("contact_id", [1, 2, 3, 4, 5])
def test_find_address(contact_id: int):
    mger = Manager(DATABASE)
    result = mger.find_telephone(contact_id)
    assert result != []
