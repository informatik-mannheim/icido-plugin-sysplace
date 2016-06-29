lastActivatedState = ""
stateChanges = 0
verbose = True

def reset():
	global stateChanges
	global lastActivatedState
	stateChanges = 0
	lastActivatedState = ""

def setVerbose(flag):
	global verbose
	verbose = flag

def log(string):
	if verbose:
		print(string)

class State:
	@staticmethod
	def activate(state):	
		global stateChanges
		global lastActivatedState
		log("[State] activating " + state)
		lastActivatedState = state
		stateChanges += 1
		
	@staticmethod
	def getStateByName(name):
		return name
		
	@staticmethod
	def getStateChanges():
		global stateChanges
		return stateChanges
	
	@staticmethod
	def getLastActiveState():
		global lastActivatedState
		return lastActivatedState
		
class SceneObjectController:
	def __init__(self, name):
		self.lastVisibleStatus = -1
		self.statusChanges = 0
		
	def setVisibleStatus(self, status):
		log("[SceneObjectController] setVisibleStatus " + str(status))
		self.lastVisibleStatus = status	
		self.statusChanges += 1
		
class AnimationListController:
	def __init__(self):
		self.lastSelection = ""
		self.starts = 0
		
	def select(self, selection):
		log("[AnimationListController] select " + selection)
		self.lastSelection = selection
		
	def start(self):
		log("[AnimationListController] start animation '" + self.lastSelection + "'")
		self.starts += 1
		
class FakeSocket:
	def __init__(self):
		self.packets = []
		
	"""pop a packet from the queue"""
	def recvfrom(self, count):
		packet = str(self.packets.pop())
		log("[Socket] received " + packet)
		return packet, 1024
	
	""""enqueue in chronological order - to be replayed exactly as was queued"""
	def enqueue(self, packet):
		self.packets.insert(0, packet)
		
"""wraps color and inside flag and override str() method for easy use"""
class Packet:
	def __init__(self, color, inside):
		self.color = color
		self.inside = inside
		
	def __str__(self):
		return "{'inside':'" + str(self.inside).lower() + "','color':'" + self.color + "'}"
		