from socketGet import *
from de.icido.VDPExtension import FakeSocket, Packet

if __name__ == "__main__":
	server = Server()

	fakeSocket = FakeSocket()
	
	fakeSocket.enqueue(Packet("blue", False))
	fakeSocket.enqueue(Packet("blue", False))
	fakeSocket.enqueue(Packet("green", False))
	fakeSocket.enqueue(Packet("green", True))
	fakeSocket.enqueue(Packet("green", True))
	fakeSocket.enqueue(Packet("blue", True))
	fakeSocket.enqueue(Packet("blue", True))
	fakeSocket.enqueue(Packet("blue", False))
	fakeSocket.enqueue(Packet("blue", False))
	fakeSocket.enqueue(Packet("blue", False))
	fakeSocket.enqueue(Packet("green", False))
	fakeSocket.enqueue(Packet("green", True))
	fakeSocket.enqueue(Packet("green", False))
	
	server.sock = fakeSocket
	
	try:
		server.getData()
	except:
		print("--- Server killed ---")