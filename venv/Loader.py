from PCB import PCB
class Loader:

    def __init__(self):
        self.run()

    def run(self):
        try:
            file = open("program_file")

            for line in file:
                # print(line)
                if "//" in line:
                    card = line[3: int(len(line) - 1)]
                    pcb = PCB()

                    arr = card.split(" ")
                    pcb.type = arr[0]
                    pcb.jobId = arr[1]
                    pcb.numberOfJobs = int("0x" + arr[2], 0)
                    pcb.priority = arr[3]

                    # print(card)
                    print(pcb.type)
                    print(pcb.jobId)
                    print(pcb.priority)
                    print(pcb.numberOfJobs)
                else:
                    print(line)

            file.close()
        except Exception as ex:
            print(ex.args)

