
# ePortfolio for Programmers

This project is an ePortfolio for programmers, showcasing their skills and projects using various technologies. The application is built with a combination of HTML, CSS, Python, Django, React, SQL, Docker, and Jinja2.

# Specification

The ePortfolio web application will serve as a personal showcase for users to display their projects, skills, and experiences. The application will be built using Django on the back-end and JavaScript on the front-end, ensuring a dynamic and responsive user experience. Below are the key specifications:

User Authentication:
Users must be able to create an account, log in, and log out.
Password reset functionality must be implemented.

Profile Management:
Users can create and edit their profiles, including personal information such as name, bio, contact details, and profile picture.
Users can manage their project listings.

Project Listings:
Users can add new projects with details including title, description, technologies used, links to live demos or repositories (e.g., GitHub), and images/screenshots.
Users can edit or delete existing projects.

Responsive Design:
The application must be mobile-responsive to ensure usability across various devices.

Search Functionality:
Implement a search feature that allows users to find specific projects based on keywords or tags.

Admin Panel:
An admin interface should allow superusers to manage users and projects effectively.

Database Structure:
Utilize Django models to define the database schema for users and projects.

User Model: 
Extends Django's AbstractUser class.

Project Model: 
Contains fields for title, description, technologies used, user reference (foreign key), etc.

Deployment:
The application should be deployable on platforms like Heroku or DigitalOcean with proper environment variable management.

## Distinctiveness and Complexity

This ePortfolio project stands out due to its integration of multiple modern technologies and frameworks, making it a comprehensive and complex application. The use of Django and React together provides a robust backend and a dynamic frontend, while Docker ensures easy deployment and scalability. The project also includes user authentication, profile management, and a responsive design, which add to its complexity and make it a valuable tool for showcasing programming skills.


## File Description

- **Dockerfile**: The Docker file that contains the Docker configuration for this project and its dependencies.
- **docker-compose.yml**: The Docker Compose file that defines the services, networks, and volumes for the application.
- **requirements.txt**: This file lists all the Python dependencies required for the project, including Django, djangorestframework, psycopg2, and other necessary packages.
- **selenium/tests.py**: This file contains automated tests for the application using Selenium. It includes test cases for various functionalities such as user authentication, profile management, and project showcase. The tests ensure that the web application behaves as expected and helps in identifying any issues or bugs in the code.
- **templates**: This file contains the templates for the ePortfolio application.


## Technologies Used

- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **Python**: For backend development.
- **Django**: As the web framework for the backend.
- **React**: For building the frontend user interface.
- **SQL**: For database management.
- **Docker**: For containerization and deployment.
- **Jinja2**: For templating in Django.
- **Bootstrap**: For responsive design and pre-built components.


## Features

- User authentication and authorization
- Profile creation and management
- Project showcase with descriptions and links
- Skill listing and endorsements
- Responsive design for mobile and desktop
- Containerized deployment with Docker


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/samurai25/capstone
    cd capstone
    ```

2. Set up the virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install --no-cache-dir -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python3 manage.py migrate
    ```

5. Run the development server:
    ```bash
    python3 manage.py runserver
    ```

6. Open your browser and navigate to `http://localhost:8000`.


## Docker Deployment

1. Build and start the containers:
    ```bash
    docker-compose up --build
    ```
2. Open your browser and navigate to `http://localhost:8000`.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [script062@gmail.com](mailto:script062@gmail.com).
