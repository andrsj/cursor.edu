# itertools
	from itertools import product, permutations

	letters = ("A", "B")
	print(list(product(letters, range(2))))
	print(list(permutations(letters))) 

	OUT:
	[('A', 0), ('A', 1), ('B', 0), ('B', 1)]
	[('A', 'B'), ('B', 'A')]

	# The function count counts up infinitely from a value.
	# The function cycle infinitely iterates through an iterable (for instance a list or string).
	# The function repeat repeats an object, either infinitely or a specific number of times.
	# takewhile - takes items from an iterable while a predicate function remains true;
	# chain - combines several iterables into one long one;
	# accumulate - returns a running total of values in an iterable. 