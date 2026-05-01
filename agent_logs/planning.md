Task: Plan the data schema before coding 
Prompt: "For each CSV the system writes, list the columns, types, and which module reads vs. writes it. Files: attendance_log.csv, events.csv ,event_log.csv."
Result: Schema table — e.g. attendance_log.csv: name, email, face_path, check_in_time written by enroll.py/utils.py, read by recognize.py. 
Human Action: Locked the schema in before asking for code so all modules used consistent column names.

Task: Plan the user-facing workflows 
Prompt: "List the end-to-end user flows this system needs to support (enrollment, event creation, event check-in, etc).
Result: Flow diagrams like Event Check-in: main.py → events.list_events() → recognize.find_match() → utils.load_face_data() → attendance.record_event_checkin() → write event_log.csv. 
Human Action: Used the flows to decide the six menu options and confirm every flow had a clear success/failure path before writing code.