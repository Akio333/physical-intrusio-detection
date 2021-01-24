
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


class FaceRecGraph(object):
    def __init__(self):
        self.graph = tf.Graph()
        #tf.io.write_graph(self.graph, './', "graph")
