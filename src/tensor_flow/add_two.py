import tensorflow as tf

## build the compute graph
a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0) # also tf.float32 implicitly
total = a + b
print(a) # no output yet
print(b)
print(total)

# evaluate the graph
sess = tf.Session()
print(sess.run(total))
print(sess.run({'ab':(a, b), 'total':total}))

# any tf.Tensor has the same value in the session.run
vec = tf.random_uniform(shape=(3,))
out1 = vec + 1
out2 = vec + 2
print(sess.run(vec))
print(sess.run(vec))
print(sess.run((vec, out1, out2))) # same vec for out1 and out2

v_1 = tf.constant([1, 2, 3, 4])
v_2 = tf.constant([2, 1, 5, 3])
I_matrix = tf.eye(5)
v_add = v_1 + v_2  # tf.add(v_1,v_2)

x = tf.placeholder('float')
y = 2 * x
data = tf.random_uniform([4, 5], 10)
with tf.Session() as sess:
    writer = tf.summary.FileWriter('graphs', sess.graph) # To activate Tensorboard
    x_data = sess.run(data)
    print(x_data)
    print(sess.run(y, feed_dict={x: x_data}))

    print(v_add.eval())
    print(I_matrix.eval())
