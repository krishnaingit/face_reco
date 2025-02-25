Part 1: Face Recognition System
Required Libraries:
pip install face-recognition opencv-python numpy pandas

Code (face_recognition.py):

Explanation:
Loads known faces from known_faces directory

Uses webcam to detect faces in real-time

Compares detected faces with known faces

Marks attendance in CSV file

Displays live video feed with recognition results


Part 2: Web Interface (Full Stack)
Required Libraries:

pip install flask pandas

Directory Structure:

project/
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── face_recognition.py
├── web_app.py
├── attendance.csv
└── known_faces/

1. Flask Backend (web_app.py):
2. HTML Template (templates/index.html):
3. CSS (static/style.css):
Explanation:
    Flask server reads CSV data
    HTML template displays data in a table
    Uses Bootstrap for styling
    Auto-refreshes data on page reload

How to Use:
    1.Create known_faces directory and add student photos (name.jpg/png)

    2.Run face recognition system:
        python face_recognition.py

    3.In another terminal, run web server:
        python web_app.py

    4.Access website at http://raspberrypi-local-ip:5000



Important Notes:
   1. Raspberry Pi Setup:

        Enable camera interface in raspi-config

        Use good lighting for better recognition

        Keep students' faces clear in reference images

   2. Performance Tips:

        Reduce video resolution in video_capture = cv2.VideoCapture(0) to 640x480

        Use smaller reference images (200x200 pixels)

   3. Security:

        Change default Raspberry Pi password

        Only use on local network

    4. Storage Management:

        Regularly backup attendance.csv

        Clean up old reference images when needed

    This system provides a basic framework that you can enhance with features like:

    Real-time website updates (using WebSocket)

    Multiple face detection improvements

    Export functionality

    User authentication