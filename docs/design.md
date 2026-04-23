This project should be for an event check-in. The project will be divided into:
enrollment - system for users to register their face on the app, a user uploads a picture file and it is assigned to them

sign-in module - System for users to register on website for check-in. If the uploaded photo matches their picture in the system, this will send the success over to attendence module. Otherwise it will just deny the user entry. This will be used for each different event as a "check-in" for when someone arrives

event module - This will write to local csv to show that a user is checked in. I will store user's name, email, face picture in the csv.

Entry point - Different python scripts/files will serve functions to fulfill all required systems. For instance, There will be an enroll file which adds a user to the system.


AI Usage:
Gemini will write all code for this project, I will handle the design and layout of the project. I will prompt it for simple modules that fulfill the requirements. 
The ai agent will make the project work as simply as possible (writing in small code chunks, each module separately), and I'll verify that the code is acceptable through constant manual testing.


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