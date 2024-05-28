from .config_schema import Config_Schema

keys = ["firstname", "lastname", "address", "telephone"]


class Contact(Config_Schema):
    def __init__(self, args: dict):
        super().__init__(args)
        self.__firstname: str = args["firstname"]
        self.__lastname: str = args["lastname"]
        self.__address: list = []
        self.__telephone: list = []
        self.__values = [
            self.__firstname,
            self.__lastname,
            self.__address,
            self.__telephone,
        ]

    def set_name(self, firstname: str = "", lastname: str = ""):
        if firstname:
            self.__firstname = firstname
        if lastname:
            self.__lastname = lastname

        self.setvalues(dict(zip(keys, self.__values)))

    def set_address(self, address: str):
        if address:
            self.__address.append(address)

        self.setvalues(dict(zip(keys, self.__values)))

    def set_telephone(self, telephone: list):
        if telephone:
            self.__telephone.append(telephone)

        self.setvalues(dict(zip(keys, self.__values)))
