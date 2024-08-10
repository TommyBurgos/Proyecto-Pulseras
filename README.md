# Project-Wristbands

## Project Description
This project aims to develop a patient monitoring system using WiFi wristbands. The system includes functionalities for managing patient data, monitoring vital signs, and providing real-time alerts. The project follows the SCRUM methodology for development and is deployed in a production environment.

## Features
- Real-time monitoring of vital signs.
- Patient data management.
- Configurable alerts.
- Web-based and mobile-friendly system.

## Repository Structure

The project is organized as follows:

```
📁 Project-Wristbands/
├── 📁 Communications/       # Folder containing all communication evidence with the client.
│   ├── README.md            # Index describing each communication file.
│   └── ...                  # Files for messages, emails, etc.
│
├── 📁 Documentation/        # Project-related documentation.
│   ├── user_manual.pdf      # User manual for the system.
│   ├── installation_guide.pdf # System installation guide.
│   └── project_report.pdf   # Complete project report.
│
├── 📁 Source Code/          # Source code of the project.
│   ├── 📁 myapp/            # Modules for the main application.
│   ├── 📁 user/             # User management module.
│   ├── 📁 static/           # Static files (CSS, JS, images).
│   ├── 📁 templates/        # HTML templates for the project.
│   └── manage.py           # Script for managing the Django project.
│
├── 📁 Test Evidence/        # Evidence of tests performed.
│   ├── test_cases.pdf       # Documented test cases.
│   └── test_results.xlsx    # Test results.
│
│
├── 📁 SCRUM Evidence/       # Evidence of SCRUM meetings and activities.
│   ├── sprint_planning.pdf  # Sprint planning documentation.
│   ├── daily_scrum_log.txt  # Daily Scrum meeting logs.
│   └── ...                  # Other SCRUM-related documents.
│
├── .gitignore               # Specifies files and directories to be ignored by Git.
├── README.md                # This file, providing an overview of the project.
├── requirements.txt         # List of dependencies required for the project.
└── LICENSE.md               # License information for the project.
```

### Folder and File Descriptions

- **Communications/**: Contains all evidence of communication with the client, such as emails, instant messages, etc. Includes a `README.md` file that serves as an index, describing each file in this folder.
  
- **Documentation/**: Includes important project documentation such as the user manual, installation guide, and the full project report in PDF format.

- **Source Code/**: Contains the source code of the project, organized into relevant modules. This includes the main application logic, user management, static files (like CSS, JavaScript, images), and HTML templates.

- **Test Evidence/**: Documents the test cases and results for the project. This folder includes a PDF of the test cases and an Excel file of the test results.

- **Deployment/**: Includes scripts and files necessary for deploying the system in a production environment. The `README.md` in this folder provides detailed instructions on how to deploy the system.

- **SCRUM Evidence/**: Contains documentation related to the SCRUM methodology used in the project. This includes sprint planning documents, daily Scrum logs, and other evidence of SCRUM activities.

- **.gitignore**: A file that specifies which files and directories Git should ignore, such as environment files, compiled code, or temporary files.

- **README.md**: The file you are reading now, providing a comprehensive overview of the project, its structure, and how to get started.

- **requirements.txt**: A text file listing all the Python dependencies needed to run the project. This can be installed using `pip`.

- **LICENSE.md**: Contains the licensing information for the project, detailing the terms under which the code can be used and modified.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/project-wristbands.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Access the system at [http://localhost:8000](http://localhost:8000)

## SCRUM Evidence
The project follows the SCRUM methodology. Evidence of meetings, planning, and sprint reviews is located in the `SCRUM Evidence` folder.

## User Guide
For more details on how to use the system, please refer to the [User Manual](./Documentation/user_manual.pdf).

## Deployment
The system is deployed in a production environment at [monitoreoDoc.pythonanywhere.com].

## Contributions
Contributions to this project are welcome. Please open an issue before submitting a pull request.

## Authors
This project was developed by Team T1, consisting of:
- Tommy Ruben Burgos Calle
- Genesis Gabriela Pacheco Reyes 
- Paula Gabriela Peralta Aguilar

## Additional Notes
For any questions or issues, please contact the team at [trburgos@espol.edu.ec].
