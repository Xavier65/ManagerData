from typing import Any


class Config_Schema:
    def __init__(self, args: dict):
        self.__args: dict = args

    def setvalues(self, args: dict) -> None:
        self.__args: dict = args

    def get(self):
        key = [k for k, _ in self.__args.items()]
        return self.__args[key[1]]

    def getvalues(self):
        return tuple([v for _, v in self.__args.items()])

    def show(self):
        return self.__args
