from os import getenv
from dotenv import load_dotenv

from manager import Manager
from schemas import Contact
from schemas import Address
from schemas import Telephone

load_dotenv()
DATABASE = getenv("DATABASE")

mger = Manager(DATABASE)
mger.start()

contact1 = Contact({"firstname": "Juan", "lastname": "Hernandez"})
address1 = Address({"contact_id": 1, "address": "Wall Street 21th"})
telephone1 = Telephone({"contact_id": 1, "telephone_number": "+502 9843-9234"})

mger.insert_contact(contact1)
mger.insert_address(address1)
mger.insert_telephone(telephone1)
