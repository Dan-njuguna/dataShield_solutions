# DataShield Solutions

DataShield Solutions bridges the gap between your data interactions and their legal implications, helping you monitor compliance with Kenya's Data Protection Act.

## Features

- Analytics for compliance.
- User and company audits.
- Compliance state management.
- User policy terms management.

## Key Components

- User authentication and login.
- Audit logging.
- Data processing for audits and analytics.
- Compliance reporting.

## Usage

1. Compliance auditing.
2. Compliance history analytics.
3. Compliance reports.

## App Versioning

- Initial version: `0.1.0`. Updates will follow as we improve and optimize the application.

## Technology Stack

- **Backend**: Django
- **Frontend**: React
- **Containerization**: Docker

## Setting Up the Environment

To set up and run the application, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Dan-njuguna/dataShield_solutions.git
    cd dataShield_solutions
    ```

2. **Build and run the Docker containers**:
    ```sh
    docker-compose up --build
    ```

3. **Access the application**:
    - Frontend: `http://localhost:3000`
    - Backend API: `http://localhost:8000`

> Note: The Docker setup creates separate containers for the frontend and backend, allowing them to interact seamlessly.

## Additional Notes

- Ensure Docker and Docker Compose are installed on your machine.
- The Docker setup handles the installation of all necessary dependencies for both the frontend and backend.
