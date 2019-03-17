#feature.py

#Abstract Implementation
#from abc import ABC, abstractmethod

from pyspark.sql import SparkSession
import time

class FeatureExtractor():
	"""Class: FeatureExtractor
	
	Description: 
		FeatureExtractor is used to clean and modify raw data and extract required statistics from data.
		The ways of modification are not self-contaiend in the class. Instead, API functions takes custom functions as arugments
		and execute it inside of class. The class also supports dumping out modified data as a form of training data/test data.
		Look at __init__ to see the internal attributes of this class.
	"""

	#Internal
	def __init__(self):
		"""Function: __init__

		Description:
			Initiate FeatureExtractor. 

		Args:
			None

		Attributes:
			spark (SparkSession): Interface between programmer and Apache Spark modules in this class.
			df (Spark DataFrame): Spark Dataframe. Main function of this class is to generate, modify, dump out the dataframe stored in this attribute.
			

		Returns:
			None
		"""
		self.spark = SparkSession.builder.master('local[4]').appName('SparkSQL_Review').getOrCreate()
		self.df = None


	
	#API
	def raw_to_df(self, input_path):
		"""Function: raw_to_df

			Description:
				Takes path to raw data as argument, then create Spark dataframe from it in self.df.
		
			Args:
				input_path (str): Relative or absolute path to raw data. Raw data must be csv-formatted file to be parsed correctly.

			Returns:
				None
				
		"""
		print("Converting raw data into dataframe...")
		self.df = self.spark.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load(input_path)
	
	def df_update(self, custom_function):
		"""Function: df_update
			
			Description:
				Takes custom function as argument, then update self.df as described in custom function. 

			Args:
				custom_function (fun): custom_function should be a function that takes spark(SparkSession), df(Dataframe) as arguments and its contents should 
														 describe the way of updating df using spark, then returns df. Here is the example custom function that follows the policy. 
														 Example)*****************************************************************
														 def WAR2014to2016(spark, df)
															 df.createOrReplaceTempView('pitcher')
															 df = spark.sql('''SELECT Name, playerid, 
																						sum(CASE WHEN Season = "2014" THEN WAR ELSE 0 END) 2014WAR,
																						sum(CASE WHEN Season = "2015" THEN WAR ELSE 0 END) 2015WAR,
																						sum(CASE WHEN Season = "2016" THEN WAR ELSE 0 END) 2016WAR,
																						avg(WAR) as last3WAR, max(Age) as Age
																						FROM pitcher
																						GROUP BY Name, playerid''')
														 return df
														***************************************************************************
			Returns:
				None
				
	
		"""
		self.df = custom_function(self.spark, self.df)

	def dump_df(self, output_path, split=False, split_function=None):
		"""
		Warning: This function is not fully implemented yet!
		"""
		"""Function: dump_df

			Description: 
				Dump out self.df as csv-formatted file.

			Args:
				output_path (str): Relative or absolute path of output.
				split (bool): Should be True if output is required to be splitted into test, training data. Default is False
			  split_function (fun): a function describing how test, training data should be splitted. 	
	
		"""
		train_df, test_df = self.df.randomSplit([0.9, 0.1], seed = 42)
		
		train_df.toPandas().to_csv("train_input/input.csv", header=True)
		test_df.toPandas().to_csv("test_input/input.csv", header=True)
		#train_df.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").csv(dirname_train + "/input")
		#test_df.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").csv(dirname_test + "/input")
		print("Dumped processed train data in " + dirname_train)
		print("Dumped processed test data in " + dirname_test)

#class: OutputType
class OutputType():
	def __init__(self, player_name, expected_WAR):
		self.player_name = player_name
		self.expected_WAR = expected_WAR



##################
#Custom Functions#
##################
def WAR2014to2016(spark, df):
	df.createOrReplaceTempView('pitcher')
	df = spark.sql('''SELECT Name, playerid, 
										sum(CASE WHEN Season = "2014" THEN WAR ELSE 0 END) 2014WAR,
										sum(CASE WHEN Season = "2015" THEN WAR ELSE 0 END) 2015WAR,
										sum(CASE WHEN Season = "2016" THEN WAR ELSE 0 END) 2016WAR,
										avg(WAR) as last3WAR, max(Age) as Age
										FROM pitcher
										GROUP BY Name, playerid''')
	return df

def join_with_2017(spark, df):
	df_2017 = spark.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load("FanGraphs_Leaderboard_2017_Pitcher_Leader.csv")
	df_2017.createOrReplaceTempView('2017pitcher')
	df.createOrReplaceTempView('pitcher')
	df = spark.sql('''SELECT pitcher.2014WAR as 2014WAR, pitcher.2015WAR as 2015WAR, pitcher.2016WAR as 2016WAR,
													 pitcher.Age as Age, 2017pitcher.WAR as 2017WAR
										FROM pitcher, 2017pitcher
										WHERE pitcher.playerid = 2017pitcher.playerid
										''')

	#from pyspark.ml.feature import VectorAssembler
	#all_features = ["2014WAR", "2015WAR", "2016WAR"]
	#assembler = VectorAssembler( inputCols = all_features, outputCol = "features")
	df = df.select("Age", "2014WAR", "2015WAR", "2016WAR", "2017WAR")
	return df


