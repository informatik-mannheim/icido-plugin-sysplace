from socketGet import *
from de.icido.VDPExtension import FakeSocket, Packet, setVerbose, reset

# set to True for debugging and to False for minimal output
setVerbose(False)

def testShouldDoNothingIfOnlyOutside():
	print("### testShouldDoNothingIfOnlyOutside ###")

	# needed to reset globals for the static State stuff
	reset()
	
	server = Server()
	
	fakeSocket = FakeSocket()

	fakeSocket.enqueue(Packet("green", False))
	fakeSocket.enqueue(Packet("green", False))
	fakeSocket.enqueue(Packet("green", False))
	fakeSocket.enqueue(Packet("green", False))
	fakeSocket.enqueue(Packet("green", False))
	fakeSocket.enqueue(Packet("green", False))
	
	server.sock = fakeSocket
	
	try:
		server.getData()
	except:
		print("--- Server killed ---")
		
	assert server.mybox.lastVisibleStatus ==  0, "expected last visible status to be 0"
	assert server.mybox.statusChanges == 1, "expected only 1 status change"
	assert server.myCarRein.starts == 0, "expected no start animation to take place"
	assert server.myCarRaus.starts == 0, "expected no start animation to take place"
	assert State.getStateChanges() == 6, "expected 6 state changes"
	assert State.getLastActiveState() == "green", "expected last active color to be green"
	
	print("Success")
	
def testShouldActivateCarOnEntryOnce():
	print("### testShouldActivateCarOnEntryOnce ###")

	# needed to reset globals for the static State stuff
	reset()
	
	server = Server()
	
	fakeSocket = FakeSocket()

	fakeSocket.enqueue(Packet("green", False))
	fakeSocket.enqueue(Packet("green", True))
	fakeSocket.enqueue(Packet("green", True))
	fakeSocket.enqueue(Packet("green", True))
	fakeSocket.enqueue(Packet("green", True))
	fakeSocket.enqueue(Packet("green", True))
	
	server.sock = fakeSocket
	
	try:
		server.getData()
	except:
		print("--- Server killed ---")
		
	assert server.mybox.lastVisibleStatus ==  1, "expected last visible status to be 1"
	assert server.mybox.statusChanges == 2, "expected 2 status changes"
	assert State.getStateChanges() == 6, "expected 6 state changes"
	assert State.getLastActiveState() == "green", "expected to be green"
	
	print("Success")
	
def testShouldDeactivateVisibleCarAfterTwoLeavingPackets():
	print("### testShouldDeactivateVisibleCarAfterTwoLeavingPackets ###")

	# needed to reset globals for the static State stuff
	reset()
	
	server = Server()
	
	fakeSocket = FakeSocket()

	fakeSocket.enqueue(Packet("green", True))
	fakeSocket.enqueue(Packet("green", False))
	fakeSocket.enqueue(Packet("green", False))
	
	server.sock = fakeSocket
	
	try:
		server.getData()
	except:
		print("--- Server killed ---")
		
	assert server.mybox.lastVisibleStatus == 0, "expected last visible status to be 0"
	assert server.mybox.statusChanges == 3, "expected 3 status changes"
	assert server.myCarRein.starts == 1, "expected one rein animation to take place"
	assert server.myCarRaus.starts == 1, "expected one raus animation to take place"
	assert State.getStateChanges() == 3, "expected 3 state changes"
	assert State.getLastActiveState() == "green", "expected last active color to be green"
	
	print("Success")

def testShouldChangeColorWhenCarIsVisible():
	print("### testShouldChangeColorWhenCarIsVisible ###")

	# needed to reset globals for the static State stuff
	reset()
	
	server = Server()
	
	fakeSocket = FakeSocket()

	fakeSocket.enqueue(Packet("green", True))
	fakeSocket.enqueue(Packet("blue", True))
	
	
	server.sock = fakeSocket
	
	try:
		server.getData()
	except:
		print("--- Server killed ---")
		
	assert server.mybox.lastVisibleStatus == 1, "expected last visible status to be 0"
	assert server.mybox.statusChanges == 2, "expected 1 visible status changes"
	assert server.myCarRein.starts == 1, "expected one rein animation to take place"
	assert server.myCarRaus.starts == 0, "expected no raus animation to take place"
	assert State.getStateChanges() == 2, "expected 2 state changes"
	assert State.getLastActiveState() == "blue", "expected last active color to be blue"
	
	print("Success")

	
if __name__ == "__main__":
	testShouldDoNothingIfOnlyOutside()
	testShouldActivateCarOnEntryOnce()
	testShouldDeactivateVisibleCarAfterTwoLeavingPackets()
	testShouldChangeColorWhenCarIsVisible()