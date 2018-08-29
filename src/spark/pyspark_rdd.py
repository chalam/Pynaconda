from operator import add, sub
from time import sleep
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Set up the Spark context and the streaming context
sc = SparkContext(appName="PysparkNotebook")
ssc = StreamingContext(sc, 1)

# Input data
rddQueue = []
for i in range(5):
    rddQueue += [ssc.sparkContext.parallelize([i, i+1])]

inputStream = ssc.queueStream(rddQueue)

inputStream.map(lambda x: "Input: " + str(x)).pprint()
inputStream.reduce(add)\
    .map(lambda x: "Output: " + str(x))\
    .pprint()

ssc.start()
sleep(5)
ssc.stop(stopSparkContext=True, stopGraceFully=True)