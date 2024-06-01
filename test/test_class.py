import pytest

from schemas import Contact, Address, Telephone

from . import ARGS_LIST_CONTACTS, ARGS_LIST_ADDRESS, ARGS_LIST_TELEPHONE


@pytest.mark.parametrize("args", ARGS_LIST_CONTACTS)
def test_create_contact(args: dict):
    contact = Contact(args)
    contact.set_id(args["id"])
    assert contact.get_id() == args["id"]
    assert contact.get_firstname() == args["firstname"]
    assert contact.get_lastname() == args["lastname"]
    assert contact.get_names() == (args["firstname"], args["lastname"])
    contact.set_address(args["address"])
    assert contact.get_address() == args["address"]
    contact.set_telephone(args["telephone"])
    assert contact.get_telephone() == args["telephone"]
    assert contact.show() == args


@pytest.mark.parametrize("args", ARGS_LIST_ADDRESS)
def test_create_address(args: list):

    address = Address(args)
    address.set_id(args["contact_id"])
    assert address.get_id() == args["contact_id"]
    assert address.get_address() == args["address"]
    assert address.show() == {
        "contact_id": args["contact_id"],
        "address": args["address"],
    }


@pytest.mark.parametrize("args", ARGS_LIST_TELEPHONE)
def test_create_telephone(args: list):
    telephone = Telephone(args)
    telephone.set_id(args["contact_id"])
    assert telephone.get_id() == args["contact_id"]
    assert telephone.get_telephones() == args["telephone"]
    assert telephone.show() == {
        "contac_id": args["contact_id"],
        "telephone": args["telephone"],
    }
