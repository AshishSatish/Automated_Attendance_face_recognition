# 🔐 Face Recognition Attendance System

A Python-based face recognition attendance system using OpenCV, face_recognition, and Firebase Realtime Database.

---

## 📁 Project Structure

├── Images/ # Folder containing student face images (e.g., 123.png)
├── Resources/
│ ├── background.png # Main UI background
│ └── Modes/ # UI images for different modes (0.png, 1.png, ...)
├── EncodeGenerator.py # Script to generate face encodings
├── AddDatatoDatabase.py # Script to add student data to Firebase
├── Main.py # Main attendance recognition script
├── serviceAccountKey.json # 🔒 Your Firebase service account credentials (should NOT be uploaded)
├── README.md # Setup & usage guide

yaml
Copy
Edit

---

## 🧰 Requirements

Install the following libraries:

```bash
pip install opencv-python face-recognition firebase-admin cvzone numpy
🔧 Setup Instructions
1. Firebase Project Setup
Go to Firebase Console.

Create a new project.

Navigate to Build > Realtime Database and click Create Database (start in test mode).

Navigate to Project Settings > Service Accounts tab.

Click Generate New Private Key and download serviceAccountKey.json.

Place serviceAccountKey.json in your project root folder (add it to .gitignore).

2. Update Firebase Configuration
Update the following line in your Python files (Main.py, etc.):

python
Copy
Edit
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://<your-database-name>.firebaseio.com"
})
Replace <your-database-name> with your actual Firebase Realtime DB URL.

🖼️ Add Student Images
Save clear, front-facing images of students in the Images/ folder.

File format: <student_id>.png (e.g., 321654.png, 963852.png)

🧬 Generate Encodings
Run:

bash
Copy
Edit
python EncodeGenerator.py
This will create EncodeFile.p containing face encodings for all students.

📊 Add Student Data to Firebase
Run:

bash
Copy
Edit
python AddDatatoDatabase.py
This will push student metadata (name, year, major, etc.) to Firebase under /Students/<student_id>.

🚀 Run the Attendance System
Launch the main app with:

bash
Copy
Edit
python Main.py
Press q to quit.

Make sure your webcam is connected.

If using external webcam, change cv2.VideoCapture(0) to cv2.VideoCapture(1) if needed.

✅ To Add or Remove Students
To Add:

Add new image to Images/ folder.

Update AddDatatoDatabase.py with the new student's data.

Rerun EncodeGenerator.py and AddDatatoDatabase.py.

To Remove:

Delete the image from Images/

Remove the student data from Firebase

Rerun EncodeGenerator.py

🛡️ .gitignore Recommendation
Make sure to exclude sensitive files like keys:

pgsql
Copy
Edit
serviceAccountKey.json
EncodeFile.p
💡 Tips
Use well-lit, frontal face images for better accuracy.

Add a delay (e.g., 30+ seconds) between repeated detections of the same person.

