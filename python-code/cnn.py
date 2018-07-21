# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image

''' Part 1 - Setting up for CNN'''
classifier = Sequential()

# Convolution Layer 1 (32 filters, 3x3 filter shape, 50x50x3 input shape, relu = rectifier function)
classifier.add(Conv2D(32, (3, 3), input_shape = (50,50,3), activation = 'relu'))
# Pooling (this would be more computation, but by having 2x2 we have minimum pixel loss)
classifier.add(MaxPooling2D(pool_size = (2,2)))
# Convolution Layer 2
classifier.add(Conv2D(32, (3,3), activation = 'relu'))
# Pooling
classifier.add(MaxPooling2D(pool_size = (2,2))))
# Flatten (making a matrix -> vector)
classifier.add(Flatten())
# Full Connection (it's common practice to use power of 2 for units, optimal unit is gained through trial and error)
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid')) # sigmoid -> making into a log curve for distinction

# Compiling all the process on top to make a basic CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


'''Part 2 - Training and Testing CNN'''
# this changes per local (make sure you change it)
trainPath = '/Users/jinwoo/Desktop/project-images/train_set'
testPath = '/Users/jinwoo/Desktop/project-images/test_set'
# transforming images so that it doesn't overfit
trainDatagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
testDatagen = ImageDataGenerator(rescale = 1./255)
trainSet = trainDatagen.flow_from_directory(trainPath, target_size = (50, 50), batch_size = 32, class_mode = 'binary')
testSet = testDatagen.flow_from_directory(testPath, target_size = (50, 50), batch_size = 32, class_mode = 'binary')
# steps per epoch = size of training set / validation step = size of test set
classifier.fit_generator(trainSet, steps_per_epoch = 4345, epochs = 10, validation_data = testSet, validation_steps = 1202)
