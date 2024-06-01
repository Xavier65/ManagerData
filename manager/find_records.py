from manager.config_manager import ConfigManager
from schemas import Contact


class FindRecords(ConfigManager):
    def __init__(self, database: str):
        super().__init__(database)

    def find_contact(self, search: str) -> list:
        try:
            sentence: str = (
                f"SELECT * FROM Contact WHERE firstname like '%{search}%' or lastname like '%{search}%'"
            )
            rows = self.execute_sentence(sentence)
            contact_found: list = []
            for row in rows.fetchall():
                contact = Contact(dict(row))
                contact.set_id(row["id"])
                contact.set_address(self.find_address(row["id"]))
                contact.set_telephone(self.find_telephone(row["id"]))
                contact_found.append(contact)

            return [contact.show() for contact in contact_found]

        except Exception as e:
            print(f"Error: {e}")

    def find_address(self, contact_id: int) -> list:
        try:
            sentence: str = f"SELECT * FROM Address WHERE contact_id = {contact_id}"
            rows = self.execute_sentence(sentence)
            records = [dict(row) for row in rows.fetchall()]
            return [record["address"] for record in records]
        except Exception as e:
            print(f"Error {e}")

    def find_telephone(self, contact_id: int) -> list:
        try:
            sentence: str = (
                f"SELECT * FROM TelephoneNumber WHERE contact_id = {contact_id}"
            )
            result = self.execute_sentence(sentence)
            return [dict(row)["telephone_number"] for row in result.fetchall()]
        except Exception as e:
            print(f"Error {e}")
