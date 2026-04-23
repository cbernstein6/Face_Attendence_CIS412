import face_recognition
import os
from utils import load_face_data

def find_match(checkin_image_path):
    """
    Loads an image, gets its face encoding, and compares it against all enrolled users.
    Returns the user data if a match is found, otherwise None.
    """
    if not os.path.exists(checkin_image_path):
        return None, f"Error: Check-in image not found: {checkin_image_path}"

    try:
        checkin_image = face_recognition.load_image_file(checkin_image_path)
        checkin_encodings = face_recognition.face_encodings(checkin_image)

        if not checkin_encodings:
            return None, "Error: No face detected in check-in image."

        checkin_encoding = checkin_encodings[0]
        enrolled_users = load_face_data()

        if not enrolled_users:
            return None, "Error: No users enrolled in the system."

        # Compare check-in face with all enrolled faces
        known_encodings = [user['encoding'] for user in enrolled_users]
        matches = face_recognition.compare_faces(known_encodings, checkin_encoding)

        if True in matches:
            first_match_index = matches.index(True)
            return enrolled_users[first_match_index], None
        
        return None, "Access Denied: Face not recognized."
    except Exception as e:
        return None, f"An error occurred during recognition: {str(e)}"
