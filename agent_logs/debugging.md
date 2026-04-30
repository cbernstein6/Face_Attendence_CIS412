Task: Fix check_in_time showing as nan or 0.0 
Prompt: "When I update check_in_time in attendance_log.csv, pandas reads existing empty values as NaN (float) and writes them back as 0.0. The column should stay as a string timestamp. Fix utils.py so the CSV always reads/writes that column as text." 
Result: Added dtype={'check_in_time': str} to pd.read_csv in load_face_data and dtype=str in update_check_in_time. 
Human Action: Re-ran a check-in and confirmed the CSV showed a clean YYYY-MM-DD HH:MM:SS string instead of 0.0.

Task: Fix duplicate event entries Prompt: "create_event in events.py lets the same event name be added twice. Before appending, read the CSV and reject the request if name already exists. Return (False, error_message) in that case." 
Result: Added a pd.read_csv + if name in df['name'].values check before the append. 
Human Action: Tried creating "Hackathon 2026" twice; second attempt was correctly rejected.