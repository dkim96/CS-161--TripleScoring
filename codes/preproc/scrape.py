import urllib.request
import json
import sys
from mine_features import calculateScore

usage = """
Usage:
$0 personName jsonArrayFile outputFilename

personName: A string containing name of person
jsonArrayFile: Path to either professions.json or nationalities.json,
                     this is the provided lists of every possible person or
                     nationality we will be given
outputFilename: Path to output file


Behavior:
Scrapes data from wiki, fills outputFilename with array that is same length
as array contained in jsonArrayFile; it will be array of integers
representing how many times that word appeared in the scraped wiki data.
"""

personName = None
jsonArrayFile = None
outputFilename = None
wikiURL = None
wikiDataString = None
is_nationality = None

# WIKI_URL_PREFIX + <personName> takes you to the respective Wiki page
WIKI_URL_PREFIX = "http://en.wikipedia.org/wiki/"

nArgs = 3

def parseArgs():
    if len(sys.argv) - 1 != nArgs:
        print(usage)
        sys.exit(1)


    global personName
    global jsonArrayFile
    global outputFilename
    global wikiURL
    global is_nationality

    personName = sys.argv[1]
    jsonArrayFile = sys.argv[2]
    outputFilename = sys.argv[3]

    is_nationality = "nation" in jsonArrayFile

    wikiURL = "%s%s" % (WIKI_URL_PREFIX, urllib.parse.quote(personName))

def scrapeData():
    print("Mining %s" % (personName))
    features = []
    try:
        response = urllib.request.urlopen(wikiURL)
        data = response.read()
        wikiDataString = data.decode('utf-8')

        searchArr = json.load(open(jsonArrayFile))

        for s in searchArr:
            features.append(calculateScore(wikiDataString, s))
    except:
        numZeros = 100 if is_nationality else 200
        print("ERROR MINING %s. Putting %d 0s into features to indicate this error." % (personName, numZeros))

        for i in range(numZeros):
            features.append(0)

    with open(outputFilename, 'w+') as ofhandle:
        json.dump(features, ofhandle)


if __name__ == "__main__":
    parseArgs()
    scrapeData()

