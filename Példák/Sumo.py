import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

Ed.RegisterEventHandler(Ed.EVENT_OBSTACLE_AHEAD, 'detectForward')
Ed.RegisterEventHandler(Ed.EVENT_OBSTACLE_LEFT, 'detectLeft')
Ed.RegisterEventHandler(Ed.EVENT_OBSTACLE_RIGHT, 'detectRight')

Ed.LineTrackerLed(Ed.ON)
Ed.ObstacleDetectionBeam(Ed.ON)

while True:
	Ed.Drive(Ed.FORWARD, Ed.SPEED_5, Ed.DISTANCE_UNLIMITED)
	while Ed.ReadLineState()==Ed.LINE_ON_WHITE:
		pass
	Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, 4)
	Ed.Drive(Ed.SPIN_LEFT, Ed.SPIN_LEFT, 180)
	
	
def detectForward():
	Ed.PlayBeep()
	Ed.Drive(Ed.FORWARD, Ed.SPEED_10, Ed.DISTANCE_UNLIMITED)
	
def detectLeft():
	Ed.LeftLed(Ed.ON)
	Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_10, 30)
	Ed.Drive(Ed.FORWARD, Ed.SPEED_5, Ed.DISTANCE_UNLIMITED)
	Ed.LeftLed(Ed.OFF)
	
def detectRight():
	Ed.RightLed(Ed.ON)
	Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_10, 30)
	Ed.Drive(Ed.FORWARD, Ed.SPEED_5, Ed.DISTANCE_UNLIMITED)
	Ed.RightLed(Ed.OFF)