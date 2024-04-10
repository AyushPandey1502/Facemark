import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://faceattendancerealtime-66384-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing":'G',
            "year":4,
            "last_attendance_time": "2023-10-21 00:54:34"
        },
    "852741":
        {
            "name": "Emily Blunt",
            "major": "Economics",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing":'B',
            "year":4,
            "last_attendance_time": "2023-10-21 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing":'G',
            "year":2,
            "last_attendance_time": "2023-10-21 00:54:34"
        },
    "150502":
        {
            "name": "Ayush Pandey",
            "major": "CSE Core",
            "starting_year": 2022,
            "total_attendance": 6,
            "standing":'G',
            "year":2,
            "last_attendance_time": "2023-10-21 00:54:34"
        },
    "116765":
        {
            "name": "Rahul Pratap Singh",
            "major": "IT",
            "starting_year": 2022,
            "total_attendance": 6,
            "standing":'B',
            "year":2,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
    "112345":
        {
            "name": "Anikait Agarwal",
            "major": "IT",
            "starting_year": 2022,
            "total_attendance": 6,
            "standing":'A',
            "year":2,
            "last_attendance_time": "2023-11-04 08:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)
