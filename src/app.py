from flask import Flask, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)

relay_pin = 17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

@app.route('/')
def index():
    relay_status = GPIO.input(relay_pin)
    return jsonify(relay_status=bool(relay_status))

@app.route('/turn-off')
def turn_on():
    GPIO.output(relay_pin, GPIO.HIGH)
    return jsonify(status='success', message='Relay turned Off')

@app.route('/turn-on')
def turn_off():
    GPIO.output(relay_pin, GPIO.LOW)
    return jsonify(status='success', message='Relay turned ON')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    