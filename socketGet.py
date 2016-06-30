#=======================================================================
# imports
import socket, time, thread
from de.icido.VDPExtension import State;
from de.icido.VDPExtension import SceneObjectController;
from de.icido.VDPExtension import AnimationListController;

#=======================================================================
# classes
class Server:
    def __init__(self):
        print("--- init ---")
        self.mybox=SceneObjectController("car")
        self.mybox.setVisibleStatus(0)
        self.myCarRein=AnimationListController()
        self.myCarRein.select("reinfahren")
        self.myCarRaus=AnimationListController()
        self.myCarRaus.select("rausfahren")
        self.lastInsides=["false","false","false"]
#=======================================================================
    def attach(self):
        print("--- attach ---")
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((getIp(),9999))
        thread.start_new_thread(self.getData, ())
            
    def detach(self):
        print("--- detach ---")
        self.sock.close()

    def release(self):
        print("--- release ---")
        self.sock.close()

    def isVisible(self):
        return u'car' in self.mybox.getVisibleNameList()
        
    def getData(self):
        car_is_inside = False

        while True:
            data, addr = self.sock.recvfrom(1024)
            data=data.decode()

            print(data)

            if data[0]=='{' and data[-1]=='}':
                array=data[1:-1].split(",")
                color=array[1].split(":")[1][1:-1]
                inside=array[0].split(":")[1][1:-1]

            self.lastInsides.insert(0,inside)
            self.lastInsides.pop()
            State.activate(State.getStateByName(color))

            if self.lastInsides[0]=="true" and not car_is_inside:
                self.mybox.setVisibleStatus(1)
                if self.lastInsides[1]=="false":
                    while not self.isVisible():
                        continue
                    self.myCarRein.start()
                    car_is_inside = True

            else:
                if self.lastInsides[0]=="false" and car_is_inside:
                    car_is_inside = False
                    self.myCarRaus.start()
                    time.sleep(5)
                    self.mybox.setVisibleStatus(0)

      
#=======================================================================
# __main__
if __name__ == "__main__":
	mServer = Server()
	print("--- Loaded ---")
#=======================================================================

def attach():
    mServer.attach()

def detach():
    mServer.detach()

def release():
    mServer.release()
	
def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("example.com",80))
    return s.getsockname()[0]
    
