from flask import Flask
import time
import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c) 


app = Flask(__name__)



@app.route('/test')
def hello():
    pin0 = mcp.get_pin(0)
    pin1 = mcp.get_pin(1)
    pin0.switch_to_output(value=False)
    return 'Hello, World!'

@app.route('/toggle-state/<int:pin>/<int:state>')
def toggleState(pin,state):
    pin = mcp.get_pin(pin)
    pin.switch_to_output(value=state)
    return 'Pin ' + str(pin) + ' set to : ' + str(state)

if __name__ =='__main__':  
    app.run(debug = True,host="0.0.0.0")  
