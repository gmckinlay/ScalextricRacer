
class RaceResults:

    def __init__(self):
        self.results = dict()

    def addResult(self, lane, time):
        if self.results.get(lane) is None:
            self.results.update({lane:list()})
        self.results.get(lane).append(time)

    def fastestLap(self, lane):
        return min(self.results.get(lane))

    def slowestLap(self, lane):
        return max(self.results.get(lane))

    def totalTime(self, lane):
        return sum(self.results.get(lane))

    def averageTime(self, lane):
        laps = self.results.get(lane)
        return sum(laps) / len(laps)

    def printResults(self):
        for lane in self.results:
            laps = self.results.get(lane)
            print("Lane " + lane + ":")
            lapNum = 0
            for lap in laps:
                lapNum += 1
                print("Lap "+ str(lapNum) + "\t" + str(lap) + " seconds")

            print("Fastest Lap\t" + str(self.fastestLap(lane)) + " seconds")
            print("Slowest Lap\t" + str(self.slowestLap(lane)) + " seconds")
            print("Average Lap\t" + str(self.averageTime(lane)) + " seconds")
            print("Total Time\t" + str(self.totalTime(lane)) + " seconds")