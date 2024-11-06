# Implement image processing model using computer vision libraries like tensorflow, keras. For classification problems  

import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load and preprocess the CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize pixel values to be between 0 and 1
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# One-hot encode the labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Step 2: Build the CNN model
model = models.Sequential()

# First Convolutional Block
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))

# Second Convolutional Block
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Third Convolutional Block
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Fully connected layers (Dense)
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))

# Output layer (10 classes)
model.add(layers.Dense(10, activation='softmax'))

# Step 3: Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 4: Train the model
history = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))

# Step 5: Evaluate the model on the test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc * 100:.2f}%")

# Step 6: Visualize the training process (accuracy and loss)
# Plot accuracy
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy over epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='upper left')

# Plot loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss over epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(loc='upper right')

plt.show()

# Step 7: Save the trained model
model.save('cifar10_image_classification_model.h5')

# Step 8: Predict on a test image
image = x_test[0].reshape(1, 32, 32, 3)  # Reshape the image to (1, 32, 32, 3) for prediction
prediction = model.predict(image)
predicted_class = np.argmax(prediction, axis=1)

print(f"Predicted class for the first test image: {predicted_class[0]}")

# Ouput:
# Downloading data from https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
# 170498071/170498071 [==============================] - 54s 0us/step
# 2024-11-06 19:34:44.036250: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
# To enable the following instructions: SSE SSE2 SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
# Epoch 1/10
# 782/782 [==============================] - 21s 26ms/step - loss: 1.5961 - accuracy: 0.4157 - val_loss: 1.3469 - val_accuracy: 0.5091
# Epoch 2/10
# 782/782 [==============================] - 20s 26ms/step - loss: 1.2467 - accuracy: 0.5576 - val_loss: 1.1845 - val_accuracy: 0.5754
# Epoch 3/10
# 782/782 [==============================] - 20s 26ms/step - loss: 1.1060 - accuracy: 0.6097 - val_loss: 1.0655 - val_accuracy: 0.6237
# Epoch 4/10
# 782/782 [==============================] - 19s 25ms/step - loss: 0.9973 - accuracy: 0.6510 - val_loss: 0.9950 - val_accuracy: 0.6483
# Epoch 5/10
# 782/782 [==============================] - 20s 25ms/step - loss: 0.9218 - accuracy: 0.6771 - val_loss: 0.9184 - val_accuracy: 0.6784
# Epoch 6/10
# 782/782 [==============================] - 20s 25ms/step - loss: 0.8591 - accuracy: 0.7018 - val_loss: 0.9597 - val_accuracy: 0.6651
# Epoch 7/10
# 782/782 [==============================] - 20s 26ms/step - loss: 0.8151 - accuracy: 0.7166 - val_loss: 0.9065 - val_accuracy: 0.6878
# Epoch 8/10
# 782/782 [==============================] - 20s 25ms/step - loss: 0.7707 - accuracy: 0.7323 - val_loss: 0.9149 - val_accuracy: 0.6901
# Epoch 9/10
# 782/782 [==============================] - 20s 25ms/step - loss: 0.7327 - accuracy: 0.7455 - val_loss: 0.8544 - val_accuracy: 0.7054
# Epoch 10/10
# 782/782 [==============================] - 20s 26ms/step - loss: 0.7011 - accuracy: 0.7548 - val_loss: 0.8616 - val_accuracy: 0.7085
# 313/313 [==============================] - 1s 4ms/step - loss: 0.8616 - accuracy: 0.7085
# Test accuracy: 70.85%
# C:\Users\yagni\AppData\Local\Programs\Python\Python311\Lib\site-packages\keras\src\engine\training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
#   saving_api.save_model(
# 1/1 [==============================] - 0s 101ms/step
# Predicted class for the first test image: 3