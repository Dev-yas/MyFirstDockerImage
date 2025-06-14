from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    color1 = os.getenv("GRADIENT_COLOR_1", "#ff7e5f")
    color2 = os.getenv("GRADIENT_COLOR_2", "#feb47b")
    return render_template("index.html", color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
