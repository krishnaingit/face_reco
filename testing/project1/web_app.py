from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Attendance
import face_recognition
import numpy as np
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['UPLOAD_FOLDER'] = 'known_faces'
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    attendances = Attendance.query.order_by(Attendance.timestamp.desc()).all()
    return render_template('index.html', attendances=attendances)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        roll_number = request.form['roll_number']
        image = request.files['image']
        
        # Save image
        filename = f"{roll_number}.jpg"
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)
        
        # Create face encoding
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        
        if len(encodings) == 0:
            os.remove(image_path)
            return "No face detected. Please try again."
            
        face_encoding = encodings[0].tobytes()
        
        # Save to database
        new_user = User(
            username=username,
            roll_number=roll_number,
            image_path=image_path,
            face_encoding=face_encoding
        )
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)