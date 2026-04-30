Task: Build the enrollment module 
Prompt: "Write a Python function enroll_user(name, email, image_path) for [enroll.py](file:///Users/chadbernstein/Downloads/project/face_attendance_project/src/enroll.py). Use the face_recognition library to validate the image contains exactly one face. Reject images with zero or multiple faces. Copy valid images into data/faces/ with a unique filename based on name+email, then call add_user_to_csv from utils. Return a (success: bool, message: str) tuple." 
Result: Function with face_locations validation, shutil.copy2 for image storage, and try/except wrapping the whole flow. 
Human Action: Tested with a single-face photo, a no-face landscape, and a group photo to confirm all three branches worked. Verified the file appeared in data/faces/.


Task: Build the interactive CLI 
Prompt: "Write [main.py](file:///Users/chadbernstein/Downloads/project/face_attendance_project/src/main.py) with a menu loop offering: enroll, create event, check-in to event, quick check-in, list events, exit. Wire each option to the existing modules (enroll, recognize, attendance, events). Use plain input() prompts." 
Result: A while True loop with if/elif branches for choices 1–6. 
Human Action: Ran end-to-end: enrolled a user, created an event, checked in. Verified all CSVs updated correctly.