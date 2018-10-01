.PHONY: train
train:
	python3 train.py y; python3 train.py n

.PHONY: test1
test1:
	mkdir -p ./tests/out1; python3 main.py -i ./tests/data1/nationality.test -i ./tests/data1/profession.test -o ./tests/out1

.PHONY: clean
clean:
	rm -rf ./tests/out*; 

.PHONY: scoreTest
scoreTest:
	mkdir -p ./tests/profession.test.out; python3 main.py -i ./tests/profession.test/profession.test -o ./tests/profession.test.out

.PHONY: scrapeTest
scrapeTest:
	cd preproc; ./run.sh  ./../specFiles/profession.test.persons ./../specFiles/professions.json; ./run.sh  ./../specFiles/nationality.test.persons ./../specFiles/nationalities.json

.PHONY: evaluateTest
evaluateTest:
	python3 evaluator.py --run ./tests/profession.test.out/profession.test --truth ./tests/profession.test/truth --output ./tests/profession.test.out/evaluation.txt
    
.PHONY: scoreTrain
scoreTrain:
	mkdir -p ./tests/profession.train.out; python3 main.py -i ./tests/profession.train/profession.test -o ./tests/profession.train.out

.PHONY: scrapeTrain
scrapeTrain:
	cd preproc; ./run.sh  ./../specFiles/profession.train.persons ./../specFiles/professions.json;  ./run.sh  ./../specFiles/nationality.train.persons ./../specFiles/nationalities.json


.PHONY: evaluateTrain
evaluateTrain:
	python3 evaluator.py --run ./tests/profession.train.out/profession.test --truth ./tests/profession.train/truth --output ./tests/profession.train.out/evaluation.txt


.PHONY: validateNat
validateNat:
	mkdir -p ./validation/nationality; python3 main.py -i ./specFiles/validate/nationality.test -o ./validation/nationality; python3 evaluator.py --run ./validation/nationality/nationality.test --truth ./specFiles/nationality.train.20 --output ./validation/nationality/evaluation.txt

.PHONY: validateProf
validateProf:
	mkdir -p ./validation/profession; python3 main.py -i ./specFiles/validate/profession.test -o ./validation/profession; python3 evaluator.py --run ./validation/profession/profession.test --truth ./specFiles/profession.train.20 --output ./validation/profession/evaluation.txt
	
.PHONY: testNat
testNat:
	mkdir -p ./finalTest/profession; python3 main.py -i ./specFiles/test/profession.test -o ./finalTest/profession; python3 evaluator.py --run ./finalTest/profession/profession.test --truth ./specFiles/profession.test --output ./finalTest/profession/evaluation.txt


.PHONY: testProf
testProf:
	mkdir -p ./finalTest/nationality ; python3 main.py -i ./specFiles/test/nationality.test -o ./finalTest/nationality; python3 evaluator.py --run ./finalTest/nationality/nationality.test --truth ./specFiles/nationality.test --output ./finalTest/nationality/evaluation.txt

.PHONY: validate
validate:
	echo "Validating profession on 20 pct of profession data"; make validateProf; echo "Validating nationality on 20 pct of data"; make validateNat
    
