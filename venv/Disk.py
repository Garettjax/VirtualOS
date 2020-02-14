class Disk:


    def __init__(self):
        self.memory = [None] * 4028
        # print(diskMemory[0])


    def setDiskData(self, data, location):
        diskMemory[location] = data