# -*- coding: utf-8 -*-
"""fashionMNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e_9enV-VaKTRDcfbeg3rt_jq0WSgNqHb
"""

import tensorflow as tf
print(tf.__version__)

# data collection
mnist = tf.keras.datasets.fashion_mnist

# loading of data
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# data visulaization
import matplotlib.pyplot as plt
plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])

# data visulaization-2
import matplotlib.pyplot as plt
plt.imshow(training_images[1])
print(training_labels[1])
print(training_images[1])

# data normalisation
training_images  = training_images / 255.0
test_images = test_images / 255.0

# design the model with 3 layers model
# Sequential defines a sequence of layers in the neural network.
# Flatten takes a square and turns it into a one-dimensional vector.
# Dense adds a layer of neurons.
# Activation functions tell each layer of neurons what to do:
# Relu effectively means that if X is greater than 0 return X, else return 0. It only passes values of 0 or greater to the next layer in the network.
# Softmax takes a set of values, and effectively picks the biggest one.
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), tf.keras.layers.Dense(128, activation=tf.nn.relu), tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

# Model building and training
model.compile(optimizer = tf.keras.optimizers.Adam(), loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=5)

# Test the model
model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)
print(classifications[0])

print(test_labels[0])

classifications = model.predict(test_images)

print(classifications[1])

print(test_labels[1])

# Hidden Layers increased
import tensorflow as tf
print(tf.__version__)

mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

training_images = training_images/255.0
test_images = test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(1024, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy')

model.fit(training_images, training_labels, epochs=5)

model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)

print(classifications[0])
print(test_labels[0])

import tensorflow as tf
print(tf.__version__)

mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

training_images = training_images/255.0
test_images = test_images/255.0


model = tf.keras.models.Sequential([tf.keras.layers.Dense(64, activation=tf.nn.relu),tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

# This version has the 'flatten' removed. Replace the above with this one to see the error.
#model = tf.keras.models.Sequential([tf.keras.layers.Dense(64, activation=tf.nn.relu),
#                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])


model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy')

model.fit(training_images, training_labels, epochs=5)

model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)

print(classifications[1])
print(test_labels[1])

## Error detection details:
## The Flatten layer is needed in this case because the input data for the neural network is a two-dimensional array (a 28x28 image), but the Dense layers expect one-dimensional input data.
## Without the Flatten layer, the input data would be passed to the Dense layers as a two-dimensional array, which would result in an error.

### Here's a more detailed explanation:

##The Dense layer expects input data in the following format: [batch_size, features]. In this case, the batch size is the number of images being processed at once, and the features are the individual pixels in each image.
##The input data for this neural network is a two-dimensional array with the shape (28, 28). This means that each image is represented as a 28x28 grid of pixels.
##To convert the two-dimensional input data into one-dimensional data, we need to flatten it. This means that we need to take all of the pixels in each image and arrange them in a single row.
##The Flatten layer does this for us. It takes the two-dimensional input data and reshapes it into a one-dimensional array with the shape [batch_size, 784]. This is because there are 28x28 = 784 pixels in each image.
##The one-dimensional output from the Flatten layer can then be passed to the Dense layers.
##In general, the Flatten layer is used whenever you have input data that is not already in the correct format for the Dense layers. For example, if you have input data that is a three-dimensional array (e.g., a color image), you would need to use a Flatten layer to convert it into a one-dimensional array before passing it to the Dense layers.

# Another checking
import tensorflow as tf
print(tf.__version__)

mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

training_images = training_images/255.0
test_images = test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(64, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(5, activation=tf.nn.softmax)])

# Replace the above model definiton with this one to see the network with 5 output layers
# And you'll see errors as a result!
# model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
#                                    tf.keras.layers.Dense(64, activation=tf.nn.relu),
#                                    tf.keras.layers.Dense(5, activation=tf.nn.softmax)])

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy')

model.fit(training_images, training_labels, epochs=5)

model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)

print(classifications[0])
print(test_labels[0])

# The error message points to an issue with the sparse_categorical_crossentropy loss function.
# The error message states that a label value of 9 is outside the valid range of [0, 5).
# This means that the model is expecting labels between 0 and 4, but it encountered a label of 9.
print(training_labels)
print(test_labels)

# From above we can cnclude that there is need to change the output layer of the model to have 10 neurons instead of 5.

# Consider the effects of additional layers in the network.
# What will happen if you add another layer between the one with 512 and the final layer with 10?
# There isn't a significant impact -- because this is relatively simple data.
# For far more complex data (including color images to be classified as flowers that you'll see in the next lesson), extra layers are often necessary.
import tensorflow as tf
print(tf.__version__)

mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

training_images = training_images/255.0
test_images = test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(512, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(256, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy')

model.fit(training_images, training_labels, epochs=5)

model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)

print(classifications[0])
print(test_labels[0])

# Consider the impact of training for more or less epochs. Why do you think that would be the case?

# I have tried 15 epochs -- Got a model with a much better loss than the one with 5 Try 30 epochs
# Saw the loss value stops decreasing, and sometimes increases.
# This is a side effect of something called 'overfitting' which you can learn about [somewhere]
# It is something you need to keep an eye out for when training neural networks.
# There's no point in wasting your time training if you aren't improving your loss, right! :)
import tensorflow as tf
print(tf.__version__)

mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels) ,  (test_images, test_labels) = mnist.load_data()

training_images = training_images/255.0
test_images = test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy')

model.fit(training_images, training_labels, epochs=30)

model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)

print(classifications[34])
print(test_labels[34])

# Before I trained, normalized the data, going from values that were 0 through 255 to values that were 0 through 1.
# What would be the impact of removing that?
import tensorflow as tf
print(tf.__version__)
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(training_images, training_labels, epochs=5)
model.evaluate(test_images, test_labels)
classifications = model.predict(test_images)
print(classifications[0])
print(test_labels[0])

# In a nutshell, normalization reduces the complexity of the problem your network is trying to solve.
## This can potentially increase the accuracy of your model and speed up the training.
### You bring the data on the same scale and reduce variance.
### None of the weights in the network are wasted on doing a normalization for you, meaning that they can be used more efficiently to solve the actual task at hand.

# Earlier when I trained for extra epochs I had an issue where my loss might change.
# It might have taken a bit of time for one to wait for the training to do that,
# One might have thought 'wouldn't it be nice if I could stop the training when I reach a desired value?' -- i.e. 95% accuracy might be enough for one.
# If one reaches that after 3 epochs, why sit around waiting for it to finish a lot more epochs....
# So how would one fix that? Like any other program...One has callbacks! Let's see them in action...
import tensorflow as tf
print(tf.__version__)

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>0.9):
      print("\nReached 90% accuracy so cancelling training!")
      self.model.stop_training = True

callbacks = myCallback()
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images/255.0
test_images=test_images/255.0
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), tf.keras.layers.Dense(512, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])