import tensorflow as tf

# TensorFlow separates the definition of computations from their execution
# even further by having them happen in separate places: a graph defines
# the operations, but the operations only happen within a session.
# Graphs and sessions are created independently.
# A graph is like a blueprint and a session is like a construction site.

tf.reset_default_graph()
sess = tf.Session()
x = tf.constant(1.0, name='input')
print('`x` evaluates to: {}'.format(sess.run(x)))

w = tf.Variable(0.8, name='weight')
y = tf.multiply(w, x, name='output')
y_ = tf.constant(0.0, name='correct_value')

loss = tf.pow(y - y_, 2, name='loss')

# gradient descent optimizer can update the weight based on the derivative of the loss.
# The optimizer takes a learning rate to moderate the size of the updates
optim = tf.train.GradientDescentOptimizer(learning_rate=0.025)
grads_and_vars = tf.train.GradientDescentOptimizer(learning_rate=0.025).compute_gradients(loss)
sess.run(tf.initialize_all_variables())
print('The gradient is: {}'.format(sess.run(grads_and_vars[0][0])))

# Let's apply the gradient, finishing the backpropagation.
sess.run(optim.apply_gradients(grads_and_vars))
print('The new value of the weight is: {}'.format(sess.run(w)))

# Instead of hand-holding the optimizer like this,
# we can make one operation that calculates and applies the gradients
train_step = tf.train.GradientDescentOptimizer(learning_rate=0.025).minimize(loss)

graph = tf.get_default_graph()
operations = graph.get_operations()
# print('`operations` is now: {}'.format(operations))
# print(operations[0].node_def)

for value in [x, w, y, y_, loss]:
    tf.summary.scalar(value.op.name, value)

summaries = tf.summary.merge_all()

# sess = tf.Session()
summary_writer = tf.summary.FileWriter('log_simple_stats', sess.graph)

sess.run(tf.initialize_all_variables())
for i in range(100):
    summary_writer.add_summary(sess.run(summaries), i)
    sess.run(train_step)