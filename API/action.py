from conDB import Con

c = Con

class Action:
    def getHW():
        data = c.getHW()
        return data
    
    def updateHW(ID, status):
        data = c.updateHW(ID, status)
        return data 
    
    def selectidHW(ID):
        data = c.selectidHW(ID)
        return data
    
    def updateHW(ID, status):
        t = c.updateHW(ID, status)
        if(t== True):
            data = c.selectidHW(ID)
        else :
            data = {"error": True}
        return data 
    
    def insertHW(name, hw_name):
        ID = c.insertHW(name, hw_name)
        if(ID):
            data = c.selectidHW(ID)
        else :
            data = {"error":True}
        return data
    
    def deleteHW(ID):
        data = c.deleteHW(ID)
        return data
 