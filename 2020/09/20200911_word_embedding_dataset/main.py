import os

import tensorflow as tf


# noinspection PyShadowingNames
def download_and_read(url):
    local_file = url.split('/')[-1]
    tf.keras.utils.get_file(local_file, url, extract=True, cache_dir='.')
    labels, texts = [], []
    local_file = os.path.join('datasets', 'SMSSpamCollection')
    with open(local_file, 'r', encoding='utf-8') as fin:
        for line in fin:
            label, text = line.strip().split('\t')
            labels.append(1 if label == 'spam' else 0)
            texts.append(text)
    return texts, labels


if __name__ == '__main__':
    texts, labels = download_and_read('https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip')

    # tokenize and pad text
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(texts)
    text_sequences = tokenizer.texts_to_sequences(texts)
    text_sequences = tf.keras.preprocessing.sequence.pad_sequences(text_sequences)

    # labels
    NUM_CLASSES = 2
    cat_labels = tf.keras.utils.to_categorical(labels, num_classes=NUM_CLASSES)

    # dataset
    dataset = tf.data.Dataset.from_tensor_slices((text_sequences, cat_labels))
    dataset = dataset.shuffle(10000)

    num_records = len(text_sequences)
    test_size = num_records // 4  # get int part
    val_size = (num_records - test_size) // 10

    test_dataset = dataset.take(test_size)
    val_dataset = dataset.skip(test_size).take(val_size)
    train_dataset = dataset.skip(test_size + val_size)

    BATCH_SIZE = 128
    test_dataset = test_dataset.batch(BATCH_SIZE, drop_remainder=True)
    val_dataset = val_dataset.batch(BATCH_SIZE, drop_remainder=True)
    train_dataset = train_dataset.batch(BATCH_SIZE, drop_remainder=True)
