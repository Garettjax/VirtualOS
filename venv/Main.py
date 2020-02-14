from Disk import Disk
from Loader import Loader

try:
    disk = Disk()
    loader = Loader()
    # for index in disk.memory:
    #     print(index)


except Exception as ex:
    print(ex.args)