#models.py

#Abstract Implementation
from abc import ABC, abstractmethod

import torch.nn as nn
import xgboost as xgb



#class: CNN
class CNN(nn.Module):
	#Internal		
	def __init__(self, parameters):
		super(CNN, self).__init__()
		self.init_model_(parameters)
		self.linear1 = nn.Linear(4, 8)
		self.linear2 = nn.Linear(8, 1)
		self.activ = nn.Sigmoid()

	def init_model_(self, parameters):
		print("CNN model initiated")

	def forward(self, x):
		#print("forwarding CNN model...")
		return self.linear2(self.activ(self.linear1(x)))


#class: LSTM
#abstract class
class LSTM(ABC):
	#Internal
	def __init__(self, parameters):
		super.__init__()
		init_model_(parameters)

	def init_model_(parameters):
		print("LSTM model initiated")

	#API
	@abstractmethod
	def forward():
		print("forwarding LSTM model...")

#class: XGBoost
#abstract class
#Note: train, test API should work without knowing schema of input data as long as both have same format and label at last column.
class XGBoost(ABC):
	#Internal
	#self.output contatins the result line by line
	def __init__(self, parameters):
		super.__init__()
		self.model = None
		self.output = []
		init_model_(parameters)
	
	def init_model_(parameters):
		print("XGBoost model initiated")
	
	#API
	@abstractmethod
	def train(train_parameters, path_train_input):
		print("XGBoost training starts")

	
	@abstractmethod
	def test(test_parameters, path_test_input):
		print("XGBoost testing starts")
	
	def dump_output(dirname_output):
		f = open(dirname_output + "/output.txt", "w")
		for line in self.result:
			f.write(line + '\n')
		f.close()

		print("XGBoost dumped testing reuslt in " + dirname_output + "/output.txt")


"""
class CNNDemo(CNN):
	def forward(self, x):
		avg = 0;
		for val in x:
			avg += val
		return avg/len(x)
"""


