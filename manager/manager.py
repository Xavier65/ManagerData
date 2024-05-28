from manager import ConfigManager

from schemas import Contact
from schemas import Address
from schemas import Telephone


class Manager(ConfigManager):
    def __init__(self, database: str) -> None:
        super().__init__(database)

    def start(self) -> None:
        self.create_tables()

    def insert_contact(self, contact: Contact) -> bool:
        try:
            sentence: str = (
                f"INSERT INTO Contact (firstname, lastname) VALUES {contact.getvalues()}"
            )
            self.execute_sentence(sentence)
            self.commit()
            return True
        except Exception as e:
            print(f"Error {e} -> Manager.insert_contact")

    def insert_address(self, address: Address) -> bool:
        try:
            sentence: str = (
                f"INSERT INTO Address (contact_id, address) VALUES {address.getvalues()}"
            )
            self.execute_sentence(sentence)
            self.commit()
            return True
        except Exception as e:
            print(f"Error {e} -> Manager.insert_address")

    def insert_telephone(self, telephone: Telephone):
        try:
            sentence: str = (
                f"INSERT INTO TelephoneNumber (contact_id, telephone_number) VALUES {telephone.getvalues()}"
            )
            self.execute_sentence(sentence)
            self.commit()
        except Exception as e:
            print(f"Error {e} -> Manager.insert_telephone")
