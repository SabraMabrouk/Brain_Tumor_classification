import tensorflow as tf

def image_to_example(image, label):
    img_raw = tf.io.encode_jpeg(tf.cast(image, tf.uint8)).numpy()
    
    feature = {
        'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
        'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[label]))
    }
    example = tf.train.Example(features=tf.train.Features(feature=feature))
    return example


def write_to_tfrecord(dataset, tfrecord_filename):
    with tf.io.TFRecordWriter(tfrecord_filename) as writer:
        for batch_images, batch_labels in dataset:
            batch_labels = tf.argmax(batch_labels, axis=1)  
            
            for img, label in zip(batch_images, batch_labels):
                example = image_to_example(img, label.numpy())
                writer.write(example.SerializeToString())


