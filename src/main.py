import os
import sys
from enroll import enroll_user
from recognize import find_match
from attendance import record_event_checkin, record_checkin
from events import create_event, list_events

def print_menu():
    print("\n--- Face Attendance System ---")
    print("1. Create New User (Enroll)")
    print("2. Create New Event")
    print("3. Check-in for an Event")
    print("4. Quick Check-in (General)")
    print("5. List Events")
    print("6. Exit")
    return input("Select an option: ")

def main():
    while True:
        choice = print_menu()

        if choice == '1':
            name = input("Enter full name: ")
            email = input("Enter email address: ")
            image_path = input("Enter path to face image: ")
            success, message = enroll_user(name, email, image_path)
            print(message)

        elif choice == '2':
            event_name = input("Enter event name: ")
            description = input("Enter event description (optional): ")
            success, message = create_event(event_name, description)
            print(message)

        elif choice == '3':
            events = list_events()
            if not events:
                print("No events found. Please create an event first.")
                continue
            
            print("\nAvailable Events:")
            for i, event in enumerate(events, 1):
                print(f"{i}. {event}")
            
            try:
                event_choice = int(input("Select event number: "))
                if 1 <= event_choice <= len(events):
                    selected_event = events[event_choice - 1]
                    image_path = input("Enter path to current photo for check-in: ")
                    
                    print("Recognizing face...")
                    user, error = find_match(image_path)
                    
                    if error:
                        print(error)
                    elif user:
                        print(f"Match found: {user['name']} ({user['email']})")
                        success, log_msg = record_event_checkin(user['email'], user['name'], selected_event)
                        print(log_msg)
                    else:
                        print("Access Denied: Face not recognized.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            image_path = input("Enter path to current photo for general check-in: ")
            print("Recognizing face...")
            user, error = find_match(image_path)
            
            if error:
                print(error)
            elif user:
                print(f"Match found: {user['name']} ({user['email']})")
                success, log_msg = record_checkin(user['email'])
                print(log_msg)
            else:
                print("Access Denied: Face not recognized.")

        elif choice == '5':
            events = list_events()
            if events:
                print("\nEvents:")
                for event in events:
                    print(f"- {event}")
            else:
                print("No events found.")

        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
