sc = SparkContext(appName="ActiveUsers")
ssc = StreamingContext(sc, 1)

activeUsers = [
    ["Alice", "Bob"],
    ["Bob"],
    ["Carlos", "Dan"],
    ["Carlos", "Dan", "Erin"],
    ["Carlos", "Frank"],
]

rddQueue = []
for datum in activeUsers:
    rddQueue += [ssc.sparkContext.parallelize(datum)]

inputStream = ssc.queueStream(rddQueue)
inputStream.window(5, 1)\
    .map(lambda x: set([x]))\
    .reduce(lambda x, y: x.union(y))\
    .pprint()

ssc.start()
sleep(5)
ssc.stop(stopSparkContext=True, stopGraceFully=True)