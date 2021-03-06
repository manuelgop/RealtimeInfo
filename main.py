from flask import *
import time
import random
import sensor
import json




app = Flask(__name__)
sensor_thing = sensor.SensorThing()


@app.route("/")
def index():
	# Read the current switch state to pass to the template.
	temp = sensor_thing.read_temp()
	return render_template('index.html', temp=temp)

    

@app.route("/update")
def updates():
    def UpdatesValues():
        while True:
        	#temp = sensor_thing.read_temp()
             # Build up a dict of the current thing state.
            temp_state = {
                'temperature': sensor_thing.read_temp()
            }
            yield('data: {0}\n\n'.format(json.dumps(temp_state)))
            time.sleep(1.0)
    return Response(UpdatesValues(), mimetype='text/event-stream')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=50, debug=True, threaded=True)

