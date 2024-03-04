
class Treasure:
    def __init__(self, value:int, level:str) -> None:
        self.value = value
        self.level = level
    #end constructor

    def getValue(self):
        return self.value
    #end function
    
    def getLevel(self):
        return self.level
    #end function
    def setValue(self, newVal:int) :
        self.value = newVal
    #end procedure
        
    def setLevel(self, newLevel:str) :
        self.value = newLevel
    #end procedure
#end class
        
gold_cup = Treasure(500,"Gold")
print(gold_cup.value)