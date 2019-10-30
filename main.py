from DataCenterTopologies.FatTree import FatTree
from DataCenterTopologies.BCube import BCube

print("This app print out Fat-Tree and BCube Topologies")
select = int(input("type 1 for Fat-Tree or type 2 for BCube: "))
if select == 1:
    FatTree.createTopology()
elif select == 2:
    BCube.createTopology()
else:
    print("Oops! 😒")
