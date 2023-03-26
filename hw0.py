"""
Introductory programming assignment.
"""
import pandas as pd

"""
!!!TODO!!!
"""
def read_file(filename):
	'''Input: filename (location of stock.dat)
	   Output: a list of tuples (ticker, name)
	'''
	file = open(filename, "r")
	lines = file.readlines()
	tuple_list = []
	for line in lines:
		pairs = line.split(" - ")
		pairs[1] = pairs[1].strip('\n')
		tup = (pairs[0], pairs[1])
		tuple_list.append(tup)
	return tuple_list


"""
!!!TODO!!!
"""
def write_csv(parsed, outfile):
	'''Input: a list of tuples (ticker,name), output location
	   Output: None/Void, writes a file
	'''
	df = pd.DataFrame(parsed, columns=['ticker','name'])
	df.set_index('ticker', inplace=True)
	df.to_csv(outfile, header=True)
	return None
