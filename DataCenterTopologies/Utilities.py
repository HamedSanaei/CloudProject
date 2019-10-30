from pathlib import Path


class Utility:

    @classmethod
    def uPrint(cls, sourceSwitch, destinatonSwitch, isConnected: bool):
        if isConnected == True:
            print(f"{sourceSwitch}      {destinatonSwitch}      {1}")
        else:
            print(f"{sourceSwitch}      {destinatonSwitch}      {99999}")

    @classmethod
    def uText(cls, sourceSwitch, destinatonSwitch, isConnected: bool):
        if isConnected == True:
            return f"{sourceSwitch}      {destinatonSwitch}      {1}"
        else:
            return f"{sourceSwitch}      {destinatonSwitch}      {99999}"

    @classmethod
    def writeToFile(cls, strList: list):
        #print("File      Path:", Path(__file__).absolute())
        #print("Directory Path:", Path().absolute())
        txtPath = Path().absolute() / "Print.txt"
        if txtPath.exists():
            txtPath.unlink()
            # txtPath.write_text("")
            with open(txtPath, 'w') as f:
                for item in strList:
                    f.write(f"{item} \n")

        else:
            with open(txtPath, 'w') as f:
                for item in strList:
                    f.write("%s\n" % item)
