####################################
### Flask app for GZ QR code webpage
####################################


from __future__ import print_function, division, unicode_literals
import numpy as np
import StringIO

from flask import Flask, jsonify, render_template, request, send_file, make_response
from werkzeug.contrib.cache import SimpleCache
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import json
import qrcode
import requests
cache = SimpleCache()
app = Flask(__name__)

import os
token = os.environ.get('ADS_DEV_KEY', None)
if token:
	ads.config.token = token


@app.route('/')
def homepage():
	imageURL, galid = img()

	return render_template('index.html', galid=galid, imageURL=imageURL)

@app.route('/images/<galaxy>')
def img():
  	#insert code to get galaxy image here
	url = 'https://panoptes.zooniverse.org/api/subjects?workflow_id=2076&sort=queued'
	headers = {'Content-Type':'application/json', 'Accept':'application/vnd.api+json; version=1'}

	r=requests.get(url,headers=headers)
	sub=r.json()

	galid =sub['subjects'][0]['id']
	ImageURL=sub['subjects'][0]['locations'][0]['image/jpeg']
	return ImageURL, galid

@app.route('/images/qrcode/<galid>')
def get_qrcode(galid):
	qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
	)

	qr.add_data(galid)
	qr.make(fit=True)

	img = qr.make_image()
	fig = plt.figure(frameon=False)
	axis = fig.add_subplot(111)
	axis.imshow(img)
	axis.axis('off')
	#plt.subplots_adjust(top = 0, bottom = 0, right = 0, left = 0, hspace = 0, wspace = 0)
	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	return response


	
if __name__ == '__main__':
	app.debug = True
	app.run()
