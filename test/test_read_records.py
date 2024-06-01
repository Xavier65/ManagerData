import pytest
from os import getenv
from dotenv import load_dotenv
from manager import Manager

from . import ARGS_LIST_CONTACTS

load_dotenv()
DATABASE = getenv("DATABASE")
EMPTY: list = []

search: list = [
    "pa",
    "rand",
    "uan",
    "and",
    "cos",
    "eles",
    "loza",
    "Loza",
    "jor",
    "firs",
    "ree",
    "second",
]


@pytest.mark.parametrize("search_args", search)
def test_find_contact(search_args: str):
    mger = Manager(DATABASE)
    result = mger.find_contact(search_args)
    assert result == EMPTY


@pytest.mark.parametrize("contact_id", [range(1, 12)])
def test_find_address(contact_id: int):
    mger = Manager(DATABASE)
    result = mger.find_address(contact_id)
    assert result != EMPTY


@pytest.mark.parametrize("contact_id", [range(1, 12)])
def test_find_telephone(contact_id: int):
    mger = Manager(DATABASE)
    result = mger.find_telephone(contact_id)
    assert result != EMPTY
