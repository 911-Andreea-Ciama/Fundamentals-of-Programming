class Route:
    
    def __init__(self,routeCode,length):
        self.__routeCode = routeCode
        self.__length = length 
        
    def __str__(self):
        return "Code: " + str(self.__routeCode) + "   Length in kms: " + str(self.__length)

    @property
    def getRouteCode(self):
        return self.__routeCode

    @property
    def getLength(self):
        return self.__length
