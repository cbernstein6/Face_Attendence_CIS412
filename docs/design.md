This project should be for an event check-in. The project will be divided into:
enrollment - system for users to register their face on the app, a user uploads a picture file and it is assigned to them

sign-in module - System for users to register for check-in. If the uploaded photo matches their picture in the system, this will send the success over to attendence module. Otherwise it will just deny the user entry. This will be used for each different event as a "check-in" for when someone arrives

Recognition module - uses recognize.py, which uses face_recognition library to determine whether a person is a match with anyone in the system

event file - This will write to local csv to show all events. This would be for an admin typically but we will allow all users to create an event for simplicity.

Main.py - This will serve as the entry point for the script, and will call all python files. This will be what users call in the terminal.


AI Usage:
Gemini will write all code for this project, I will handle the design and layout of the project. I will prompt it for simple modules that fulfill the requirements. 
The ai agent will make the project work as simply as possible (writing in small code chunks, each module separately), and I'll verify that the code is acceptable through constant and thorough manual testing. Ideally we'll have as little code as needed to keep the workflow as simple as possible.


Project Workflow Breakdown:
Project Architecture (By Human) – High-level design and module breakdown.
Enrollment Module (By AI) – Building file upload and storage functions.
Sign-in Module (By AI) – Creating face-matching logic.
Attendance Module (By AI) – Managing CSV read/write operations.
Entry Point Script (By Human + AI) – Wiring the modules together.
Prompting Strategy (By Human) – Defining constraints and instructions.
Manual Testing (By Human) – Verifying each file as it's generated.
Integration Testing (By Human) – Running the complete end-to-end flow.
Debugging & Fixing (By Human + AI) – Identifying bugs and regenerating code.
Final Review & Cleanup (By Human) – Polishing code and checking edge cases.