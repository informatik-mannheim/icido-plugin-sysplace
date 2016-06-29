#=======================================================================
# imports
import socket, time
from de.icido.VDPExtension import State;
from de.icido.VDPExtension import SceneObjectController;
from de.icido.VDPExtension import AnimationListController;
from IPConfig import *
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
        print("--- attach ---")#
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((ip,port))
        thread.start_new_thread(self.getData())
            
    def detach(self):
        print("--- detach ---")
        self.sock.close()

    def release(self):
        print("--- release ---")
        self.sock.close()

    def getData(self):
        i=0
        car_is_inside = False
        while i<1:
            data, addr = self.sock.recvfrom(1024)
            data=data.decode()
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
                    self.myCarRein.start()
                    car_is_inside = True

            else:
                if self.lastInsides[0]=="false" and car_is_inside:
                    self.myCarRaus.start()
                    time.sleep(2)
                    self.mybox.setVisibleStatus(0)
                    car_is_inside = False


      
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
    
