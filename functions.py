#functions.py
"""
A collection of custom functions and split functions for FeatrueExtractor class
"""
import env
from pyspark.sql.functions import col,min,max

##################
#Custom Functions#
##################
def selection(spark, df, col=None):
    '''Custom Function: selection

        Description: 
            select columns given by col argument. Default is all columsn of data frame

        Args: 
            col (string list): list of columns that you want to select.

        Return:
    '''


    if col==None:
        columns = df.columns
    else:
        columns = col
    df = df.select(columns)
    return df

def join(spark, df, name, on, how="inner"): 
    new_df = spark.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema",
    "true").load(name)
    new_df = new_df.withColumnRenamed(on, "new" + on)
    df = df.join(new_df, col(on) == col("new" + on), how)
    return df
    



def WAR2014to2016(spark, df):
    '''Custom Function: WAR2014to2016

        Description: 
            Enumerate 2014, 2015, 2016 WAR of one player.

        Args: 

        Return:

        Note: 
            WAR enumeration do similar works for you.
    '''


    df.createOrReplaceTempView('pitcher')
    df = spark.sql('''SELECT Name, playerid, 
                                        sum(CASE WHEN Season = "2014" THEN WAR ELSE 0 END) 2014WAR,
                                        sum(CASE WHEN Season = "2015" THEN WAR ELSE 0 END) 2015WAR,
                                        sum(CASE WHEN Season = "2016" THEN WAR ELSE 0 END) 2016WAR,
                                        avg(WAR) as last3WAR, max(Age) as Age
                                        FROM pitcher
                                        GROUP BY Name, playerid''')
    return df

def WAR_enumeration_by_service_time(spark, df):
    '''Custom Function: WAR_enumeration_by_service_time

        Description: 
            Enumerate WAR of first service time to 15th service time.

        Args: 

        Return:
        
        Note:
            Hard coded now. Need to be modified,
    '''


    df.createOrReplaceTempView('pitcher')
    df = spark.sql('''SELECT Name, playerid, 
                                        sum(CASE WHEN ServiceTime = "1" THEN WAR ELSE NULL END) WAR1,
                                        sum(CASE WHEN ServiceTime = "2" THEN WAR ELSE NULL END) WAR2,
                                        sum(CASE WHEN ServiceTime = "3" THEN WAR ELSE NULL END) WAR3,
                                        sum(CASE WHEN ServiceTime = "4" THEN WAR ELSE NULL END) WAR4,
                                        sum(CASE WHEN ServiceTime = "5" THEN WAR ELSE NULL END) WAR5,
                                        sum(CASE WHEN ServiceTime = "6" THEN WAR ELSE NULL END) WAR6,
                                        sum(CASE WHEN ServiceTime = "7" THEN WAR ELSE NULL END) WAR7,
                                        sum(CASE WHEN ServiceTime = "8" THEN WAR ELSE NULL END) WAR8,
                                        sum(CASE WHEN ServiceTime = "9" THEN WAR ELSE NULL END) WAR9,
                                        sum(CASE WHEN ServiceTime = "10" THEN WAR ELSE NULL END) WAR10,
                                        sum(CASE WHEN ServiceTime = "11" THEN WAR ELSE NULL END) WAR11,
                                        sum(CASE WHEN ServiceTime = "12" THEN WAR ELSE NULL END) WAR12,
                                        sum(CASE WHEN ServiceTime = "13" THEN WAR ELSE NULL END) WAR13,
                                        sum(CASE WHEN ServiceTime = "14" THEN WAR ELSE NULL END) WAR14,
                                        sum(CASE WHEN ServiceTime = "15" THEN WAR ELSE NULL END) WAR15
                                        FROM pitcher
                                        GROUP BY Name, playerid''')
    return df

def WAR_enumeration_by_age(spark, df):
    '''Custom Function: WAR_enumeration_by_service_time

        Description: 
            Enumerate WAR of first service time to 15th service time.

        Args: 

        Return:
        
        Note:
            Hard coded now. Need to be modified,
    '''


    df.createOrReplaceTempView('pitcher')
    df = spark.sql('''SELECT Name, playerid, 
                                        sum(CASE WHEN Age = "16" THEN WAR ELSE NULL END) WAR16, 
                                        sum(CASE WHEN Age = "17" THEN WAR ELSE NULL END) WAR17,
                                        sum(CASE WHEN Age = "18" THEN WAR ELSE NULL END) WAR18,
                                        sum(CASE WHEN Age = "19" THEN WAR ELSE NULL END) WAR19,
                                        sum(CASE WHEN Age = "20" THEN WAR ELSE NULL END) WAR20,
                                        sum(CASE WHEN Age = "21" THEN WAR ELSE NULL END) WAR21,
                                        sum(CASE WHEN Age = "22" THEN WAR ELSE NULL END) WAR22,
                                        sum(CASE WHEN Age = "23" THEN WAR ELSE NULL END) WAR23,
                                        sum(CASE WHEN Age = "24" THEN WAR ELSE NULL END) WAR24,
                                        sum(CASE WHEN Age = "25" THEN WAR ELSE NULL END) WAR25,
                                        sum(CASE WHEN Age = "26" THEN WAR ELSE NULL END) WAR26,
                                        sum(CASE WHEN Age = "27" THEN WAR ELSE NULL END) WAR27,
                                        sum(CASE WHEN Age = "28" THEN WAR ELSE NULL END) WAR28,
                                        sum(CASE WHEN Age = "29" THEN WAR ELSE NULL END) WAR29,
                                        sum(CASE WHEN Age = "30" THEN WAR ELSE NULL END) WAR30,
                                        sum(CASE WHEN Age = "31" THEN WAR ELSE NULL END) WAR31,
                                        sum(CASE WHEN Age = "32" THEN WAR ELSE NULL END) WAR32,
                                        sum(CASE WHEN Age = "33" THEN WAR ELSE NULL END) WAR33,
                                        sum(CASE WHEN Age = "34" THEN WAR ELSE NULL END) WAR34,
                                        sum(CASE WHEN Age = "35" THEN WAR ELSE NULL END) WAR35,
                                        sum(CASE WHEN Age = "36" THEN WAR ELSE NULL END) WAR36,
                                        sum(CASE WHEN Age = "37" THEN WAR ELSE NULL END) WAR37,
                                        sum(CASE WHEN Age = "38" THEN WAR ELSE NULL END) WAR38,
                                        sum(CASE WHEN Age = "39" THEN WAR ELSE NULL END) WAR39,
                                        sum(CASE WHEN Age = "40" THEN WAR ELSE NULL END) WAR40,
                                        sum(CASE WHEN Age = "41" THEN WAR ELSE NULL END) WAR41,
                                        sum(CASE WHEN Age = "42" THEN WAR ELSE NULL END) WAR42,
                                        sum(CASE WHEN Age = "43" THEN WAR ELSE NULL END) WAR43,
                                        sum(CASE WHEN Age = "44" THEN WAR ELSE NULL END) WAR44,
                                        sum(CASE WHEN Age = "45" THEN WAR ELSE NULL END) WAR45,
                                        sum(CASE WHEN Age = "46" THEN WAR ELSE NULL END) WAR46
                                        FROM pitcher
                                        GROUP BY Name, playerid''')
    return df




def join_2014to2016_with_2017(spark, df):
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

def join_with_2017(spark, df):
    '''Custom Function: join_with_2017

        Description: 
            join given dataframe with 2017 raw data where player name matches.

        Args: 

        Return:
    '''


    df_2017 = spark.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema",
                "true").load("raw/2017_WAR.csv")
    df_2017.createOrReplaceTempView('w2017')
    df.createOrReplaceTempView('df')
    df = spark.sql('''SELECT df.*, w2017.WAR
                      FROM df, w2017
                      WHERE df.Player = w2017.Name
                      ''')
    return df

def rescaling(spark, df):
    '''Custom Function: rescaling

        Description: 
            Rescaling the range of all cloumns to [0,1] using max-min normalization.

        Args: 

        Return:

    '''

    columns = df.columns[2:-1] # except label, name, playerid
    from pyspark.sql.functions import col,min,max
    for column in columns:
        col_min = df.agg(min(column)).head()[0]
        col_max = df.agg(max(column)).head()[0]
        df = df.withColumn(column, (col(column)-col_min)/(col_max-col_min))
    return df
        
    
def WAR_clustering(spark, df, cluster_num=3):
    '''Custom Function: WAR_clustering

        Description: 
            Clustering given data frame along the distribution of WAR using K-Means

        Args: 
            cluster_num (int): the number of clusters that kmeans will make

        Return:

        Notes: Works poorly.
    '''
    all_columns = df.columns
    columns = ["WAR"]
    from pyspark.ml.feature import VectorAssembler
    from pyspark.ml.clustering import KMeans

    vecAssembler = VectorAssembler(inputCols=columns, outputCol="features")
    vector_df = vecAssembler.transform(df)
    kmeans = KMeans().setK(cluster_num).setSeed(42)
    model = kmeans.fit(vector_df)
    predictions = model.transform(vector_df)
   
    all_columns.append("prediction")
    df = predictions.select(all_columns)
    return df

def clustering(spark, df, cluster_num=3):
    '''Custom Function: clustering

        Description: 
            Clustering given data frame using K-Means

        Args: 
            cluster_num (int): the number of clusters that kmeans will make

        Return:

        Notes: Works poorly.
    '''
    all_columns = df.columns
    columns = df.columns[env.feature_start_index:env.feature_start_index + env.features_num]
    from pyspark.ml.feature import VectorAssembler
    from pyspark.ml.clustering import KMeans

    vecAssembler = VectorAssembler(inputCols=columns, outputCol="features")
    vector_df = vecAssembler.transform(df)
    kmeans = KMeans().setK(cluster_num).setSeed(42)
    model = kmeans.fit(vector_df)
    predictions = model.transform(vector_df)
   
    all_columns.append("prediction")
    df = predictions.select(all_columns)
    return df

def null_remover(spark, df, col=None):
    '''Custom Function: null_remover

        Description: 
            Remove all columns containing at least one null data

        Args: 

        Return:

    '''
    df.createOrReplaceTempView("df")
    if col==None:
        columns = df.columns
    else:
        columns = col
    for column in columns:
        df = df.filter(column + " is not null")
    return df


def join_8th_WAR(spark, df):
    df_1960_2018 = spark.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema",
                "true").load("raw/1960-2018.csv")
    df_1960_2018.createOrReplaceTempView("big_df")
    df.createOrReplaceTempView("df")
    df = spark.sql('''SELECT df.*, big_df.WAR as WAR8
                 FROM df, big_df
                 WHERE big_df.ServiceTime=8 AND df.playerid=big_df.playerid
                ''')
    return df

def join_age_WAR(spark, df, age):
    df_1960_2018 = spark.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema",
                "true").load("raw/1960-2018.csv")
    df_1960_2018.createOrReplaceTempView("big_df")
    df.createOrReplaceTempView("df")
    df = spark.sql("SELECT df.*, big_df.WAR as WAR" + str(age) + " FROM df, big_df WHERE big_df.AGE=" + str(age) + " AND df.playerid=big_df.playerid")
    return df


def join_clusters(spark, df, start_year, end_year):
    '''Custom Function: join_clusters

        Description: 
            join cluster information from clusters_until_start_year to clusters_until_end_year.

        Args:
            start_year (int): start year (1~15)
            end_year (int): end year (1~15, start_year<)

        Return:
        
    '''
    df = df.select(["Name", "playerid"]).withColumnRenamed('Name', 'Name_df').withColumnRenamed('playerid', 'playerid_df')
    for i in range(start_year, end_year + 1):
        new = spark.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema",
                "true").load("raw/clusters_players_until_career_" + str(i) + ".csv")
        cols = df.columns
        cols.append('Cluster')
        print("****************************************************************************************")
        print(cols)
        print("****************************************************************************************")
        df = df.join(new, df.playerid_df == new.playerid, 'inner').select(cols).withColumnRenamed('Cluster', 'Cluster'+str(i))

    df = df.withColumnRenamed('Name_df', 'Name').withColumnRenamed('playerid_df', 'playerid')

    return df



#################
#Split Functions#
#################

def random_split(spark, df):
    '''Split Function: random_split

        Description: 
            Randomly split data into train data, test data in the ratio of 9:1

        Args: 

        Return:

    '''

    train_df, test_df = df.randomSplit([0.9, 0.1], seed=42)
    return [train_df, test_df]


def test_2017_train_less2017_split(spark, df):
    '''Split Function: test_2017_train_less_2017_split

        Note: Default split function

        Description: 
            Split data into train data, test data by the year of latest year contained in data.

        Args: 

        Return:

    '''

   
    col_max = df.agg(max(col("1ySeason"))).head()[0]
    test_df = df.where(col("1ySeason") == col_max)
    train_df = df.where(col("1ySeason") < col_max)
    return [train_df, test_df]

def cluster_split(spark, df, cluster_num):
    out = []
    for i in range(cluster_num):
        out.append(df.where(col("prediction") == i))
    return out
    
