from manager.config_manager import ConfigManager


class FindRecords(ConfigManager):
    def __init__(self, database: str):
        super().__init__(database)

    def find_contact(self, search: str) -> list:
        try:
            sentence: str = (
                f"SELECT * FROM Contact WHERE firstname like '%{search}%' or lastname like '%{search}%'"
            )
            result = self.execute_sentence(sentence)
            return [dict(row) for row in result.fetchall()]
        except Exception as e:
            print(f"Error: {e}")

    def find_address(self, contact_id: int) -> list:
        try:
            sentence: str = f"SELECT * FROM Address WHERE contact_id = {contact_id}"
            result = self.execute_sentence(sentence)
            return [dict(row) for row in result.fetchall()]
        except Exception as e:
            print(f"Error {e}")

    def find_telephone(self, contact_id: int) -> list:
        try:
            sentence: str = (
                f"SELECT * FROM TelephoneNumber WHERE contact_id = {contact_id}"
            )
            result = self.execute_sentence(sentence)
            return [dict(row) for row in result.fetchall()]
        except Exception as e:
            print(f"Error {e}")
