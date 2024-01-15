
class PositionFile:
    def load(self):
        try:
            with open("filePositon.txt",'a+') as file:
                item =  file.read()
                if(item is None or item==""):
                    return 2
                return int(item)
        except TypeError as err:
            return 2
        
    def write(self,position):
        with open("filePositon.txt",'w+') as file:
            file.write(position)