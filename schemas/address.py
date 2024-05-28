from .config_schema import Config_Schema


class Address(Config_Schema):
    def __init__(self, args: dict):
        super().__init__(args)
        self.__contact_id: int = args["contact_id"]
        self.__address: str = args["address"]

    def set_address(self, address: str):
        self.__address = address
        keys = ["contact_id", "address"]
        values = [self.__contact_id, self.__address]
        self.setvalues(dict(zip(keys, values)))
