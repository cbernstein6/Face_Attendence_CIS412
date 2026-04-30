Task: Plan the data schema before coding 
Prompt: "For each CSV the system writes, list the columns, types, and which module reads vs. writes it. Files: attendance_log.csv (users + last check-in), events.csv (event catalog), event_log.csv (per-event check-ins)." 
Result: Schema table — e.g. attendance_log.csv: name, email, face_path, check_in_time written by enroll.py/utils.py, read by recognize.py. 
Human Action: Locked the schema in before asking for code so all modules used consistent column names.

Task: Plan the user-facing workflows 
Prompt: "List the end-to-end user flows this system needs to support (enrollment, event creation, event check-in, quick check-in, listing events). For each, write the step-by-step sequence of module calls and CSV reads/writes. I'll use this to design the menu in main.py." 
Result: Flow diagrams like Event Check-in: main.py → events.list_events() → recognize.find_match() → utils.load_face_data() → attendance.record_event_checkin() → write event_log.csv. 
Human Action: Used the flows to decide the six menu options and confirm every flow had a clear success/failure path before writing code.