# example of using a pre-trained model as a classifier
import cv2
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

# load an image from file saved from video_capture.py code run
# reshape it to 224x224x3 for vgg16
image = load_img('tiger.jpg', target_size=(224, 224))

# write frame to intermediate image file
filename = "intermediate_tiger.jpg"

# convert the image pixels to a numpy array
image = img_to_array(image)
print(image.shape)


# write image to file
cv2.imwrite(filename, image)

# reshape data for the model - from 224x224x3 to 1x224x224x3
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

(x,h, w, c) = image.shape # x , h - height w - width c - channels
print("x h w c - ",x,h,w,c)

# prepare the image for the VGG model
image = preprocess_input(image)

# load the model
model = VGG16()

# predict the probability across all output classes
yhat = model.predict(image)

# convert the probabilities to class labels
label = decode_predictions(yhat)

# print all objects predicted with decreasing probability on screen
print(label)

# retrieve the most likely result, e.g. highest probability
label = label[0][0]

# print the classification
print('%s (%.2f%%)' % (label[1], label[2]*100))


# save out to file
fh = open("objects_detected.txt", "w")
fh.write(label[1])
fh.close()
