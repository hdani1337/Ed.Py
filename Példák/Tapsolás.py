import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

while True:
	waitClap()
	Ed.RightLed(Ed.ON)
	Ed.TimeWait(100, Ed.TIME_MILLISECONDS)
	Ed.ReadClapSensor()
	Ed.TimeWait(250, Ed.TIME_MILLISECONDS)
	if Ed.ReadClapSensor() == Ed.CLAP_DETECTED:
		Ed.LeftLed(Ed.ON)
		Ed.Drive(Ed.FORWARD, Ed.SPEED_10, 15)
	else:
		Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_10, 90)
	Ed.TimeWait(250, Ed.TIME_MILLISECONDS)
	Ed.RightLed(Ed.OFF)
	Ed.LeftLed(Ed.OFF)
	Ed.ReadClapSensor()

def waitClap():
	while Ed.ReadClapSensor() != Ed.CLAP_DETECTED:
		pass