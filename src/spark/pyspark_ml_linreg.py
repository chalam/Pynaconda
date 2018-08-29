from pyspark.mllib.regression import LabeledPoint
import random

random.seed(1111)

test_data = []
train_data = []
for i in range(10):
    train_data += [[]]

with open("temperature_data_small.txt") as t:
    for l in t:
        fields = l.split()
        point = LabeledPoint(fields[22],
                             [fields[7], fields[8], fields[11], fields[21]])
        if random.random() >= 0.8:
            test_data += [point]
        else:
            train_data[random.randrange(10)] += [point]
# Input fields:
#8. Relative humidity (dining room), in %.
#9. Relative humidity (room), in %.
#12. Rain, the proportion of the last 15 minutes where rain was detected (a value in range [0,1]).
#22. Outdoor temperature, in C.
#23. Outdoor relative humidity, in %.


from pyspark.mllib.regression import StreamingLinearRegressionWithSGD

sc = SparkContext(appName="HumidityPrediction")
ssc = StreamingContext(sc, 2)

training_data_stream = ssc.queueStream(
    [ssc.sparkContext.parallelize(d) for d in train_data])
test_data_stream = ssc.queueStream(
    [test_data for d in train_data])\
    .map(lambda lp: (lp.label, lp.features))

##
model = StreamingLinearRegressionWithSGD(
    numIterations=5,
    stepSize=0.00005)
model.setInitialWeights([1.0,1.0,1.0,1.0])

model.trainOn(training_data_stream)

##
predictions = model.predictOnValues(test_data_stream)\
    .map(lambda x: (x[0], x[1], (x[0] - x[1])))

predictions.map(lambda x:
                "Actual: " + str(x[0])
                + ", Predicted: " + str(x[1])
                + ", Error: " + str(x[2])).pprint()
predictions.map(lambda x: (x[2]**2, 1))\
    .reduce(lambda x,y: (x[0] + y[0], x[1] + y[1]))\
    .map(lambda x: "MSE: " + str(x[0]/x[1]))\
    .pprint()

##
ssc.start()
for i in range(10):
    sleep(2)
    print(model.latestModel())
ssc.stop(stopSparkContext=True, stopGraceFully=True)