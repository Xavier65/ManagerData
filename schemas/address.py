class Address:
    def __init__(self, args: dict):
        self.__contact_id: int = args["contact_id"]
        self.__address: str = args["address"]

    def get_id(self) -> int:
        return self.__contact_id

    def get_address(self) -> str:
        return self.__address

    def get(self) -> tuple:
        return (self.__contact_id, self.__address)

    def show(self) -> dict:
        return {"contact_id": self.__contact_id, "address": self.__address}

    def set_id(self, id: int) -> None:
        self.__contact_id = id

    def set_address(self, adress: str) -> None:
        self.__address = adress
