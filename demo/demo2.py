'''
@Author: your name
@Date: 2019-11-24 10:46:05
@LastEditTime: 2019-11-24 10:48:34
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \python\demo2.py
'''
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))