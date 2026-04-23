import pandas as pd
import face_recognition
import os

CSV_PATH = os.path.join('data', 'attendance_log.csv')

def load_face_data():
    """
    Loads face images from paths specified in data/attendance_log.csv.
    Returns a list of dictionaries with 'name', 'email', 'face_path', and 'encoding'.
    """
    if not os.path.exists(CSV_PATH):
        return []

    try:
        # Explicitly read check_in_time as string to avoid float inference
        df = pd.read_csv(CSV_PATH, dtype={'check_in_time': str})
    except pd.errors.EmptyDataError:
        return []

    face_data = []
    for _, row in df.iterrows():
        name = str(row['name'])
        email = str(row['email'])
        path = str(row['face_path'])
        
        if os.path.exists(path):
            try:
                image = face_recognition.load_image_file(path)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    face_data.append({
                        'name': name,
                        'email': email,
                        'face_path': path,
                        'encoding': encodings[0]
                    })
            except Exception as e:
                print(f"Warning: Could not load face for {name}: {e}")
    return face_data

def add_user_to_csv(name, email, face_path):
    """
    Adds a new user to the CSV file.
    """
    new_data = {
        'name': [name],
        'email': [email],
        'face_path': [face_path],
        'check_in_time': ['']
    }
    df_new = pd.DataFrame(new_data)
    
    if os.path.exists(CSV_PATH):
        df_new.to_csv(CSV_PATH, mode='a', header=False, index=False)
    else:
        df_new.to_csv(CSV_PATH, index=False)

def update_check_in_time(email, timestamp):
    """
    Updates the check_in_time for a user identified by email.
    """
    if not os.path.exists(CSV_PATH):
        return False
    
    # Read as string to avoid type issues
    df = pd.read_csv(CSV_PATH, dtype=str)
    if email in df['email'].values:
        df.loc[df['email'] == email, 'check_in_time'] = timestamp
        df.to_csv(CSV_PATH, index=False)
        return True
    return False
