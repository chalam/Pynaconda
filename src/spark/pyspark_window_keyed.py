sc = SparkContext(appName="HighScores")
ssc = StreamingContext(sc, 1)
ssc.checkpoint("highscore-checkpoints")

player_score_pairs = [
    [("Alice", 100), ("Bob", 60)],
    [("Bob", 60)],
    [("Carlos", 90), ("Dan", 40)],
    [("Carlos", 10), ("Dan", 20), ("Erin", 90)],
    [("Carlos", 20), ("Frank", 200)],
]

rddQueue = []
for datum in player_score_pairs:
    rddQueue += [ssc.sparkContext.parallelize(datum)]

inputStream = ssc.queueStream(rddQueue)
inputStream.reduceByKeyAndWindow(add, sub, 3, 1)\
    .pprint()

ssc.start()
sleep(5)
ssc.stop(stopSparkContext=True, stopGraceFully=True)