import RPi.GPIO as GPIO
import time
import datetime
from multiprocessing.dummy import Pool as ThreadPool

laneOne = 17
laneTwo = 18

def timeLaps(laneInfo):
    prevInput = 0
    lapCount = 0
    startLapTime = datetime.datetime.now()

    while lapCount < laneInfo['maxLaps']:
        #take a reading
        input = GPIO.input(laneInfo['gpioPin'])

        #if the last reading was low and this one high, print
        if ((not prevInput) and input):
            #increment lap count
            lapCount += 1
            #set the lap end time
            endLapTime = datetime.datetime.now()
            #get lap delta time
            lapDelta = endLapTime - startLapTime
            #print lap info
            print("Car " + laneInfo['laneId'] + " - Lap " + str(lapCount) + " " + str(lapDelta.total_seconds()))
            #reset timer for next lap
            startLapTime = datetime.datetime.now()
            time.sleep(0.05)

        prevInput = input

def startRace(threads=2):
    pool = ThreadPool(threads)

    lanes = [{'gpioPin': laneOne, 'laneId':"1", 'maxLaps':10}, {'gpioPin': laneTwo, 'laneId':"2", 'maxLaps':10}]
    pool.map(timeLaps, lanes)
    pool.close()
    pool.join()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(laneOne,GPIO.IN)
    GPIO.setup(laneTwo,GPIO.IN)

setup()
startRace()