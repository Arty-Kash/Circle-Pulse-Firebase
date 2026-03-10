import os
import time
import math
from flask import Flask, send_file, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/api/color_data")
def get_color_data():
    """Generates a color that changes smoothly over time."""
    # Get the current time in seconds
    current_time = time.time()

    # Use sine waves with different frequencies to get smooth color transitions
    # The division by a number (e.g., 5, 7, 11) controls the speed of the color change.
    red = int(127 * math.sin(current_time / 5) + 128)
    green = int(127 * math.sin(current_time / 7) + 128)
    blue = int(127 * math.sin(current_time / 11) + 128)

    # Format as a hex color string
    color = f'#{red:02x}{green:02x}{blue:02x}'

    return jsonify(color=color, timestamp=current_time)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
