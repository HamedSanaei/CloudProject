class Utility:

    @classmethod
    def uPrint(cls, sourceSwitch, destinatonSwitch, isConnected: bool):
        if isConnected == True:
            print(f"{sourceSwitch}      {destinatonSwitch}      {1}")
        else:
            print(f"{sourceSwitch}      {destinatonSwitch}      {99999}")

    @classmethod
    def writeToFile(cls):
        pass
