import serial 
import time
from flask import Flask, render_template, request

## GLOBALS
serialPort = '/dev/ttyACM0'
serverIP = '192.168.0.10'
port = 5005
# try:
arduino = serial.Serial(serialPort, 9600)

# Flask initialization
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Nico mancoooo!!'

@app.route('/leds/', methods=['POST', 'GET'])
def leds():
  form = request.form
  if request.method == 'POST':
    if request.form['submit_button'] == 'Lights on':
      arduino.write('1'.encode())
      return render_template('leds.html', form=form)
    elif request.form['submit_button'] == 'Lights off':
      arduino.write('2'.encode()) 
      return render_template('leds.html', form=form)
    else:
        pass # unknown
  elif request.method == 'GET':
      return render_template('leds.html', form=form)

if __name__ == "__main__":
  app.debug = True
  app.run(host=serverIP, port=port)


