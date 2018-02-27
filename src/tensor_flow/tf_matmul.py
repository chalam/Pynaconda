# https://github.com/chalam/TensorFlow-1x-Deep-Learning-Cookbook/tree/master/Chapter01
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'  ## To deactivate SSE Warnings
# Create a graph

# Selecting only CPU
with tf.device('/cpu:0'):
    rand_t = tf.random_uniform([50, 50], 0, 10, dtype=tf.float32, seed=0)
    a = tf.Variable(rand_t)
    b = tf.Variable(rand_t)
    c = tf.matmul(a, b)
    init = tf.global_variables_initializer()
# sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,log_device_placement=True))
# sess.run(init)
# print(sess.run(c))
# sess.close()

    with tf.Session(config=tf.ConfigProto(allow_soft_placement=True,log_device_placement=True)) as sess:
        writer = tf.summary.FileWriter('graphs', sess.graph) # To activate Tensorboard
        sess.run(init)
        print(sess.run(c))

# Create two random matrices
a = tf.Variable(tf.random_normal([4,5], stddev=2))
b = tf.Variable(tf.random_normal([4,5], stddev=2))

#Element Wise Multiplication
A = a * b

#Multiplication with a scalar 2
B = tf.scalar_mul(2, A)

# Elementwise division, its result is
C = tf.div(a,b)

#Element Wise remainder of division
D = tf.mod(a,b)

# Pairwise cross product
#E = tf.cross(a,b)
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    writer = tf.summary.FileWriter('graphs', sess.graph)
    a,b,A_R, B_R, C_R, D_R = sess.run([a , b, A, B, C, D])
    print("a\n",a,"\nb\n",b, "\na*b\n", A_R, "\n2*a*b\n", B_R, "\na/b\n", C_R, "\na%b\n", D_R)


    #Define a 5x5 Identity matrix
    I_matrix = tf.zeros(5)
    print(I_matrix.eval()) # This will print a zero matrix with 5 elements

    #Define a Variable initialized to a 10x10 identity matrix
    X = tf.Variable(tf.eye(10))
    X.initializer.run()  # Initialize the Variable
    print(X.eval()) # Evaluate the Variable and print the result

    #Create a random 5x10 matrix
    A = tf.Variable(tf.random_normal([5,10]))
    A.initializer.run()

    #Multiply two matrices
    product = tf.matmul(A, X)
    print(product.eval())

    #create a random matrix of 1s and 0s, size 5x10
    b = tf.Variable(tf.random_uniform([5,10], 0, 2, dtype= tf.int32))
    b.initializer.run()
    print(b.eval())
    b_new = tf.cast(b, dtype=tf.float32)

    # Add the two matrices
    t_sum = tf.add(product, b_new)
    t_sub = product -b_new
    print("A*X _b\n", t_sum.eval())
    print("A*X - b\n", t_sub.eval())

    writer.close()
