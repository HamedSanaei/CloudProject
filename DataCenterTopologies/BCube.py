from Topology import Topology
from Utilities import Utility as U


class BCube(Topology):

    @classmethod
    def createTopology(cls):
        k = int(input("Enter server port's count minus 1 =  K: "))
        n = int(input("Enter switch port's count =  N: "))

        racks = n**(k+1)
        bcubes = n**k
        levelSwithes = bcubes
        levels = k+1
        switches = (k+1)*bcubes
        allElement = switches + racks

        strList = []
        numOfPorts = n
        numOfShifts = 1
        # cube coverage indicates how many cube
        cubeCoverage = numOfShifts
        row = 0
        connectedServers = list(range(n))
        for level in range(levels):
            # currentServer show the precise current server we are trying connect to switches
            # resetTo means the first server we should strating from it to connect it to switch in the cubes
            currentServer, resetTo, counter = 0, 0, 0
            for cube in range(bcubes):
                # this for connect the each switch to it's servers
                switchNumber = (level * levelSwithes) + cube+racks
                currentServer = resetTo
                for port in range(numOfPorts):
                    # print
                    U.uPrint(currentServer, switchNumber, True)
                    strList.append(U.uText(currentServer, switchNumber, True))
                    U.uPrint(switchNumber, currentServer, True)
                    strList.append(U.uText(switchNumber, currentServer, True))

                    connectedServers[port] = currentServer
                    currentServer += numOfShifts
                    counter += 1
                # check the switch in each cube to get disconnect server
                for server in range(racks):
                    if not connectedServers.__contains__(server):
                        U.uPrint(server, switchNumber, False)
                        strList.append(U.uText(server, switchNumber, False))
                        U.uPrint(switchNumber, server, False)
                        strList.append(U.uText(switchNumber, server, False))

                if level > 0:
                    cubeCoverage -= 1
                    if (cube+1)*numOfPorts == counter and cubeCoverage == 0:
                        resetTo = (cube+1)*numOfPorts
                        currentServer = resetTo
                    else:
                        resetTo += 1
                        currentServer = resetTo
                    # the last time it becomes zero we fixed it
                    if cubeCoverage == 0:
                        cubeCoverage = numOfShifts

            numOfShifts *= numOfPorts
            cubeCoverage = numOfShifts

        # copare racks with racks and switches with switches
        for i in range(allElement):
            for j in range(allElement):
                if i < racks and j < racks:
                    if i == j:
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                elif i >= racks and j >= racks:
                    if i == j:
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
        U.writeToFile(strList)
