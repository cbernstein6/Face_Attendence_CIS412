# Face Attendance Project

A simple CLI-based event check-in system using face recognition and CSV storage.

## Features
- **Enrollment**: Register users by providing their name, email, and a face image.
- **Check-in**: Log attendance by providing a current photo of a user. The system matches the photo against enrolled users and records the check-in time in a CSV.

## Requirements
- Python 3.14 (or compatible)
- `face_recognition`
- `pandas`
- `opencv-python`
- `setuptools < 82.0.0` (required for `pkg_resources` compatibility)

## Installation
It is recommended to use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install "setuptools<82.0.0"
```
source venv/bin/activate
## Usage

### Enroll a User
```bash
python3 src/entry.py enroll "John Doe" "john@example.com" "data/faces/User_One_user1_example.com.png"
```
This will:
1. Validate that exactly one face is in the image.
2. Copy the image to `data/faces/`.
3. Add a row to `data/attendance_log.csv`.

### Check-in a User
```bash
python3 src/entry.py checkin "data/faces/User_One_user1_example.com.png"
```
This will:
1. Scan the photo for a face.
2. Match it against all enrolled users.
3. If a match is found, update the `check_in_time` for that user in `data/attendance_log.csv`.

## Data Storage
- **CSV Path**: `data/attendance_log.csv`
- **Columns**: `name`, `email`, `face_path`, `check_in_time`
- **Faces Directory**: `data/faces/`
