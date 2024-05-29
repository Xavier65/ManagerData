from manager.insert_records import InsertRecords
from manager.find_records import FindRecords


class Manager(InsertRecords, FindRecords):
    def __init__(self, database: str) -> None:
        super().__init__(database)

    def start(self) -> None:
        return self.create_tables()
