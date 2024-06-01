class Telephone:
    def __init__(self, args: dict):
        self.__contact_id: str = args["contact_id"]
        self.__telephones: str = args["telephone"]

    def get_id(self) -> int:
        return self.__contact_id

    def get_telephones(self) -> list:
        return self.__telephones

    def get(self) -> tuple:
        return (self.__contact_id, self.__telephones)

    def show(self) -> dict:
        return {"contac_id": self.__contact_id, "telephone": self.__telephones}

    def set_id(self, id: int) -> None:
        self.__contact_id = id

    def set_telephone(self, telephone: str) -> None:
        self.__telephones = telephone
