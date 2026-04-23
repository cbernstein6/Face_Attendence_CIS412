from datetime import datetime
from utils import update_check_in_time

def record_checkin(user_email):
    """
    Logs a successful check-in with the current timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    success = update_check_in_time(user_email, timestamp)
    if success:
        return True, f"Check-in successful at {timestamp}"
    return False, "Error updating attendance log."
