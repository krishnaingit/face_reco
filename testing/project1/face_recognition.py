import face_recognition
import cv2
import numpy as np
from models import db, User, Attendance
from datetime import datetime
from web_app import app

# Initialize with Flask context
with app.app_context():
    # Load all users
    users = User.query.all()
    known_face_encodings = [np.frombuffer(user.face_encoding) for user in users]
    known_face_data = [(user.username, user.roll_number) for user in users]

video_capture = cv2.VideoCapture(0)

def mark_attendance(user_id):
    with app.app_context():
        new_attendance = Attendance(user_id=user_id)
        db.session.add(new_attendance)
        db.session.commit()

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name, roll_number = known_face_data[best_match_index]
            mark_attendance(users[best_match_index].id)
            
            # Display user info on camera feed
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, f"{name} ({roll_number})", (left + 6, bottom - 6), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()