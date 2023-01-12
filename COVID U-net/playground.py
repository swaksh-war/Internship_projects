import tensorflow as tf
import matplotlib.pyplot as plt
import cv2

model = tf.keras.models.load_model('model.h5')

img_path = str(input('enter image path: '))
lung_test = cv2.imread(img_path)

predicted = model.predict(lung_test)
fig = plt.figure(figsize = (18,15))

plt.subplot(1,3,1)
plt.imshow(lung_test[100][...,0], cmap = 'bone')
plt.title('original lung')

plt.subplot(1,3,3)
plt.imshow(lung_test[100][...,0], cmap = 'bone')
plt.imshow(predicted[100][...,0],alpha = 0.5,cmap = "nipy_spectral")
plt.title('predicted infection mask')

fig.savefig('output.png')