from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation, Dropout
from keras.layers.advanced_activations import LeakyReLU
import numpy as np
import random
import json
import sys

def get_array_for_person(name, is_nationality):
	# TODO: Escape spaces and periods and stuff in the name?
	filename = "preproc/features/" + name + (".nationalities" if is_nationality else ".professions") + ".json"
	try:
		with open(filename) as f:
			return np.asarray(json.load(f))
	except:
		print("person %s not found - using zeros" % (name))
		return np.zeros(100 if is_nationality else 200)

def get_index_of_role(role, is_nationality):
	filename = "specFiles/nationalities" if is_nationality else "specFiles/professions"
	with open(filename) as f:
		for (line_number, line) in enumerate(f):
			if role in line:
				return line_number

def get_role_score(person, is_nationality):
	filename = "specFiles/nationality.train" if is_nationality else "specFiles/profession.train"
	scores = []
	roles = []
	with open(filename) as f:
		for line in f:
			(name, role, score) = line.split('\t')
			if name == person:
				scores.append(int(score.strip()))
				roles.append(role)
	return ([get_index_of_role(aRole, is_nationality) for aRole in roles], scores)

"""
n: an integer
returns: array of length 8, where array[n] is 1, all else 0
"""
def to_one_hot_array(n):
	ans = [0 for i in range(8)]
	ans[n] = 1
	return ans

	

def build_model(is_nationality):
	dimen = 100 if is_nationality else 200
	
	# model = Sequential([Dense(32, input_shape=(2,dimen)), Flatten(), Activation('sigmoid'), Dense(8)])
		
	model = Sequential()
	model.add(Dense(100, input_shape=(2, dimen), activation='relu'))
	model.add(Flatten())
	model.add(Dropout(rate=0.5))
	model.add(Dense(85, activation='relu'))
	model.add(Dense(64, activation='relu'))
	model.add(Dense(32, activation='tanh'))
	model.add(Dense(16, activation='relu'))
	model.add(Dense(8))
	
	
	# model.add(Dense(32, input_shape=(2,6)))
	# model.add(Dense(8, activation='relu'))
	# model.add(Dense(1, activation='sigmoid'))
	model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['accuracy'])
	return model

def main(is_nationality):
	persons_file = ""
	if is_nationality:
		persons_file = "specFiles/nationality.train.80"
	else:
		persons_file = "specFiles/profession.train.80"
	input_data = []
	output_data = []
	with open(persons_file) as pf:
		for line in pf:
			person = line.split('\t')[0].strip()
			values = get_array_for_person(person, is_nationality)
			values_len = len(values)
			(roles, scores) = get_role_score(person, is_nationality)
			for (role, score) in zip(roles, scores):
				temp = np.zeros(values_len)
				temp[role] = 1
				input_data.append([values, temp])
				output_data.append(to_one_hot_array(score))


	# filename = 'tests/data1/nationality.train'
	# wiki_data_filename = '/Users/vanshgandhi/Downloads/triple-scoring/small-wiki'
	# input_data = np.genfromtxt(filename, delimiter='\t', dtype=str, usecols=(0,1))
	# output_data = np.genfromtxt(filename, delimiter='\t', dtype=int, usecols=2)
	# with open(wiki_data_filename) as f:
	# 	wiki_data = f.read()
	# input_data_with_wiki = np.empty(shape=[1, len(input_data)])
	# for input in input_data:
	# 	np.append(input_data_with_wiki, np.append(input, wiki_data))

	model = build_model(is_nationality)

	#print(str(input_data))
	#print(str(output_data))

	input_data = np.asarray(input_data)
	output_data = np.asarray(output_data)

	#print(input_data.shape)
	#print(output_data.shape)

	model.fit(input_data, output_data, epochs=200)
	model.save(('nationalities' if is_nationality else 'professions') + '.model.h5')

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Require one argument: is_nationalty y/n")
		sys.exit(1)
	
	arg_is_nat = sys.argv[1].lower() in ["y", "yes", "true", "t"]
	
	main(arg_is_nat)
