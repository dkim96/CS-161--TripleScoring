CS 145 Project - WSDM Cup 2017 TripleScoring Task

Please first follow the instructions in data/README.txt
to download the data.

Your system must have the following requirements:
- Must be able to run the bash shell: /bin/bash
- Sufficient space to hold the unzipped data
	Space used depends on your architecture's block size
	On our machines, the unzipped files take ~3G
- python3 must be installed and must be added to your $PATH
- make must be installed and must be added to your $PATH
- Must have permissions to install new python modules using pip

Instructions for reproducing our results:
- Install the required python modules found in codes/requirements.txt
	- The following command assumes pip points to the python3 pip.
	- cd codes; pip install -r requirements.txt
- Execute the run.sh script to execute all our codes as a chain. Note that run.sh
  simply executes a sequence of makefile targets that can be found in codes/Makefile.
	- cd codes; ./run.sh
	- run.sh will report what it is doing. Look for ===== dashes for the logging.
	- Here is a description of what run.sh does:
		- Trains a model on 80% of the profession.train data, and saves it into professions.model.h5
		- Trains a model on 80% of the nationality.train data and saves it into nationalities.model.h5
		- Runs validation on professions model, using the other 20% of the profession.train data
			- validation results are saved into codes/validation/profession/evaluation.txt
		- Runs validation on nationality model, using the other 20% of the nationality.train data
			- validation results are saved into codes/validation/nationality/evaluation.txt
		- Tests both models on the profession.test and nationality.test data
			- Test results are saved into the following files:
				- codes/finalTest/nationality/evaluation.txt
				- codes/finalTest/profession/evaluation.txt

