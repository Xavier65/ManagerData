from .config_schema import Config_Schema


class Telephone(Config_Schema):
    def __init__(self, args: dict):
        super().__init__(args)
        self.__contact_id: int = args["contact_id"]
        self.__telephone_number: str = args["telephone_number"]

    def set_telephone(self, telephone_number: str):
        self.__telephone_number = telephone_number
        keys = ["contact_id", "telephone_number"]
        values = [self.__contact_id, self.__telephone_number]
        self.setvalues(dict(zip(keys, values)))
