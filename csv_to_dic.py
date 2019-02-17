import urllib.request as urllib


url = 'data.csv'

def createDict():
        statistics = {}
        with open(url) as f:
                lines = f.readlines()
                
                for i in range(1, len(lines)):
                        #Handle data and make it into arrays
                        line = lines[i]
                        values = list(map(int, line.split(",")))
                        currDict = statistics

                        for y in range(3):
                                #Set current value
                                currVal = values[y]

                                #If it exist in the structure:
                                if currVal in statistics.keys():
                                        #Go to next level of dictionary
                                        currDict = currDict.get(currVal)

                                #If it doesn't
                                else:
                                        #Add value as dict
                                        currDict[currVal] = {}
                                        currDict = currDict[currVal]
                        #Set last k/v pair
                        currDict[values[3]] = values[4]


createDict()
