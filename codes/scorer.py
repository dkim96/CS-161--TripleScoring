from keras.models import load_model
from train import get_index_of_role, get_array_for_person

import numpy as np
import random

"""
arr: an array of length 8
returns: index of maximum element in arr.

Special cases:
all same val: then returns random num in [1-5]
max element is present more than once: randomly select from the maximum indexes
"""
def one_hot_to_integer(arr):
    if len(set(arr)) == 1:
        # every element same. Return random value in [1-5]
        return random.randint(1, 6)

    max_element = max(arr)

    # Accumulate indexes of maximum element
    max_indexes = []
    for i in range(8):
        if arr[i] == max_element:
            max_indexes.append(i)
    
    return random.choice(max_indexes)


def score(name, roles, is_nationality):
	model = load_model(('nationalities' if is_nationality else 'professions') + '.model.h5')
	test_values = get_array_for_person(name, is_nationality)
	input = []
	for role in roles:
		one_hot_roles = np.zeros(len(test_values))
		one_hot_roles[get_index_of_role(role, is_nationality)] = 1
		input.append([test_values, one_hot_roles])
	predictions = model.predict(np.asarray(input))

	return [one_hot_to_integer(prediction) for prediction in predictions]
	# return [int(min(7, max(0, round(prediction[0])))) for prediction in predictions]
	# return [5 for role in roles]

if __name__ == "__main__":
	results = score('Barack Obama', ['Politician', 'Lawyer', 'Law professor', 'Tentmaker'], False)
	for result in results:
		print(result)
