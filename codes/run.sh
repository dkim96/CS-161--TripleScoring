#! /bin/bash

# This is a shell script to do the following:
# Check that you have followed instructions in data/README.txt, to download data from google drive, and unzip
# Train model for nationality, and train model for profession on ~80% of train data
# Run validation for nationality and validation for profession on ~20% of train data
# Run test for nationality and validation, and print results

echo "===========Training=========="
make train
echo "==============================================="
echo "Training done"
echo "==============================================="

echo "===========Running validation=========="
make validate
echo "==============================================="
echo "Validation done. Results have been printed out. To review results, see ./validation/profession/evaluation.txt and ./validation/nationality/evaluation.txt"
echo "==============================================="


echo "===========Running tests on public test data released after competition completion=========="
echo "Testing nationality"
make testNat
echo "==============================================="
echo "Nationality test done. Results have been printed. To review results, see ./finalTest/nationality/evaluation.txt"
echo "==============================================="


echo "Testing profession"
make testProf

echo "==============================================="
echo "Profession test done. Results have been printed. To review results, see ./finalTest/profession/evaluation.txt"
echo "==============================================="
