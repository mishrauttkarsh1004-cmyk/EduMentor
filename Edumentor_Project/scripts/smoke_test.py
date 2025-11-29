import requests, json
BASE="http://localhost:8000"
s = {"student_id":"s1","name":"Anshul","grade":8}
print("Register:", requests.post(BASE+"/register_student", json=s).text)
print("Generate lesson:", requests.post(BASE+"/generate_lesson", json={"student_id":"s1","topic":"Quadratic Equations","difficulty":"easy"}).json())
