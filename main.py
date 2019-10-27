from Models.Utilities import Utility as U

K = int(input("Enter K:"))
coreSwithces: int = (K//2)**2
agrSwitches: int = (K**2)//2
egdeSitches: int = agrSwitches
racks: int = int((K**3)/4)
allSwitches: int = coreSwithces+agrSwitches+egdeSitches
allElements: int = allSwitches+racks

counter = 0
# for e in range(egdeSitches):
#     print(f"{int(e*(K/2))}  {int(e+racks)}    1")
#     print(f"{int(e+racks)}  {int(e*(K/2))}    1")
#     print(f"{int(e+racks)}  {int(e*(K/2)+1)}   1")
#     print(f"{int(e*(K/2)+1)}  {int(e+racks)}   1")

# for e in range(egdeSitches):
#     for r in range(racks):
#         if e == r*K/2
#         print("x")
#         elif e :


for i in range(allElements):
    for j in range(allElements):
        # compare rack with rack
        if i < racks and j < racks:
            if i == j:
                U.uPrint(i, j, True)
                continue
            else:
                U.uPrint(i, j, False)
                continue
        # compare rack with edge
        if i < racks and j >= racks and j < racks+egdeSitches:
            if (j-racks)*K//2 == i:
                U.uPrint(i, j, True)
                continue
            elif ((j-racks)*K//2)+1 == i:
                U.uPrint(i, j, True)
                continue
            else:
                U.uPrint(i, j, False)
                continue
        # compare racks with aggregations and cores
        if i < racks and j >= racks+egdeSitches:
            U.uPrint(i, j, False)
            continue
        # compare edge(i) with racks(j)
        if i >= racks and i < racks+egdeSitches and j < racks:
            if (i-racks)*K//2 == j:
                U.uPrint(j, i, True)
                continue
            elif ((i-racks)*K//2)+1 == j:
                U.uPrint(j, i, True)
                continue
            else:
                U.uPrint(j, i, False)
                continue
        # compare edge with edge
        if i >= racks and i < racks+egdeSitches and j >= racks and j < racks+egdeSitches:
            if i == j:
                U.uPrint(i, j, True)
                continue
            else:
                U.uPrint(i, j, False)
                continue
        # compare edge with aggregation
        if i >= racks and i < racks+egdeSitches and j >= racks+egdeSitches and j < racks+egdeSitches+agrSwitches:
            if ((i-racks) % (K/2) == (j - racks-egdeSitches) % (K/2)):
                U.uPrint(i, j, True)
                continue
            else:
                U.uPrint(i, j, False)
                continue

        # compare edge with core
        # compare aggregation with racks
        # compare aggregation with edge
        # compare aggregation with core
        # compare core with racks and edge
        # compare core with aggregation
        # compare core with core
# یک تابع برای پرینت و یکی هم برای نوشتن در فایل بنویس
