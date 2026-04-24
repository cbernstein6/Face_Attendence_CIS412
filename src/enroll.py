import os
import shutil
import face_recognition
from utils import add_user_to_csv

def enroll_user(name, email, image_path):
    """
    Validates a face image, copies it to data/faces, and adds user to CSV.
    """
    if not os.path.exists(image_path):
        print("Current directory:", os.getcwd())
        return False, f"Error: Image file not found: {image_path}"

    try:
        # Validate that exactly one face is present
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        
        if len(face_locations) == 0:
            return False, "Error: No face detected in the provided image."
        if len(face_locations) > 1:
            return False, "Error: Multiple faces detected. Please provide an image with only one face."

        # Ensure data/faces directory exists
        faces_dir = os.path.join('data', 'faces')
        if not os.path.exists(faces_dir):
            os.makedirs(faces_dir)

        # Generate a unique filename for the face image
        ext = os.path.splitext(image_path)[1]
        new_filename = f"{name.replace(' ', '_')}_{email.replace('@', '_')}{ext}"
        new_path = os.path.join(faces_dir, new_filename)

        # Copy image to faces directory
        shutil.copy2(image_path, new_path)

        # Add to CSV
        add_user_to_csv(name, email, new_path)
        
        return True, f"Successfully enrolled {name}!"
        
    except Exception as e:
        return False, f"An error occurred during enrollment: {str(e)}"
