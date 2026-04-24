import pandas as pd
import os

EVENTS_CSV = os.path.join('data', 'events.csv')

def create_event(name, description=""):
    """
    Adds a new event to data/events.csv.
    """
    if not os.path.exists('data'):
        os.makedirs('data')

    new_data = {
        'name': [name],
        'description': [description]
    }
    df_new = pd.DataFrame(new_data)
    
    if os.path.exists(EVENTS_CSV):
        df_events = pd.read_csv(EVENTS_CSV)
        if name in df_events['name'].values:
            return False, f"Error: Event '{name}' already exists."
        df_new.to_csv(EVENTS_CSV, mode='a', header=False, index=False)
    else:
        df_new.to_csv(EVENTS_CSV, index=False)
    
    return True, f"Event '{name}' created successfully!"

def list_events():
    """
    Returns a list of all event names.
    """
    if not os.path.exists(EVENTS_CSV):
        return []
    
    df = pd.read_csv(EVENTS_CSV)
    return df['name'].tolist()
