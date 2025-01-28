
# ePortfolio for Programmers

This project is an ePortfolio for programmers, showcasing their skills and projects using various technologies. The application is built with a combination of HTML, CSS, Python, Django, React, SQL, Docker, and Jinja2.


## Distinctiveness and Complexity

This ePortfolio project stands out due to its integration of multiple modern technologies and frameworks, making it a comprehensive and complex application. The use of Django and React together provides a robust backend and a dynamic frontend, while Docker ensures easy deployment and scalability. The project also includes user authentication, profile management, and a responsive design, which add to its complexity and make it a valuable tool for showcasing programming skills.


## Technologies Used

- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **Python**: For backend development.
- **Django**: As the web framework for the backend.
- **React**: For building the frontend user interface.
- **SQL**: For database management.
- **Docker**: For containerization and deployment.
- **Jinja2**: For templating in Django.

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
    pip install -r requirements.txt
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
