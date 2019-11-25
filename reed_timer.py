import RPi.GPIO as GPIO
import time
import datetime
from lane_info import LaneInfo
from multiprocessing.dummy import Pool as ThreadPool

laneOne = 17
laneTwo = 18
maxLaps = 10

def timeLaps(laneInfo):
    # type: (LaneInfo) -> None
    """Times the laps for a given lane"""
    prevInput = 0
    lapCount = 0
    startLapTime = datetime.datetime.now()

    while lapCount < maxLaps:
        #take a reading
        input = GPIO.input(laneInfo.gpioPin)
        
        #if the last reading was low and this one high, print
        if ((not prevInput) and input):
            #increment lap count
            lapCount += 1
            #set the lap end time
            endLapTime = datetime.datetime.now()
            #get lap delta time
            lapDelta = endLapTime - startLapTime
            processLap(laneInfo.laneId, lapCount, lapDelta)
            #reset timer for next lap
            startLapTime = datetime.datetime.now()
            #wait a short period to avoid double counting a lap..
            time.sleep(0.05)

        prevInput = input

def processLap(laneId, lap, lapDelta):
    # type: (str, int, datetime) -> None
    """Times the laps for a given lane"""
    #print lap info
    print("Car " + laneId + " - Lap " + str(lap) + " " + str(lapDelta.total_seconds()))

def startRace(threads=2):
    pool = ThreadPool(threads)

    # lanes = [{'gpioPin': laneOne, 'laneId':"1"}, {'gpioPin': laneTwo, 'laneId':"2"}]
    lanes = [LaneInfo(laneOne, "1"), LaneInfo(laneTwo, "2")]
    
    pool.map(timeLaps, lanes)
    pool.close()
    pool.join()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(laneOne,GPIO.IN)
    GPIO.setup(laneTwo,GPIO.IN)

setup()
startRace()