from schemas import Contact, Address, Telephone
from manager.config_manager import ConfigManager


class InsertRecords(ConfigManager):
    def __init__(self, database: str):
        super().__init__(database)

    def insert_contact(self, contact: Contact) -> bool:
        try:
            sentence: str = (
                f"INSERT INTO Contact (firstname, lastname) VALUES {contact.get_names()}"
            )
            self.execute_sentence(sentence)
            self.commit()
            return True
        except Exception as e:
            print(f"Error {e}")

    def insert_address(self, address: Address) -> bool:
        try:
            sentence: str = (
                f"INSERT INTO Address (contact_id, address) VALUES {address.get()}"
            )
            self.execute_sentence(sentence)
            self.commit()
            return True
        except Exception as e:
            print(f"Error {e} -> Manager.insert_address")

    def insert_telephone(self, telephone: Telephone) -> bool:
        try:
            sentence: str = (
                f"INSERT INTO TelephoneNumber (contact_id, telephone_number) VALUES {telephone.get()}"
            )
            self.execute_sentence(sentence)
            self.commit()
            return True
        except Exception as e:
            print(f"Error {e} -> Manager.insert_telephone")
