import os
import pandas as pd
from datetime import datetime
from utils import update_check_in_time

EVENT_LOG_CSV = os.path.join('data', 'event_log.csv')

def record_checkin(user_email):
    """
    Logs a successful check-in with the current timestamp in the main user list.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    success = update_check_in_time(user_email, timestamp)
    if success:
        return True, f"Check-in successful at {timestamp}"
    return False, "Error updating attendance log."

def record_event_checkin(user_email, user_name, event_name):
    """
    Logs a check-in for a specific event in data/event_log.csv.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_data = {
        'event_name': [event_name],
        'user_name': [user_name],
        'user_email': [user_email],
        'timestamp': [timestamp]
    }
    df_new = pd.DataFrame(new_data)
    
    if os.path.exists(EVENT_LOG_CSV):
        df_new.to_csv(EVENT_LOG_CSV, mode='a', header=False, index=False)
    else:
        df_new.to_csv(EVENT_LOG_CSV, index=False)
        
    return True, f"Checked in {user_name} for '{event_name}' at {timestamp}"
