import tensorflow as tf

cfig = tf.ConfigProto(log_device_placement=True)
hello = tf.constant("Hello,TF!")
print('tf.__version__:',tf.__version__)