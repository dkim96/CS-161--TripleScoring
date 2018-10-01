#! /bin/bash

# Batch scraper. Call with argument of { 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 }
# Will scrape from [arg-99, arg]th files of PERSON_SPLITDIR, for both nationality and profession
# Then will save files to preproc/features<arg>
# Sample command: ./batchScrapeAll.sh 300 2>&1 | tee scrape300.log

if [[ $PWD != *preproc ]]
then
    echo "Must run from preproc dir"
    exit 1
fi

if [ $# -ne 1 ]
then
    echo "one arg required: batch number"
    exit 1
fi

PERSON_SPLITDIR="./../specFiles/personsSplit/"
#PERSON_SPLITDIR="./test/"

endNum=$1
startNum=$(($endNum-99))
#startNum=$(($endNum-4))

for i in `seq $startNum $endNum`
do
    personFile=`ls $PERSON_SPLITDIR | sed -n ${i}p`
    if [ -z $personFile ]
    then
        echo "Skipping batch $endNum, number $i beacuse not found"
    else
        ./run.sh "${PERSON_SPLITDIR}/${personFile}" ./../specFiles/professions.json $endNum
        ./run.sh "${PERSON_SPLITDIR}/${personFile}" ./../specFiles/nationalities.json $endNum
    fi

done


