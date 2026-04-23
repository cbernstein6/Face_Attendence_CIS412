# Quick Start Guide

### 1. Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install "setuptools<82.0.0"
```
source venv/bin/activate

### 2. Enroll a User
python3 src/entry.py enroll "John Doe" "john@example.com" "data/faces/User_One_user1_example.com.png"

### 3. Check-in a User
python3 src/entry.py checkin "data/faces/User_One_user1_example.com.png"
