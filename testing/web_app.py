from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        data = pd.read_csv('attendance.csv')
        attendance = data.to_dict('records')
    except:
        attendance = []
    return render_template('index.html', attendance=attendance)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)