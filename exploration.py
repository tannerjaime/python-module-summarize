import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from numpy import genfromtxt

test_np = genfromtxt('C:/Users/andy/Documents/GitHub/python-module-summarize/sample.csv', delimiter=',')


test_pd = pd.read_csv('C:/Users/andy/Documents/GitHub/python-module-summarize/sample.csv')


type(test_np)

type(test_pd)

""" A module to summarize and visualize a numpy ndarray or a pandas dataframe or series """

def check_input_data(data):
	""" check that input data is a pandas dataframe or series or a numpy ndarray """
	""" convert input to pandas dataframe (if not one already) """
	""" return error if input is not any of these data structures """
	structure = type(data)
	if structure == type('DataFrame'):
		datatype = ('Dataset is a Pandas DataFrame.')
	else:
		datatype = ("Dataset is not a Pandas DataFrame.")
	return datatype

check_data_type('test')

def check_data_type(): #ANDREW
	""" simple function to check data type """

class Explore():
	""" summarize and visualize data """

	def __init__(self, data):
		self.data = data

	def summarize():
		""" method to summarize and visualize self.data """