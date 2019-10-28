from Utilities import Utility as U


class FatTree:

    def __init__(self):
        pass

    @classmethod
    def createTopology(cls):
        strList = []
        K = int(input("Enter K:"))
        coreSwithces: int = (K//2)**2
        agrSwitches: int = (K**2)//2
        egdeSitches: int = agrSwitches
        racks: int = int((K**3)/4)
        allSwitches: int = coreSwithces+agrSwitches+egdeSitches
        allElements: int = allSwitches+racks

        # Build first index for each pod to connect pods to cores
        startIndex: list = []
        for i in range(K):
            startIndex.append(i)

        # Build a condition for every agr switch to connect to cord
        maxLimitOfAgrToCores: list = []
        for i in range(agrSwitches):
            maxLimitOfAgrToCores.append(0)

        counter = 0

        for i in range(allElements):
            for j in range(allElements):
                # compare rack with rack
                if i < racks and j < racks:
                    if i == j:
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                        continue
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                        continue
                # compare rack with edge
                if i < racks and j >= racks and j < racks+egdeSitches:
                    if (j-racks) == i//(K//2):
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                        continue

                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                        continue
                # compare racks with aggregations and cores
                if i < racks and j >= racks+egdeSitches:
                    U.uPrint(i, j, False)
                    strList.append(U.uText(i, j, False))
                    continue
                # compare edge(i) with racks(j)
                if i >= racks and i < racks+egdeSitches and j < racks:
                    if (i-racks) == j//(K//2):
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                        continue
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                        continue
                # compare edge with edge
                if i >= racks and i < racks+egdeSitches and j >= racks and j < racks+egdeSitches:
                    if i == j:
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                        continue
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                        continue
                # compare edge with aggregation
                if i >= racks and i < racks+egdeSitches and j >= racks+egdeSitches and j < racks+egdeSitches+agrSwitches:
                    if ((i-racks) // (K/2) == (j - racks-egdeSitches) // (K/2)):
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                        continue
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                        continue

                # compare edge with core
                if i >= racks and i < racks+egdeSitches and j >= racks+egdeSitches+agrSwitches:
                    U.uPrint(i, j, False)
                    strList.append(U.uText(i, j, False))
                    continue

                # compare aggregation with racks
                if i >= racks+egdeSitches and i < racks+egdeSitches+agrSwitches and j < racks:
                    U.uPrint(i, j, False)
                    strList.append(U.uText(i, j, False))
                    continue
                # compare aggregation with edge
                if i >= racks+egdeSitches and i < racks+egdeSitches+agrSwitches and j >= racks and j < racks+egdeSitches:
                    if ((i - racks-egdeSitches) // (K/2)) == (j-racks) // (K/2):
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                        continue
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                        continue
                # compare aggregation with aggregation
                if i >= racks+egdeSitches and i < racks+egdeSitches+agrSwitches and j >= racks+egdeSitches and j < racks+egdeSitches+agrSwitches:
                    if i == j:
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                        continue
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                        continue
                    # compare aggregation with core
                if i >= racks+egdeSitches and i < racks+egdeSitches+agrSwitches and j >= racks+egdeSitches + agrSwitches:
                    coreNumber = j-racks-egdeSitches-agrSwitches
                    podNumber: int = int((i - racks-egdeSitches) // (K/2))
                    agrNumber: int = int(i-racks-egdeSitches)
                    # if coreNumber == podNumber + startIndex[podNumber] and maxLimitOfAgrToCores[agrNumber] < K//2:
                    if maxLimitOfAgrToCores[agrNumber] < K//2:
                        z = startIndex[podNumber]+racks+egdeSitches+agrSwitches
                        U.uPrint(i, z, True)
                        strList.append(U.uText(i, z, True))
                        U.uPrint(z, i, True)
                        strList.append(U.uText(z, i, True))
                        startIndex[podNumber] += 1
                        startIndex[podNumber] = startIndex[podNumber] % K
                        maxLimitOfAgrToCores[agrNumber] += 1
                        continue
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                        U.uPrint(j, i, False)
                        strList.append(U.uText(j, i, False))
                        continue

                # compare core with racks and edge
                if i >= racks+egdeSitches + agrSwitches and j < racks+egdeSitches:
                    U.uPrint(i, j, False)
                    strList.append(U.uText(i, j, False))
                    continue
                # compare core with aggregation
                if i >= racks+egdeSitches + agrSwitches and j >= racks+egdeSitches and j < racks+egdeSitches+agrSwitches:
                    continue
                    # coreNumber = i-racks-egdeSitches-agrSwitches
                    # podNumber = int((j - racks-egdeSitches) // (K/2))
                    # if coreNumber == podNumber + startIndex[podNumber]:
                    #     U.uPrint(i, j, True)
                    #     startIndex[podNumber] += 1
                    #     startIndex[podNumber] = startIndex[podNumber] % 4
                    #     continue
                    # else:
                    #     U.uPrint(i, j, False)
                    #     continue
                # compare core with core
                if i >= racks+egdeSitches + agrSwitches and j >= racks+egdeSitches + agrSwitches:
                    if i == j:
                        U.uPrint(i, j, True)
                        strList.append(U.uText(i, j, True))
                        continue
                    else:
                        U.uPrint(i, j, False)
                        strList.append(U.uText(i, j, False))
                        continue

        U.writeToFile(strList)
