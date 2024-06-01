from os import getenv
from dotenv import load_dotenv
from manager import Manager
from schemas import Address

load_dotenv()
DATABASE = getenv("DATABASE")

mger = Manager(DATABASE)

new_address = Address({"contact_id": 1, "address": "Cortes, San Pedro Sula"})
mger.insert_address(Address)
