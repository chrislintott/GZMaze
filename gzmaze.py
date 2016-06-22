####################################
### Flask app for GZ QR code webpage
####################################


from __future__ import print_function, division, unicode_literals
import numpy as np

from flask import Flask, jsonify, render_template, request
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()
app = Flask(__name__)

import os
token = os.environ.get('ADS_DEV_KEY', None)
if token:
	ads.config.token = token

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def get_gz_qrcode():
	### insert function here

	
if __name__ == '__main__':
    app.run()
