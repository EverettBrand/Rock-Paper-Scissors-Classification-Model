from flask import Flask, jsonify, request
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
import numpy as np
from datetime import date

# initialize our Flask application
app = Flask(__name__)

@app.route("/name", methods=["POST"])
def setName():
    today = date.today()

    d2 = today.strftime("%B %d, %Y")

    return jsonify('Rock, Paper and Scissors image classification server.', 'Everett Brandenburg', d2)


# load the model
model = tf.keras.models.load_model('rps.h5')

@app.route('/api',methods=['POST'])
def predict():
    #Display server name and port number
    print(request.host_url)

    #get the data sent to server
    data = request.get_json(force=True)

    #load image at local path given by data['exp']
    img = image.load_img(data['exp'], target_size=(150, 150))

    #get image ready to be loaded into predict function
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    #predict
    prediction = model.predict(img)

    # Take the first value of prediction
    output = prediction[0]

    #array determines output 0: paper 1: rock 2: scissors
    if(output[0] == 1):
        return jsonify('paper')
    elif(output[1] == 1):
        return jsonify('rock')
    elif(output[2] == 1):
        return jsonify('scissors')

#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(port=5000, debug=True)
