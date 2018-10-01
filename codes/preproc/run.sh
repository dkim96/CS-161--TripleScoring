#! /bin/bash

show_help(){
cat << EOF
Usage:
$0 personsFile jsonSearchArrayFile

personsFile: File containing all persons
jsonSearchArrayFile: Path to either professions.json or nationalities.json,
                     this is the provided lists of every possible person or
                     nationality we will be given
outDirSuffix: Optional. Suffix for features dir. If left out, will not have suffix

Behavior:
Calls scrape.py for each person
for each person, creates:
    ./features/<personName>.<profession|nationality>.json
        <profession|nationalitity> is determiend by jsonSearchArrayFile name
EOF
}

nArgs=2

if [ $# -ne $nArgs ] && [ $# -ne $(($nArgs+1)) ]
then
    show_help
    exit 1
fi

personsFile=$1
jsonSearchArrayFile=$2
suffix=$3
categorySuffix=`basename $jsonSearchArrayFile`
outdir="features${3}"
mkdir -p $outdir

while read person
do
    python3 scrape.py "$person" "$jsonSearchArrayFile" "${outdir}/${person}.${categorySuffix}"
done < <(cat $personsFile | awk -F '\t' '{print $1}')
