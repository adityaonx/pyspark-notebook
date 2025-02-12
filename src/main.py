from pyspark import SparkContext, SparkConf

# Create a SparkConf object to configure your Spark application
conf = SparkConf().setAppName("MySparkApp")

# Create a SparkContext object, which is the entry point to Spark functionality
sc = SparkContext(conf=conf)
# Set the log level to ERROR
sc.setLogLevel("WARN")

# Your Spark application code goes here...
# For example:
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
result = rdd.map(lambda x: x * 2).collect()
print(result)

# Stop the SparkContext when your application is finished
sc.stop()