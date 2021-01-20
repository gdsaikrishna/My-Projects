import pyqrcode
from pyqrcode import QRCode
value = "https://www.kaggle.com/getting-started/51445"
code = pyqrcode.create(value)
code.svg("random.svg", scale=8) 