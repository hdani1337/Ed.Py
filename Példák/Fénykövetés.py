import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

while True:
	if Ed.ReadLeftLightLevel()>Ed.ReadRightLightLevel():
		Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_4, Ed.DISTANCE_UNLIMITED)
	else:
		Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_4, Ed.DISTANCE_UNLIMITED)