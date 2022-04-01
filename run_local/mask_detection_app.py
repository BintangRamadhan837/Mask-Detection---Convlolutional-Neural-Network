import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow import expand_dims
from tensorflow.keras import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax


def main():
    # st.markdown("<h1 style='text-align: center; color: grey;'>00</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: grey;'>======= MASK DETECTION =======</h1>", unsafe_allow_html=True)

    file_uploaded = st.file_uploader("Choose the file", type = ['jpg', 'png', 'jpeg']) #upload file
    if file_uploaded is not None:
        image = Image.open(file_uploaded) #buka uploaded file
        figure = plt.figure()
        plt.imshow(image)
        plt.axis("off")
        result = predict_class(image)
        st.write(result)
        st.pyplot(figure)

def predict_class(image):
    classifier_model = tf.keras.models.load_model('model_tl.h5') #load model
    shape = ((300, 300, 3))
    test_image = image.resize((300, 300)) #resize
    test_image = preprocessing.image.img_to_array(test_image) #img to array
    test_image = test_image/255.0 #rescale
    # test_image = np.expand_dims(test_image, axis = 0)
    # class_names = [' Incorrect Mask ',
    #                 ' With Mask ',
    #                 ' Without Mask ']
    # predictions = classifier_model.predict(test_image) #predict model
    # score = tf.nn.softmax(predictions[0])
    # score = score.numpy()
    # image_class = class_names[np.argmax(score)] #result
    # # result = "The image uploaded is : {}".format(image_class)
    # # result = image_class
    # st.title("The Image Uploaded is : {}".format(image_class))
    # # return result

    test_image = expand_dims(test_image, axis = 0)
    predictions = classifier_model.predict(test_image) #predict model
    result = predictions.argmax()
    if result == 0:
        st.title("The Image Uploaded is : Incorrect Mask")
    elif result == 1:
        st.title("The Image Uploaded is : With Mask")
    else:
        st.title("The Image Uploaded is : Without Mask")


if __name__  == "__main__":
    main()