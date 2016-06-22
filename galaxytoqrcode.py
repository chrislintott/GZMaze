import qrcode # get this https://pypi.python.org/pypi/qrcode eg with pip install qrcode
import json
import matplotlib.pyplot as plt

#Set up parameters for getting stuff

url = 'https://panoptes.zooniverse.org/api/subjects?workflow_id=2076&sort=queued'
headers = {'Content-Type':'application/json', 'Accept':'application/vnd.api+json; version=1'}

r=requests.get(url,headers=headers)
sub=r.json()

id=sub['subjects'][0]['id']
ImageURL=sub['subjects'][0]['locations'][0]['image/jpeg']

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(id)
qr.make(fit=True)

img = qr.make_image()

plt.imshow(img)
plt.show()