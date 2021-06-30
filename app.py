# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from model1 import imgg, pimgg
import base64
import json
import time
# Declare a flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    img = request.files['file']
    new_graph_name = "graph" + str(time.time()) + ".png"
    img.save("./"+new_graph_name)
    pimgg(new_graph_name)
    imgg(new_graph_name)
    return render_template('index.html', result=1, pimggg=new_graph_name)
  return render_template('index.html')


  


if __name__ == '__main__':
  app.run()
