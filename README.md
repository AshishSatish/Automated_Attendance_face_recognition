# 🔐 Face Recognition Attendance System

A Python-based face recognition attendance system using OpenCV, face_recognition, and Firebase Realtime Database.

---

## 📁 Project Structure

```
├── Images/                   # Folder containing student face images (e.g., 123.png)
├── Resources/
│   ├── background.png        # Main UI background
│   └── Modes/                # UI images for different modes (0.png, 1.png, ...)
├── EncodeGenerator.py        # Script to generate face encodings
├── AddDatatoDatabase.py      # Script to add student data to Firebase
├── Main.py                   # Main attendance recognition script
├── serviceAccountKey.json    # 🔒 Your Firebase service account credentials (do NOT upload this)
├── README.md                 # Setup & usage guide
```

---

## 🧰 Requirements

Install the following Python libraries:

```bash
pip install opencv-python face-recognition firebase-admin cvzone numpy
```

---

## 🔧 Setup Instructions

### 1. Firebase Project Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project.
3. Go to **Build > Realtime Database** and click **Create Database** (start in test mode).
4. Navigate to **Project Settings > Service Accounts**.
5. Click **Generate New Private Key** and download `serviceAccountKey.json`.
6. Move `serviceAccountKey.json` to the root folder of this project.

### 2. Update Firebase Config

In all Python files that use Firebase (like `Main.py`, `AddDatatoDatabase.py`), update:

```python
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://<your-database-name>.firebaseio.com"
})
```

Replace `<your-database-name>` with your actual Firebase DB URL.

---

## 🖼️ Add Student Images

- Place front-facing student images into the `Images/` folder.
- File names should follow this format: `StudentID.png`  
  _Example: `12345.png`_

---

## 🧬 Generate Encodings

Run the following command to encode the student faces:

```bash
python EncodeGenerator.py
```

It will generate `EncodeFile.p` which is used by the main attendance system.

---

## 📊 Add Student Data to Firebase

Run the following command to upload student details to Firebase:

```bash
python AddDatatoDatabase.py
```

Edit this file to include the relevant student info.

---

## 🚀 Run the Attendance System

Start the system with:

```bash
python Main.py
```

- A GUI window will open showing live webcam feed and attendance status.
- Press **`q`** to quit the application.
- If using an external webcam, update:

```python
cv2.VideoCapture(0)
```

to

```python
cv2.VideoCapture(1)
```

---

## ➕➖ Add or Remove Students

### To **Add** a Student:
- Add their image to `Images/`
- Add their details in `AddDatatoDatabase.py`
- Run:
  ```bash
  python EncodeGenerator.py
  python AddDatatoDatabase.py
  ```

### To **Remove** a Student:
- Delete their image from `Images/`
- Remove their record from Firebase manually
- Run:
  ```bash
  python EncodeGenerator.py
  ```

---

## 🛡️ .gitignore Recommendation

Create a `.gitignore` file and add:

```
serviceAccountKey.json
EncodeFile.p
```

So sensitive files are not pushed to GitHub.

---

## 💡 Tips

- Use clear, well-lit images for better accuracy.
- Adjust webcam index if needed.
- Use smaller input image sizes (via resizing) to improve performance.

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests.

---

## 👨‍💻 Author

**Ashish Bhosale**  
GitHub: [@your-username](https://github.com/your-username)

---

## 📜 License

This project is licensed under the **MIT License**.
