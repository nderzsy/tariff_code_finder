from flaskexample.a_Model import ModelIt
from flask import render_template
from flaskexample import app
from flask import request
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import numpy as np
import pandas as pd
import psycopg2
import pickle
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier


with open ('model_file', 'rb') as fp1:
  model = pickle.load(fp1)

with open ('class_labels', 'rb') as fp2:
  class_labels = pickle.load(fp2)
    
with open ('trained_file', 'rb') as fp3:
  trained_data = pickle.load(fp3)


@app.route('/')
@app.route('/index')
@app.route('/input')
def input():
    return render_template("input.html")

@app.route('/output')
def output():
 #pull 'test_item' from input field and store it
  test_item = [request.args.get('test_item')]

  predicted_item_svm = model.predict(test_item)
  class_label = class_labels[int(predicted_item_svm)-1]
  #print("{} - {}".format(predicted_item_svm, class_labels[int(predicted_item_svm)-1]))

  return render_template("output.html", pred=predicted_item_svm, cllab = class_label)