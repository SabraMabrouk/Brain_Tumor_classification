import tensorflow as tf

def parse_example(serialized_example):
    
    feature_description = {
        'image': tf.io.FixedLenFeature([], tf.string),
        'label': tf.io.FixedLenFeature([], tf.int64)
    }
 
    parsed_example = tf.io.parse_single_example(serialized_example, feature_description)
    image = tf.io.decode_jpeg(parsed_example['image'], channels=3)
    label = parsed_example['label']
    image = tf.image.resize(image, [150, 150])  

    return image, label