class Switch:
    # class level attributes
    #firstOutput: Switch = Switch(10)

    # self means compiler prepare currnet instance as a value for the called method
    # constructor method
    def __init__(self, number, stype):
        # instance level attributes
        # using property
        self.__number = number
        self.stype = stype

    def __str__(self) -> str:
        return f"this is switch number:({self.number}) with type:({self.stype})"

    # define a class method
    @classmethod
    def factoryMethod(cls) -> Switch:
        return cls(0, "core")

    @property
    def stype(self):
        return self.__stype

    @stype.setter
    def stype(self, stype: str):
        self.__stype = stype

    # A readonly property
    @property
    def number(self):
        return self.__number

    @property
    def connectedSwithes(self):
        return self.__connectedSwithes

    @connectedSwithes.setter
    def connectedSwithes(self, switchList: list):
        self.__connectedSwithes = switchList
