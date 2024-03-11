
class Treasure:
    def __init__(self, value:int, level:str) -> None:
        self.__value = value
        self.__level = level
    #end constructor

    def getValue(self):
        return self.__value
    #end function
    
    def getLevel(self):
        return self.__level
    #end function
    def setValue(self, newVal:int) :
        self.__value = newVal
    #end procedure
        
    def setLevel(self, newLevel:str) :
        self.__level = newLevel
    #end procedure
#end class
        
gold_cup = Treasure(500,"Gold")

gold_cup.__value = 300
print(gold_cup._Treasure__value,gold_cup._Treasure__level)
print(gold_cup.getValue(),gold_cup.getLevel())