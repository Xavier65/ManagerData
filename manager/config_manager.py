from sqlite3 import Connection, Row, Cursor


class ConfigManager:
    def __init__(self, database: str):
        self.__database: str = database
        self.__conn: Connection = Connection(self.__database)

    def execute_sentence(self, sentence_sql) -> Cursor:
        try:
            self.__conn.row_factory = Row
            cursor = self.__conn.cursor()
            return cursor.execute(sentence_sql)
        except Exception as e:
            print(f"{e} -> ConfigManager.execute_sentence")

    def commit(self) -> None:
        try:
            self.__conn.commit()
        except Exception as e:
            print(f"{e} -> Manager.commit")

    def create_tables(self) -> bool:
        try:
            cursor = self.__conn.cursor()
            with open("manager/script.sql", "r") as script:
                cursor.executescript(script.read())
            self.commit()
            print(f"Tables created!")
            return True
        except Exception as e:
            print(f"Error {e} -> ConfigManager.create_tables")
