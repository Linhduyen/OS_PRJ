import part2


def checkTLB(pageNumber, physicalMemory, offset, logicalAddress, tlb, i, outputFile):
    for j in range(len(tlb)):
        if pageNumber == tlb[j][0]:
            print("Page Number \"" + str(pageNumber) + "\" found in TLB!!")
            frameNumber = tlb[j][1]
            data = part2.readPhysicalMemory(frameNumber, offset, physicalMemory)
            physicalAddress = "{0:08b}".format(int(frameNumber)) + "{0:08b}".format(offset)
            physicalAddress = int(physicalAddress, 2)
            outStr = str(i) + " Virtual address: " + str(logicalAddress) + " Physical address: " + str(
                physicalAddress) + " Value: " + data + "\n"
            print(str(i) + " Virtual address: " + str(logicalAddress) + " Physical address: " + str(
                physicalAddress) + " Value: " + data)
            outputFile.write(outStr)
            part2.updateTLBCounter(j, tlb)
            return 1

    return 0


def checkPageTable(pageNumber, logicalAddress, offset, i,pageTable_queue, pageTable, physicalMemory, outputFile):
    
    if pageTable[pageNumber] != -1: 
        print("Page Number \"" + str(pageNumber) + "\" found in page table!!")
        frameNumber = pageTable[pageNumber]
        data = part2.readPhysicalMemory(frameNumber, offset, physicalMemory)
        physicalAddress = "{0:08b}".format(int(frameNumber)) + "{0:08b}".format(offset)
        physicalAddress = int(physicalAddress, 2)
        outStr = str(i) + " Virtual address: " + str(logicalAddress) + " Physical address: " + str(
            physicalAddress) + " Value: " + data + "\n"
        print(str(i) + " Virtual address: " + str(logicalAddress) + " Physical address: " + str(
            physicalAddress) + " Value: " + data)
        outputFile.write(outStr)
        part2.updatepageTableCounter(pageNumber, pageTable_queue)
        return 1

    return 0
