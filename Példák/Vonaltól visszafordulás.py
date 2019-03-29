import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

Ed.LineTrackerLed(Ed.ON)

while True:
	Ed.Drive(Ed.FORWARD, Ed.SPEED_5, Ed.DISTANCE_UNLIMITED)
	while Ed.ReadLineState()==Ed.LINE_ON_WHITE:
		pass
	Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, 2)
	Ed.Drive(Ed.SPIN_LEFT, Ed.SPIN_LEFT, 180)