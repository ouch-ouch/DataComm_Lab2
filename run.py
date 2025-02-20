from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def current_time():
    # Set timezone to New York
    nyc_tz = pytz.timezone('America/New_York')
    # Get the current time in UTC and convert to NYC time
    now = datetime.now(nyc_tz)
    return now.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)
