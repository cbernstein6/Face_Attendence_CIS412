import argparse
import sys
import os
from enroll import enroll_user
from recognize import find_match
from attendance import record_checkin

def main():
    parser = argparse.ArgumentParser(description="Face Attendance System CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Enroll command
    enroll_parser = subparsers.add_parser("enroll", help="Enroll a new user")
    enroll_parser.add_argument("name", help="Full name of the user")
    enroll_parser.add_argument("email", help="Email address of the user")
    enroll_parser.add_argument("image_path", help="Path to the user's face image")

    # Check-in command
    checkin_parser = subparsers.add_parser("checkin", help="Check in a user by matching their face")
    checkin_parser.add_argument("image_path", help="Path to the current photo for check-in")

    args = parser.parse_args()

    if args.command == "enroll":
        success, message = enroll_user(args.name, args.email, args.image_path)
        print(message)
        if not success:
            sys.exit(1)

    elif args.command == "checkin":
        print("Recognizing face...")
        user, error = find_match(args.image_path)
        
        if error:
            print(error)
            sys.exit(1)
            
        if user:
            print(f"Match found: {user['name']} ({user['email']})")
            success, log_msg = record_checkin(user['email'])
            print(log_msg)
            if not success:
                sys.exit(1)
        else:
            print("Access Denied: Face not recognized.")
            sys.exit(1)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
