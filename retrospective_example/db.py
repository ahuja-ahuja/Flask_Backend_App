from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



rooms = [{"id": "1", "room_name": "Team Orion", "user_id": "1", "password": "abcd123"},
                 {"id": "2", "room_name": "Team Apollo", "user_id": "1", "password": "abcd123456"},
                 {"id": "3", "room_name": "Team Discovery", "user_id": "2", "password": "abcd8875"}]

users = [
    {"email": "john.doe@example.com", "id": "1", "name": "John Doe", "password": "Demo1"},
    {"email": "karel.novak@example.com", "id": "2", "name": "Karel Novak", "password": "Demo2"},
]