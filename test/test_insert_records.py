import pytest
from os import getenv
from dotenv import load_dotenv

from manager import Manager
from schemas import Contact, Address, Telephone
from . import ARGS_LIST_CONTACTS, ARGS_LIST_ADDRESS, ARGS_LIST_TELEPHONE

load_dotenv()
DATABASE = getenv("DATABASE")


def test_start_database():
    mger = Manager(DATABASE)
    assert mger.start()


@pytest.mark.parametrize("contact_args", ARGS_LIST_CONTACTS)
def test_insert_new_contact(contact_args: dict):
    mger = Manager(DATABASE)
    assert mger.insert_contact(Contact(contact_args)) == True


@pytest.mark.parametrize("address_args", ARGS_LIST_ADDRESS)
def test_insert_new_address(address_args: dict):
    mger = Manager(DATABASE)
    assert mger.insert_address(Address(address_args)) == True


@pytest.mark.parametrize("telephone_args", ARGS_LIST_TELEPHONE)
def test_insert_new_telephone(telephone_args: dict):
    mger = Manager(DATABASE)
    assert mger.insert_telephone(Telephone(telephone_args)) == True
