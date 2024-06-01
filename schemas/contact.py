class Contact:
    def __init__(self, args: dict):
        self.__firstname: str = args["firstname"]
        self.__lastname: str = args["lastname"]
        self.__address: list = []
        self.__telephone: list = []

    def get_id(self) -> int:
        return self.__id

    def get_firstname(self) -> str:
        return self.__firstname

    def get_lastname(self) -> str:
        return self.__lastname

    def get_address(self) -> list:
        return self.__address

    def get_telephone(self) -> list:
        return self.__telephone

    def get_names(self) -> tuple:
        return (self.__firstname, self.__lastname)

    def show(self) -> dict:
        return {
            "id": self.__id,
            "firstname": self.__firstname,
            "lastname": self.__lastname,
            "address": self.__address,
            "telephone": self.__telephone,
        }

    def set_id(self, id: int) -> None:
        self.__id = id

    def set_address(self, address: list):
        if address:
            self.__address = address.copy()

    def set_telephone(self, telephone: list):
        if telephone:
            self.__telephone = telephone.copy()
