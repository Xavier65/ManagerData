import pytest
from os import getenv
from dotenv import load_dotenv

from manager import Manager
from schemas import Contact, Address, Telephone

load_dotenv()
DATABASE = getenv("DATABASE")


def test_start_database():
    mger = Manager(DATABASE)
    assert mger.start()


@pytest.mark.parametrize(
    "contact_args",
    [
        ({"firstname": "Paolo", "lastname": "Brand"}),
        ({"firstname": "Juan", "lastname": "Hernandez"}),
        ({"firstname": "Juan", "lastname": "Manueles"}),
        ({"firstname": "Marcos", "lastname": "Fernandez"}),
        ({"firstname": "Jorge", "lastname": "Lozano"}),
    ],
)
def test_insert_new_contact(contact_args: list):
    mger = Manager(DATABASE)
    assert mger.insert_contact(Contact(contact_args)) == True


@pytest.mark.parametrize(
    "address_args",
    [
        ({"contact_id": 1, "address": "Wall Stree 21Th"}),
        ({"contact_id": 2, "address": "Main Stree 31Th"}),
        ({"contact_id": 3, "address": "Florida Stree 1Th"}),
        ({"contact_id": 4, "address": "Ioio Stree 12Th"}),
        ({"contact_id": 5, "address": "Minesota  Main 7th Stree, 8th Aveniu"}),
        ({"contact_id": 3, "address": "Mexico D.F Procedes 21, Calle Principal"}),
    ],
)
def test_insert_new_address(address_args: list):
    mger = Manager(DATABASE)
    assert mger.insert_address(Address(address_args)) == True


@pytest.mark.parametrize(
    "telephone_args",
    [
        ({"contact_id": 1, "telephone_number": "+504 8923-9234"}),
        ({"contact_id": 2, "telephone_number": "+502 8923-9234"}),
        ({"contact_id": 3, "telephone_number": "+503 823-9234"}),
        ({"contact_id": 4, "telephone_number": "+505 9342-9234"}),
        ({"contact_id": 5, "telephone_number": "+507 8923-8947"}),
        ({"contact_id": 4, "telephone_number": "+509 893-9234"}),
        ({"contact_id": 3, "telephone_number": "+504 923-9234"}),
        ({"contact_id": 2, "telephone_number": "+504 8923-9383"}),
    ],
)
def test_insert_new_telephone(telephone_args: list):
    mger = Manager(DATABASE)
    assert mger.insert_telephone(Telephone(telephone_args)) == True
