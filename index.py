from flask import Flask
import time
import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.SCL, board.SDA)

mcps = []
for item in i2c.scan():
    print(item)
    mcp = MCP23017(i2c,address=item) 
    mcps.append(mcp)
print(mcps)
print(i2c.scan())

app = Flask(__name__)



@app.route('/test')
def hello():
    pin0 = mcp.get_pin(0)
    pin1 = mcp.get_pin(1)
    pin0.switch_to_output(value=False)
    return 'Hello, World!'

@app.route('/toggle-state/<int:icNumber>/<int:pin>/<int:state>')
def toggleState(icNumber,pin,state):
    mcp = mcps[icNumber]
    print(mcp)
    if mcp:
        _pin = mcp.get_pin(pin)
        _pin.switch_to_output(value=state)
        return 'Pin ' + str(pin) + ' set to : ' + str(state)

if __name__ =='__main__':  
    app.run(debug = True,host="0.0.0.0")  
