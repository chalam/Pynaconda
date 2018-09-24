import numpy as np

# Simple Holdout

data, test_data = None
def get_model(): pass

num_validation_samples = 10000

np.random.shuffle(data)

# after shuffle create a holdout validation
validation_data = data[:num_validation_samples]
data = data[num_validation_samples:]

training_data = data[:]

# tuned your hyperparameters
model = get_model()
model.train(training_data)
validation_score = model.evaluate(validation_data)


# At this point you can tune your model,
# retrain it, evaluate it, tune it again...

model = get_model()
model.train(np.concatenate([training_data,
                            validation_data]))
test_score = model.evaluate(test_data)


# K-Fold
k = 4
num_validation_samples = len(data) // k

np.random.shuffle(data)

validation_scores = []
for fold in range(k):
    #  Selects the validation-data partition
    validation_data = data[num_validation_samples * fold:num_validation_samples * (fold + 1)]
    # the rest in train
    training_data = data[:num_validation_samples * fold] + data[num_validation_samples * (fold + 1):]
    # create a new instance model
    model = get_model()
    model.train(training_data)
    validation_score = model.evaluate(validation_data)
    validation_scores.append(validation_score)

# avg of all scores from k folds
validation_score = np.average(validation_scores)

# final train
model = get_model()
model.train(data)
test_score = model.evaluate(test_data)

# Iterative K-Fold
num_epochs = 500
all_mae_histories = []
for i in range(k):
    print('processing fold #', i)
    # 1 Prepares the validation data: data from partition #k
    val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
    val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]
    # 2 Prepares the training data: data from all other partitions
    partial_train_data = np.concatenate(
        [train_data[:i * num_val_samples],
         train_data[(i + 1) * num_val_samples:]],
        axis=0)

    partial_train_targets = np.concatenate(
        [train_targets[:i * num_val_samples],
         train_targets[(i + 1) * num_val_samples:]],
        axis=0)

    # 3 Builds the Keras model (already compiled)
    model = build_model()
    # 4 Trains the model (in silent mode, verbose=0)
    history = model.fit(partial_train_data, partial_train_targets,
                        validation_data=(val_data, val_targets),
                        epochs=num_epochs, batch_size=1, verbose=0)

    mae_history = history.history['val_mean_absolute_error']
    all_mae_histories.append(mae_history)


# Add Regularization L1 and L2

from keras import regularizers
model = models.Sequential()
model.add(layers.Dense(16, kernel_regularizer=regularizers.l2(0.001),
                       activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, kernel_regularizer=regularizers.l2(0.001),
                       activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

regularizers.l1(0.001)                         # L1 regularization
regularizers.l1_l2(l1=0.001, l2=0.001)         # * 2 Simultaneous L1 and L2 regularization

# Add drop outs
model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))