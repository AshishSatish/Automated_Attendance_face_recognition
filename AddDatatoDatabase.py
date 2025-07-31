import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://automated-attendance-691c3-default-rtdb.firebaseio.com"  
})

ref = db.reference('Students')

data = {
    "122B1F011":
        {
            "name": "Ashish Bhosale",
            "major": "Information Technology",
            "starting_year": 2022,
            "total_attendance": 0,
            "Division": "A",
            "year": 4,
            "last_attendance_time": "2025-07-18 00:54:34",
            "attendance_log": []
        },
    "122B1F041":
        {
            "name": "Shreyas Jawale",
            "major": "Information Technology",
            "starting_year": 2022,
            "total_attendance": 0,
            "Division": "A",
            "year": 4,
            "last_attendance_time": "2025-07-18 00:54:34",
            "attendance_log": []
        },
    "122B1F023":
        {
            "name": "Ritesh Dudhade",
            "major": "Information Technology",
            "starting_year": 2022,
            "total_attendance": 0,
            "Division": "B",
            "year": 4,
            "last_attendance_time": "2025-07-18 00:54:34",
            "attendance_log": []
        },
    "122B1F005":
        {
            "name": "Sankalp Banginwar",
            "major": "Computer Science",
            "starting_year": 2022,
            "total_attendance": 0,
            "Division": "A",
            "year": 4,
            "last_attendance_time": "2025-07-18 00:54:34",
            "attendance_log": []
        },
    "122B1F004":
        {
            "name": "Sushil Bang",
            "major": "Computer Science",
            "starting_year": 2022,
            "total_attendance": 0,
            "Division": "B",
            "year": 4,
            "last_attendance_time": "2025-07-18 00:54:34",
            "attendance_log": []
        },
    "122B1F002":
        {
            "name": "Abhinandan Ashtekar",
            "major": "Information Technology",
            "starting_year": 2022,
            "total_attendance": 0,
            "Division": "B",
            "year": 4,
            "last_attendance_time": "2025-07-18 00:54:34",
            "attendance_log": []
        },
    "123B1B024":
        {
            "name": "Atharv Rao",
            "major": "Computer Science",
            "starting_year": 2023,
            "total_attendance": 0,
            "Division": "A",
            "year": 3,
            "last_attendance_time": "2025-07-18 00:54:34",
            "attendance_log": []
        },
    "122B1F016":
        {
            "name": "Harshal Chavan",
            "major": "Information Technology",
            "starting_year": 2022,
            "total_attendance": 0,
            "Division": "A",
            "year": 4,
            "last_attendance_time": "2025-07-18 00:54:34",
            "attendance_log": []
        }
    
}

for key, value in data.items():
    ref.child(key).set(value)
