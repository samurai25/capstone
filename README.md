
## ePortfolio for Programmers

This project is an ePortfolio for programmers, showcasing their skills and projects using various technologies. The application is built with a combination of HTML, CSS, Python, Django, React, SQL, Docker, and Jinja2.

## Distinctiveness and Complexity

Why My Project Satisfies the Distinctiveness and Complexity Requirements.
My ePortfolio project is sufficiently distinct from other projects in this course due to its unique combination of features, technology stack, and the purpose it serves. Unlike many traditional course projects, my ePortfolio is a dynamic web application designed to showcase my personal portfolio of work, while integrating several distinct and complex functionalities that demonstrate my technical skills and provide real value to users.

Unique Purpose and Scope
While some projects in the course may be simple websites or applications that perform similar functions, my ePortfolio goes beyond a basic website. It serves as both a showcase and a utility tool for prospective employers, clients, or collaborators to review my skills, experience, and the projects I have worked on. This purpose inherently makes it different from projects like social networks or e-commerce sites, which focus on user interaction in a generalized context. My ePortfolio is designed with personalization at its core, offering features that allow me to dynamically update the content and present it in a sophisticated, user-friendly interface.

Advanced Features and Technology Integration
The use of multiple technologies within my project sets it apart from simpler projects. Unlike a typical e-commerce site or social network, which might focus on basic user authentication and CRUD operations, my project utilizes the following technologies and features to enhance both the complexity and uniqueness of the platform:

Django and React Integration: The combination of Django as a backend framework and React for the frontend allows me to create a seamless, interactive user experience. Django serves as a robust framework for handling data models, user authentication, and dynamic content management, while React allows for a modern, responsive frontend with real-time interactions. This combination is not typical in basic e-commerce or social network projects.

Docker and Docker Compose: By incorporating Docker and Docker Compose, I have ensured that my project is containerized for development, testing, and deployment. This makes the application portable and easier to manage, which is a significant advancement over simpler projects that may not have the same deployment infrastructure.

SQL Database and Custom Data Models: Unlike most simple applications that rely on a fixed set of data, my ePortfolio integrates a custom SQL database that allows for the storage and management of my project details, personal information, and achievements. These elements can be dynamically updated or expanded as I progress in my career. Additionally, the use of complex data models such as many-to-many relationships between skills, projects, and categories adds to the complexity of the project.

Authentication and User Management: The integration of user authentication using Django's built-in user management system makes the project secure and functional for a potential multi-user environment, where different individuals might want to create their own personalized ePortfolio. This feature is not typically found in simpler projects.

Bootstrap and Jinja2 for Responsiveness and Templating: The integration of Bootstrap for responsive design ensures that the ePortfolio is usable across various devices, from mobile phones to desktops. Additionally, the use of Jinja2 templating for dynamic content rendering helps in creating a modular and maintainable frontend, which allows for future expansions and customization.

Customization Options for Future Users: Beyond just showcasing my own work, the ePortfolio is built with the flexibility to be easily adapted for other users. In the future, I plan to extend the project by adding features such as multiple user profiles, enabling others to create and manage their own portfolios within the same system.

Clear Distinction from Social Networks and E-Commerce Sites
Unlike a social network, which typically focuses on user interaction, communication, and content sharing, my ePortfolio serves a singular, focused purpose: displaying professional projects and achievements in a personalized manner. A social network would involve complex algorithms for friend connections, posts, and social interactions, which is not the goal of my ePortfolio. Similarly, while my project involves user authentication, it does not revolve around user-generated content or social engagement.

Additionally, my project is not an e-commerce site. E-commerce sites typically involve the listing and selling of products, with a focus on payment systems, inventory management, and user transactions. My ePortfolio, on the other hand, is a personal portfolio website with a focus on presenting my own work and achievements. Although it uses dynamic content management and incorporates user authentication, these features serve different purposes than in an e-commerce site. The system does not have any transactions, product listings, or financial features, which are core elements of e-commerce platforms.

Conclusion
In conclusion, my ePortfolio project is distinct from the other projects in this course because of its unique combination of features, technologies, and purpose. It goes beyond simple CRUD operations and static websites, providing a dynamic and scalable platform that integrates modern web development practices. By utilizing Django, React, Docker, SQL databases, and custom templating, I have created a project that demonstrates a higher level of complexity, customization, and technical skill, all while serving the purpose of showcasing my personal work in a professional and user-friendly way.


## Specification

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


## File Description
- capstone/.github/workflows/: Defines a GitHub Actions workflow for testing the application. Sets up Python, installs dependencies, and runs tests on push and pull request.
    ```yaml
    name: Testing
    on: [push, pull_request]

    jobs:
    build:
        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v2

        - name: Set up Python
        uses: actions/setup-python@v2
        with:
            python-version: '3.x'

        - name: Install dependencies
        run: |
            python -m pip install --upgrade pip
            pip install django
            pip install python-dotenv
            pip install django-cors-headers
            pip install Pillow

        - name: Run tests
        run: |
            python manage.py test

- capstone/capstone/templates/
    - **capstone**: a folder containing templates.
    - **registration**: a folder containing templates for registration.
    - **base.html**: a folder containing layouts for templates.
        ```html
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <title>{% block title %}ePortfolio{% endblock %}</title>
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <meta name="description" content="" />
                <script src="https://unpkg.com/react@17/umd/react.production.min.js" crossorigin></script>
                <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js" crossorigin></script>
                <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
                <link rel="stylesheet" type="text/css" href="{% static 'capstone/styles.css' %}">
            </head>
            <body>
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                    <a class="navbar-brand" href="{% url 'index' %}">ePortfolio</a>
                    <div>
                    <ul class="navbar-nav mr-auto">
                        {% if user.is_authenticated %}
                            <li class="nav-item">
                                <a class="nav-link" href="{% url 'capstone:profile' %}">
                                    <span style="font-weight: bold;">{{user.username}}</span>
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="about" href="{% url 'capstone:about' user.username %}">About</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" id="projects" href="{% url 'capstone:projects' user.username %}">Projects</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="contact" href="{% url 'capstone:contact' user.username %}">Contact</a>
                            </li>
                            <li class="nav-item">
                                <form class="nav-link" action="{% url 'logout' %}" method="post">
                                    {% csrf_token %}
                                    <button type="submit" id="logout" class="logout">Logout</button>
                                </form>
                            </li>
                        {% else %}
                            <li class="nav-item">
                                <a class="nav-link" id="login" href="{% url 'login' %}">Log In</a>
                            </li>
                            <li class="nav-item">
                                <div class="nav-link">or</div>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="register" href="{% url 'register' %}">Register</a>
                            </li>
                        {% endif %}
                    </ul>
                    </div>
                </nav>
                {% block content %}{% endblock %}
            </body>
        </html>

    - **index.html**: displays a homepage.
        ```html
        {% extends "base.html" %}
        {% block content %}
        {% if user.is_authenticated %}
            <div class="welcome">
                <div class="header">
                    <h2 id="username">Hello, {{ user.username }}!</h2>
                    <p>Thanks for logging in.</p>    
                </div>
            </div>
        {% else %}
            <div class="welcome">
                <div class="header">
                    <h2>
                        <p>Welcome! Please log in.</p> 
                    </h2>
                </div>
            </div>
        {% endif %}
        {% endblock %}


- capstone/capstone/templates/capstone/
    - **about.html**: displays a photo, bio, skills and certificates.
        ```html
        {% extends "base.html" %}
        {% load static %}
        {% block content %}

        <div class="header">
            <h2>About Me</h2>   
        </div>

        <div class="about">
            {% if profile %}
                <div>
                    {% if profile.profile_picture %}
                        <img src="{{ profile.profile_picture.url }}" alt="{{ profile.first_name }}">
                    
                    {% endif %}
                </div>
                <div class="bio">
                    <p>Hi, I'm {{profile.first_name}} {{profile.last_name}}, a {{profile.get_role_display}} from {{profile.country}}.</p>
                    <p>{{profile.bio}}</p>
                    <div class="skills">
                        <h4>My Skills</h4>
                        <ul>
                            {% if profile.frontend %}
                                <li><strong>Frontend: </strong>{{profile.frontend}}</li>
                            {% endif %}
                            {% if profile.backend %}
                                <li><strong>Backend: </strong>{{profile.backend}}</li>
                            {% endif %}
                            {% if profile.database %}
                                <li><strong>Databases: </strong>{{profile.database}}</li>
                            {% endif %}
                        </ul>
                        {% if certificates %}
                            <h4>Certificates: </h4>
                            <ul>
                                {% for certificate in certificates %}
                                    <li><strong>{{ certificate.url }}</strong></li>
                                {% endfor %}
                            </ul>
                        {% endif %}
                    </div>
                </div>
                
            {% endif %}
        </div>
        {% endblock %}

    - **add_project.html**: a form to add a project. 
        ```html
        {% extends "base.html" %}
        {% load static %}
        {% block content %}
        <div class="header">
            <h2>Add Project</h2>
        </div>

        <div class="form_container">
            <form method="post" action="" enctype="multipart/form-data">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit" id="add_project" class="btn btn-primary">Add</button>
            </form>
        </div>
        {% endblock %}

    - **contact.html**: displays contacts information.
        ```html
        {% extends "base.html" %}
        {% load static %}
        {% block content %}
            <div class="header">
                <h2>Contact</h2> 
            </div>

            <div class="contact_container">
                <p>For any inquiries or requests, please contact me at:</p>
                <div>
                    <ul>
                        <li><i class="bi bi-envelope" id="email"></i> {{ user.email }}</li>
                        {% if profile.github %}
                            <li><i class="bi bi-github" id="github"></i> {{profile.github}}</li>
                        {% endif %}
                        {% if profile.linkedin %}
                            <li><i class="bi bi-linkedin" id="linkedin"></i> {{profile.linkedin}}</li>
                        {% endif %}
                    </ul>   
                </div>
            </div>
        {% endblock %}

    - **edit_profile.html**: a form to edit a profile, add certificate links or delete certificate links.
        ```html
        {% extends "base.html" %}
        {% load static %}
        {% block content %}
        <div class="header">
        <h2>Edit Profile</h2>
        </div>

        <div class="form_container">
        <form method="post" action="" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form.as_p }} 
            <button type="submit" name="save_profile" id="save_profile" class="btn btn-primary">Save</button>
        </form>
        </div>

        <h3>Add a New Certificate</h3>
        <div class="form_container">    
            <form method="POST">
                {% csrf_token %}
                {{ certificate_form.as_p }}
                <button type="submit" name="add_certificate" class="btn btn-primary">Add Certificate</button>
            </form>
        </div>

        <h3>Your Certificates</h3>
        <div class="form_container">
        <ul class="list-group">
            {% for certificate in certificates %}
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <a href="{{ certificate.url }}" target="_blank">{{ certificate.url }}</a>
                    <form method="POST" class="d-inline">
                        {% csrf_token %}
                        <input type="hidden" name="certificate_id" value="{{ certificate.id }}">
                        <button type="submit" name="delete_certificate" class="btn btn-danger btn-sm">Delete</button>
                    </form>
                </li>
            {% empty %}
                <li class="list-group-item">No certificates added yet.</li>
            {% endfor %}
        </ul>
        </div>
        {% endblock %}

    - **edit_project.html**: a form to edit a project.
        ```html
        {% extends "base.html" %}
        {% load static %}
        {% block content %}
        <div class="header">
            <h2>Edit Project</h2>
        </div>

        <div class="form_container">
            <form method="post" action="" enctype="multipart/form-data">
                {% csrf_token %}
                {% if project %}
                    <p>Project: {{project.title}}</p>
                {% endif %}
                {{ form.as_p }}
                <button type="submit" id="save_project" class="btn btn-primary">Save</button>
            </form>
        </div>
        {% endblock %}

    - **error.html**: displays an error message.
        ```html
        {% extends "base.html" %}
        {% block content %}
            <div class="header">
                <h2>Error</h2>
                <h3><strong>You need to log in.</strong></h3>    
            </div>
        {% endblock %}

    - **profile.html**: displays the profile information.
        ```html
        {% extends "base.html" %}

        {% load static %}

        {% block content %}

            <div class="header"></div>
            
            <div id="app"></div>

            <script type="text/babel">

                function getCookie(name) {
                    let cookieValue = null;
                    if (document.cookie && document.cookie !== '') {
                        const cookies = document.cookie.split(';');
                        for (let i = 0; i < cookies.length; i++) {
                            const cookie = cookies[i].trim();
                            // Does this cookie string begin with the name we want?
                            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }
                const csrftoken = getCookie('csrftoken');


                function DjangoCSRFToken() {
                    return (
                        <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
                    );
                };


                function Profile(props) {

                    let role;

                    switch (props.role) {
                        case 'frontend':
                        role = 'Frontend Developer';
                        break;
                        case 'backend':
                        role = 'Backend Developer';
                        break;
                        case 'fullstack':
                        role = 'Fullstack Developer';
                        break;
                        case 'devops':
                        role = 'Devops Engineer';
                        break;
                        case 'qa':
                        role = 'QA Engineer';
                        break;
                        default:
                        role = 'Frontend Developer';
                    }

                    return (
                        <div class="profile_container">
                            <div>
                                {props.profile_picture ? <img src={'/media/' + props.profile_picture} alt='profile-picture' className="profile_picture"/> :
                                    <img src={'/media/images/profile-picture.png'} alt='profile-picture' className="profile_picture"/>
                                }
                            </div>
                            <ul>
                                <li><strong>Login:</strong> {{user.username}}</li>
                                <li><strong >First name:</strong> <span id="first_name">{props.first_name ? props.first_name : '-'}</span></li>
                                <li><strong>Last name:</strong> <span id="last_name">{props.last_name ? props.last_name : '-'}</span></li>
                            </ul>

                            <h2>Role:</h2>
                            <p>I'm a {role}.</p>

                            <h2>Contact Information:</h2>
                            <ul>
                                <li><strong>GitHub:</strong> {props.github ? props.github : '-'}</li>
                                <li><strong>LinkedIn:</strong> {props.linkedin ? props.linkedin : '-'}</li>
                                <li><strong>Phone Number:</strong> {props.phone_number ? props.phone_number : '-'}</li>
                                <li><strong>Email:</strong> {props.email}</li>
                            </ul>
                            <h2>Country</h2>
                            <p>{props.country}</p>
                            <h2>Bio:</h2>
                            <p>{props.bio}</p>
                            
                            <h2>Skills and Technologies:</h2>
                            <ul>
                                <li><strong>Frontend: </strong>{props.frontend}</li>
                                <li><strong>Backend: </strong>{props.backend}</li>
                                <li><strong>Databases: </strong>{props.database}</li>
                            </ul>
                            <h2>Certificates:</h2>
                            <ul>
                            {props.certificates.map(certificate => (
                                <li key={certificate.id}>
                                    <strong><a className="certificate" href={certificate.url}>{certificate.url}</a></strong>
                                </li>
                            ))}
                            </ul>
                        </div>
                    );
                }


                function App() {
                    const [profile, setProfile] = React.useState([]);
                    const [certificates, setCertificates] = React.useState([]);
                    React.useEffect(() => {
                        const fetchData = async () => {
                            try {
                                const baseUrl = window.location.hostname === "localhost" ? "http://localhost:8000" : "http://127.0.0.1:8000";
                                const response = await fetch(`${baseUrl}/fetch_profile/`);
                                const data = await response.json();
                                setProfile(data);
                                data["certificates"].map(certificate => {
                                    setCertificates(certificates => [...certificates, certificate]);
                                });
                            } catch (error) {
                                console.error("Error fetching data:", error);
                            }
                        };

                        fetchData();
                    }, []);

                    return (
                        <div class="profile-container">
                            <h2><strong>My Profile</strong></h2>
                            <Profile 
                                first_name={profile.first_name}
                                last_name={profile.last_name}
                                role={profile.role}
                                github={profile.github}
                                linkedin={profile.linkedin}
                                phone_number={profile.phone_number}
                                email={profile.email}
                                bio={profile.bio}
                                frontend={profile.frontend}
                                backend={profile.backend}
                                database={profile.database}
                                country={profile.country}
                                profile_picture={profile.profile_picture}
                                certificates={certificates}
                                />
                            <a id="edit_profile" href="{% url 'capstone:edit_profile' %}"><strong>Edit Profile</strong></a>
                        </div>
                    );
                }
                ReactDOM.render(<App />, document.querySelector('#app'));
            </script>
        {% endblock %}

    - **project.html**: displays the project information. And a link to edit the project.
        ```html
        {% extends "base.html" %}
        {% block content %}
        <div class="header">
            <h2>Project: {{project.title}}</h2>    
        </div>

        {% if user.is_authenticated %}

        <div class="project_div">

            <p><strong>Title:</strong> {{project.title}}</p>

            <p><a href="{% url 'capstone:edit_project' project.id %}">Edit</a></p>

            <p><strong>Description:</strong> {{project.description}}</p>
            <p><strong>Technologies used:</strong></p>
            <ul>
                {% if project.frontend %}
                    <li><strong>Frontend: </strong>{{project.frontend}}</li>
                {% endif %}
                {% if project.backend %}
                    <li><strong>Backend: </strong>{{project.backend}}</li>
                {% endif %}
                {% if project.database %}
                    <li><strong>Database: </strong>{{project.database}}</li>
                {% endif %}
            </ul>
            {% if project.github %}
                <p><strong>Github: </strong><a href={{project.github}}>{{project.github}}</a></p>
            {% endif %}
            {% if project.link_to_live_demo %}
                <p><strong>Link to live demo: </strong><a href={{project.link_to_live_demo}}>{{project.link_to_live_demo}}</a></p>
            {% endif %}
        </div>   
        {% endif %}
        {% endblock %}

    - **projects.html**: displays projects listings, a link to 'add a project'. Search for projects. And you can delete each project.
        ```html
        {% extends "base.html" %}
        {% load static %}
        {% block content %}
            <div class="header">
                <h2>My Projects</h2>    
            </div>

            <div id="app"></div>

            <script type="text/babel">

                function getCookie(name) {
                    let cookieValue = null;
                    if (document.cookie && document.cookie !== '') {
                        const cookies = document.cookie.split(';');
                        for (let i = 0; i < cookies.length; i++) {
                            const cookie = cookies[i].trim();
                            // Does this cookie string begin with the name we want?
                            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }
                const csrftoken = getCookie('csrftoken');


                function DjangoCSRFToken() {
                    return (
                        <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
                    );
                };


                function Project(props) {

                    const [isToggle, setIsToggle] = React.useState(false);
                    const [clickedProject, setClickedProject] = React.useState('');
                    const [isDelete, setIsDelete] = React.useState(false);

                    function handleDeleteClick(event) {

                        if (isDelete) {
                            setIsDelete(false); 
                            setClickedProject('');   
                        }
                        else {
                            setIsDelete(true);
                            setClickedProject(event.target.value);
                        }
                    }

                    function handleConfirmDeleteClick(event) {
                        event.preventDefault();
                        if (event.target.value !== 'no') {
                            postData(event.target.value);
                        }
                        else {
                            setIsDelete(false);
                        }
                        
                    }

                
                    function handleToggleClick(event) {
                        console.log(event.target.value);
                        if (isToggle) {
                            setIsToggle(false);
                            setClickedProject('');
                        }
                        else {
                            setIsToggle(true);
                            setClickedProject(event.target.value);
                        }
                    }

                    const postData = async (id) => {

                        try {
                            const baseUrl = window.location.hostname === "localhost" ? "http://localhost:8000" : "http://127.0.0.1:8000";

                            const response = await fetch(`${baseUrl}/delete_project/`, {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json',
                                    'X-CSRFToken': csrftoken
                                },
                                body: JSON.stringify({
                                    project_id: id
                                }),
                            });
                            const data = await response.json();
                            if (data.success) {
                                // Redirect to the new URL provided in the JSON response
                                window.location.href = data.redirect_url;
                            } else {
                                // Handle error message
                                alert(data.error_message);
                            }
                            
                            return data;
                        } catch (error) {
                            console.log('Error sending data:', error);
                        }
                    };

                    
                    return (

                        <div className="projects_container">
                            {props.projects.map(project => (
                                    <div className="project" key={project.id}>
                                        <div className="delete">
                                            <h3></h3>
                                            {% if user.is_authenticated %}
                                                <button onClick={handleDeleteClick} value={project.id} type="button" class="btn btn-danger btn-sm" title="Delete">X</button>
                                                {isDelete && clickedProject == project.id ? 
                                                <div id="div_delete">Delete the project?
                                                    <button onClick={handleConfirmDeleteClick} value={project.id} type="button" class="btn btn-primary btn-sm">Yes</button>
                                                    <button onClick={handleConfirmDeleteClick} value="no" type="button" class="btn btn-primary btn-sm">No</button>

                                                </div> : null}
                                            {% endif %}
                                        </div>

                                        <div id="project_div">
                                            <a href={`/project/${project.id}`} className="project_link">{project.image ?
                                                <div className="project_image_div">
                                                    <div> 
                                                        <img className="project_image" src={'/media/' + project.image} alt="project image" />
                                                    </div>
                                                    <div>
                                                        <p className="project_title">{project.title}</p>
                                                    </div>
                                                </div>
                                                : 
                                                <div className="project_image_div">
                                                    <div>
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" fill="currentColor" class="bi bi-image" viewBox="0 0 16 16">
                                                            <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0"/>
                                                            <path d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1z"/>
                                                        </svg>
                                                    </div>
                                                    <div>
                                                        <p className="project_title">{project.title}</p>
                                                    </div>
                                                </div>
                                            }
                                            </a>
                                        </div>
                                    </div>
                            ))}
                        </div>
                    );
                }


                const Pagination = ({ totalProjects, projectsPerPage, setCurrentPage, currentPage }) => {
                    let pages = [];


                    for (let i = 1; i <= Math.ceil(totalProjects.length / projectsPerPage); i++) {
                        pages.push(i);
                    }


                    return (
                        <div className="pagination">
                            <button 
                                type="button" 
                                className="btn btn-light" 
                                onClick={() => setCurrentPage(currentPage > 1 ? currentPage - 1 : currentPage)} 
                                disabled={currentPage === 1}
                            >
                                Previous
                            </button>
                            {pages.map((page, index) => {
                                return <button key={index} type="button" className="btn btn-light" onClick={() => setCurrentPage(page)} className={page == currentPage ? "active" : "btn btn-light"}>{page}</button>
                            })}

                            <button 
                            type="button" 
                            className="btn btn-light" 
                            onClick={() => setCurrentPage(currentPage < pages.length ? currentPage + 1 : currentPage)} 
                            disabled={currentPage === pages.length}
                            >
                                Next
                            </button>
                        </div>
                    );
                };


                function App() {

                    const [projects, setProjects] = React.useState([]);
                    const [search, setSearch] = React.useState([]);
                    const [filteredProjects, setFilteredProjects] = React.useState(false);
                    
                    const [currentPage, setCurrentPage] = React.useState(1);
                    const [projectsPerPage] = React.useState(8);


                    React.useEffect(() => {
                        const fetchData = async () => {
                            try {
                                const baseUrl = window.location.hostname === "localhost" ? "http://localhost:8000" : "http://127.0.0.1:8000";

                                const response = await fetch(`${baseUrl}/projects_fetch/`);
                                const data = await response.json();
                                setProjects(data);
                            } catch (error) {
                                console.error("Error fetching data:", error);
                            }
                        };

                        fetchData();
                    }, []);


                    const handleSearchClick = async (event) => {

                        if (search !== [] && search.length > 0) {
                            // Filter projects based on search criteria
                            const filteredProjects = projects.filter(project =>
                                project.title.toLowerCase().includes(search.toLowerCase()) ||
                                project.description.toLowerCase().includes(search.toLowerCase()) ||
                                project.frontend.toLowerCase().includes(search.toLowerCase()) ||
                                project.backend.toLowerCase().includes(search.toLowerCase()) ||
                                project.database.toLowerCase().includes(search.toLowerCase())
                            );

                            if (filteredProjects.length > 0) {
                                setFilteredProjects(filteredProjects);
                                setSearch('');
                            }
                            else {
                                console.error("No projects found matching the search criteria");
                            }
                        }
                        else {
                            console.error("Invalid event target");
                            return;
                        }
                    }

                    function handleSearchChange(event) {
                        setSearch(event.target.value);

                    }

                    function handleKeyPress(event) {
                        if (event.key === 'Enter') {
                            handleSearchClick(event);
                        }
                    }


                    const lastProjectIndex = currentPage * projectsPerPage;
                    const firstProjectIndex = lastProjectIndex - projectsPerPage;
                    const currentProjects = projects.slice(firstProjectIndex, lastProjectIndex);


                    return (
                        <div>
                            <div className="search_div">
                                <input onKeyPress={handleKeyPress} onChange={handleSearchChange} type="text" className="search" placeholder="Search" />
                                <button type="button" onClick={handleSearchClick}>Search</button>
                            </div>
                            {% if user.is_authenticated %}
                                <div>
                                    <a id="add_project_link" href="{% url 'capstone:add_project' %}">+add project</a>
                                </div>
                            {% endif %}
                            {filteredProjects ? 
                                <div>
                                    <h3>Found Projects</h3>
                                    <Project projects={filteredProjects} />
                                </div>    
                            : 
                                <div>
                                    <Project projects={currentProjects} />
                                    <Pagination 
                                        totalProjects={projects}
                                        projectsPerPage={projectsPerPage}
                                        setCurrentPage={setCurrentPage} 
                                        currentPage={currentPage}
                                    />
                                </div>
                            }
                        </div>
                    );
                }

                ReactDOM.render(<App />, document.querySelector('#app'));
            </script>
        {% endblock %}

- capstone/capstone/templates/registration/
    - **login.html**: displays login and password.
        ```html
        {% extends "base.html" %}
        {% block title %}Login{% endblock %}
        {% block content %}
            <div class="header">
                <h2>Login</h2>
            </div>
            <div class="form_container">
                <form class="form-group" action="{% url 'login' %}" method="post">
                    {% csrf_token %}
                        {{form.as_p}}
                    <button type="submit" id="login_button" class="btn">Log In</button>
                </form>
            </div>
            <a href="{% url 'password_reset' %}">Forgot password?</a>
        {% endblock %}

    - **password_rest_complete.html**: displays that your password changing is complete.
        ```html
        {% extends "base.html" %}
        {% block title %}Password Change Confirm{% endblock %}
        {% block content %}
        <p class="p">Password Changed!</p>
        {% endblock %}

    - **password_reset_confirm.html**: displays a form to reset your password.
        ```html
        {% extends "base.html" %}
        {% block title %}Password Change Confirm{% endblock %}
        {% block content %}
            <div class="header">
            <h2>Password Change Confirm</h2>
            </div>
            <div class="form_container">
            <form class="form-group" action="" method="post">
                {%csrf_token%}
                {{form.as_p}}
                <button type="submit" class="btn">Save Password</button>
            </form>
            </div>
        {% endblock %}

    - **password_reset_done.html**: displays a message for resetting your password.
        ```html
        {% extends "base.html" %}
        {% block title %}Password Change Confirm{% endblock %}
        {% block content %}
        <p class="p">We've emailed you the instruction for resetting your password.</p>
        {% endblock %}

    - **password_reset_email.html**: a message in your email that will be sent to reset your password.
        ```html
        Someone asked for password reset for email {{ email }}. Follow the link below:
        {{ protocol}}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

    - **password_reset_form.html**: a form to reset your password.
        ```html
        {% extends "base.html" %}
        {% block title %}Password Reset{% endblock %}
        {% block content %}
            <div class="header">
                <h2>Reset Password</h2>
            </div>
            <div class="form_container">
                <form class="form-group" method="post">
                    {% csrf_token %}
                    {{form.as_p}}
                    <button type="submit" class="btn btn-secondary">Send</button>
                </form>
            </div>
        {% endblock %}

    - **register.html**: a form to register a new user.
        ```html
        {% extends "base.html" %}
        {% block title %}Register{% endblock %}
        {% block content %}
            <div class="header">
            <h2>Register</h2>
            </div>
            <div class="form_container">
            <form class="form-group" action="{% url 'register' %}" method="post">
                {% csrf_token %}
                {{form.as_p}}
                <button type="submit" class="btn btn-secondary">Register</button>
            </form>
            </div>
            <a href="{% url 'login' %}">Already have an account?</a>
        {% endblock %}

- capstone/capstone/selenium/
    - **tests.py**: This file contains automated tests for the ePortfolio application using Selenium. It includes test cases for various functionalities such as user authentication, profile management, and project showcase. The tests ensure that the web application behaves as expected and helps in identifying any issues or bugs in the code.
        ```python
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service 
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.keys import Keys
        import time
        import unittest


        service = Service(executable_path=ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service)


        class WebpageTests(unittest.TestCase):     

            def test_title(self):
                """Make sure title is correct"""
                driver.get("http://127.0.0.1:8000/")
                self.assertEqual(driver.title, "ePortfolio")
                
            def test_login(self):
                """Make sure login works"""
                driver.get("http://127.0.0.1:8000/accounts/login/")
                username = driver.find_element(By.NAME, "username")
                password = driver.find_element(By.NAME, "password")
                username.send_keys("testuser")
                password.send_keys("Hnv32.&czY@")
                driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Hello, testuser!")
                
            def test_about(self):
                """Make sure about page works"""
                driver.get("http://127.0.0.1:8000/about/testuser/")
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "About Me")  

            def test_projects(self):
                """Make sure projects page works"""
                driver.get("http://127.0.0.1:8000/projects/testuser/")
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "My Projects")

            # Test adding a project
                wait = WebDriverWait(driver, 10)
                add = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'+add project')]")))
            
                add.click()
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Add Project")
                title = driver.find_element(By.NAME, "title")
                title.click()
                title.clear()
                title.send_keys("Selenium Test")
                
                html = driver.find_element(By.TAG_NAME, 'html')
                html.send_keys(Keys.END)
                wait = WebDriverWait(driver, 10)
                button = wait.until(EC.element_to_be_clickable((By.ID, 'add_project')))
                button.click()

                wait = WebDriverWait(driver, 10)
                h2 = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))

                self.assertEqual(h2.text, "My Projects")
                
                # Test project page
                wait = WebDriverWait(driver, 10)
                project = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Selenium Test')]")))
                project.click()
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Project: Selenium Test")
            
                # Test editing a project
                wait = WebDriverWait(driver, 10)
                edit = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Edit')]")))
                edit.click()
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Edit Project")
                
                title = driver.find_element(By.NAME, "title")
                title.click()
                title.clear()
                title.send_keys("Selenium Test")
                html = driver.find_element(By.TAG_NAME, 'html')
                html.send_keys(Keys.END)
                wait = WebDriverWait(driver, 10)
                button = wait.until(EC.element_to_be_clickable((By.ID, 'save_project')))
                button.click()
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Project: Selenium Test")

                # Test deleting a project
                projects = driver.find_element(By.XPATH, "//a[contains(text(), 'Projects')]")
                projects.click()
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "My Projects")
                project = driver.find_element(By.XPATH, "//p[contains(text(), 'Selenium Test')]")
                button = project.find_element(By.XPATH, "//button[contains(text(), 'X')]")
                button.click()
                delete = driver.find_element(By.XPATH, "//button[contains(text(), 'Yes')]")
                delete.click()
                deleted_project = WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, '//p[contains(text(), "Selenium Test")]')))
                self.assertEqual(deleted_project, True)
            
            def test_contact(self):
                """Make sure contact page works"""
                driver.get("http://127.0.0.1:8000/contact/testuser/")
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Contact")
                
            def test_profile(self):
                """Make sure profile page works"""

                driver.get("http://127.0.0.1:8000/profile/")
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "My Profile")
                driver.find_element(By.CSS_SELECTOR, "a[href='/edit_profile/']").click()
                self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Edit Profile")

                driver.find_element(By.NAME, "first_name").click()
                driver.find_element(By.NAME, "first_name").clear()
                driver.find_element(By.NAME, "first_name").send_keys("Selenium Test")
                driver.find_element(By.ID, "save_profile").click()
                self.assertEqual(driver.find_element(By.ID, "first_name").text, "Selenium Test")
          
        if __name__ == "__main__":
            unittest.main()


- capstone/capstone/static/capstone/
    - **styles.css**: The styles for the ePortfolio.
        ```css
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        :root {
            --primary-color: rgb(121, 34, 236);
            --secondary-color: rgb(96, 0, 222);
            --light-color: lightgray;
            --dark-color: gray;
            --box-shadow: 0 0 10px rgba(133, 23, 212, 0.5);
        }

        html {
            height: 100%;
        }

        body {
            font-family: Arial, sans-serif;
            text-align: center;
            color: var(--primary-color);
            background: linear-gradient(to left, var(--light-color), rgba(255, 255, 255, 0.5));
            padding: 20px 0;
        }

        .navbar-brand {
            color: var(--primary-color) !important;
            font-weight: bold;
            font-size: 24px;
        }

        .navbar {
            position: fixed;
            top: 0;
            box-shadow: var(--box-shadow);
            width: 100%;
            height: 75px;
            font-size: 18px;
            background-color: var(--light-color) !important;
            display: flex;
            justify-content: space-between;
            z-index: 2;
        }

        .navbar ul li a:hover, .navbar button:hover{
            color: var(--primary-color) !important;
        }

        .navbar button {
            background-color: var(--light-color);
            border: none;
            cursor: pointer;
            color: var(--dark-color);
            outline: none;
        }

        .navbar-nav span {
            color: var(--primary-color);
            font-weight: bold;
        }

        .navbar-nav span:hover {
            color: var(--secondary-color);
        }

        .nav-link {
            font-size: 22px;
        }


        .header {
            margin-top: 250px;
        }

        .header h2 {
            font-weight: bold;
        }


        #add_project_link {
            text-decoration: none;
            color: var(--primary-color);
            font-size: 24px;
        }


        #add_project_link:hover {
            color: var(--secondary-color);
        }


        #logout {
            padding: 0 25px;
            border-radius: 5px;
            border: none;
            background-color: var(--primary-color);
            color: white;
            outline: none;
            box-shadow: var(--box-shadow);
        }

        #logout:hover {
            background-color: var(--secondary-color);
            color: var(--light-color) !important;
        }

        .search {
            margin-top: 10px;
            width: 250px;
            padding: 5px;
            border-radius: 5px;
            outline: none;
            border: none;
            margin: auto;
            color: var(--dark-color);
            font-size: 18px;
        }

        #search_button {
            margin: auto;
        }

        .projects_container {
            display: flex;
            justify-content: center;
            flex-direction: row;
            align-items: center;
            margin: 20px auto;
            flex-wrap: wrap;
        }


        .search_div {
            margin: 10px;
            width: 60%;
            margin: auto;
        }

        .search_div input[type=text], .search_div button {
            box-shadow: var(--box-shadow);
        }

        input[type=file] {
            margin-top: 10px;
            border-radius: 5px;
            object-fit: cover;
            padding: 5px;
            box-shadow: var(--box-shadow);
        }


        .search_div button {
            margin: 10px;
            padding: 8px 40px;
            border-radius: 5px;
            border: none;
            background-color: var(--primary-color);
            color: white;
            outline: none;
        }

        .search_div button:hover {
            background-color: var(--secondary-color);
        }


        .project {
            border: 1px solid var(--light-color);
            padding: 10px;
            margin: 10px;
            width: 320px;
            height: 370px;
            background-color: #dcdcdc;
            box-shadow: var(--box-shadow);
            border-radius: 5px;
        }

        .project img {
            position: relative;
            top: -40px;
            right: 10px;
            width: 320px;
            height: 320px;
            box-shadow: var(--box-shadow);
            border-radius: 5px;
            margin-bottom: -30px;
        }

        .project_link {
            text-decoration: none !important;
            color: var(--primary-color);
            font-size: 24px;
        }

        a {
            text-decoration: none !important;
            color: rgb(255, 153, 37);
            font-size: 18px;
        }

        a:hover {
            color: rgb(255, 108, 55);
        }

        .project_link:hover {
            color: var(--secondary-color);
        }


        .project_title {
            font-size: 18px;
            font-weight: bold;
            color: var(--primary-color);
        }


        .delete {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: var(--dark-color);;
            position: relative;
            z-index: 1;
        }

        .delete button {
            background-color: transparent;
            border: none;
            color: var(--dark-color);;
            font-weight: bold;
        }

        .delete button:hover {
            background-color: var(--secondary-color);
        }

        #div_delete {
            background-color: var(--light-color);
            padding: 5px;
            height: 35px;
            border-radius: 5px;
            margin-top: -7px;
        }

        .active {
            background-color: var(--primary-color);
            color: white;
            font-weight: bold;
            padding: 5px 12px;
            border-radius: 5px;
            border: none;
        }

        .active:hover {
            background-color: var(--secondary-color);
        }


        .pagination {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .pagination button {
            margin: 3px;
            box-shadow: var(--box-shadow);
            outline: none;
        }

        .project_div {
            background-color: rgb(239, 239, 239);
            text-align: left;
            width: 500px;
            height: auto;
            margin: 0 auto;
            padding: 25px;
            margin-top: 20px;
            font-size: 18px;
            border-radius: 10px;
            border: 1px solid var(--light-color);
            box-shadow: var(--box-shadow);
            color: var(--dark-color);;
        }

        .project_div strong {
            color: var(--primary-color);
        }

        .project_div ul {
            list-style-type: none;
            padding: 0;
        }

        .form_container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 500px;
            height: auto;
            margin: auto;
            padding: 25px;
            margin-top: 20px;
            margin-bottom: 20px;
            font-size: 18px;
            border-radius: 10px;
            border: 1px solid var(--light-color);
            box-shadow: var(--box-shadow);
            background-color: rgb(239, 239, 239);
        }

        .form_container form input[type="text"], #id_role, #id_link_to_live_demo, textarea, input[type="password"], input[type="email"] {
            border-radius: 3px;
            outline-color: var(--primary-color);
            border: 1px solid var(--light-color);
            padding: 5px;
            text-align: left;
            color: var(--dark-color);;
            box-shadow: var(--box-shadow);
        }

        .form_container li {
            list-style-type: none;
        }

        .form_container button {
            margin: 10px;
            padding: 5px 55px;
            border-radius: 5px;
            border: 1px solid var(--dark-color);;
            background-color: var(--primary-color);
            color: white;
            margin: auto;
        }

        #login_button {
            padding: 10px 55px;
        }

        .form_container button:hover {
            background-color: var(--secondary-color);
        }


        .profile_container {
            width: 640px;
            margin: auto;
            height: auto;
            padding: 25px;
            margin-top: 20px;
            margin-bottom: 20px;
            text-align: left;
            font-size: 18px;
            border-radius: 10px;
            border: 1px solid var(--light-color);
            box-shadow: var(--box-shadow);
            background-color: rgb(239, 239, 239);
        }

        .profile_container {
            color: var(--dark-color);;
        }

        .profile_container a {
            font-size: 24px;
        }

        .profile_container ul {
            list-style-type: none;
            padding: 0;
            margin-top: 20px;
        }

        .profile_picture {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            margin: 15px;
            background-color: var(--light-color);
            box-shadow: var(--box-shadow);
            border: 1px solid var(--light-color);
        }



        .about {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
            font-size: 16px;
            width: 850px;
            height: auto;
            margin: auto;
            background-color: var(--light-color);
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow:var(--box-shadow);
        }

        .about img {
            width: 400px;
            height: auto;
            object-fit: cover;
            border-radius: 10px;
            margin: 15px;
            background-color: var(--light-color);
            box-shadow: var(--box-shadow);
        }

        .bio {
            background-color: rgb(179, 179, 179);
            font-size: 18px;
            min-width: 400px;
            min-height: 400px;
            width: 400px;
            height: auto;
            margin: auto;
            text-align: left;
            border-radius: 5px;
            padding: 10px;
            color: rgb(112, 112, 112);
            box-shadow: var(--box-shadow);
        }

        .bio ul li {
            list-style-type: none;
        }


        .contact_container {
            display: flex;
            justify-content: space-around;
            flex-direction: column;
            align-items: left;
            width: 600px;
            height: auto;
            margin: auto;
            background-color: var(--light-color);
            border-radius: 5px;
            font-size: 18px;
            color: var(--dark-color);;
            box-shadow: var(--box-shadow);
        }

        .contact_container ul {
            list-style-type: none;
            margin: 5px;
            font-size: 20px;
            text-align: center;
        }

        i {
            font-size: 25px;
        }

        .welcome {
            text-align: center;
            font-size: 36px;
            margin: auto;
            background-color: var(--light-color);
            width: 80%;
            height: 780px;
            margin-top: -75px;
            border: 1px solid var(--light-color);
            border-radius: 5px;
            box-shadow: var(--box-shadow);
            position: relative;
            z-index: -1;
        }

        .welcome .header {
            position: relative;
            top: 270px;
            color: var(--dark-color);
        }

        #username {
            color: var(--primary-color);
        }

        .certificate {
            color: var(--primary-color) !important;
            font-size: 18px !important;
        }

        #email {
            color: rgb(255, 88, 88);
        }

        #github {
            color: rgb(78, 78, 78);
        }

        #linkedin {
            color: rgb(55, 155, 255);
        }

        @media only screen and (max-width: 640px) {
            
            .navbar {
                height: auto;
            }

            .projects_container {
                flex-direction: column;
            }

            .profile_container {
                width: auto;
                margin: 10px;
            }

            .contact_container {
                width: auto;
                margin: 10px;
            }

            .form_container {
                width: auto;
                margin: 10px;
            }

            .search_div {
                display: flex;
                justify-content: center;
                flex-direction: column;
            }

            .search_div button {
                margin: auto;
                margin-top: 10px;
                margin-bottom: 15px;
                width: 250px;
            }

            .header {
                margin-top: 270px;
            }

            .about {
                flex-direction: column;
                width: auto;
                margin: auto;
                margin: 10px;
            }

            .project_div {
                width: auto;
                margin: 20px;
            }

            .welcome .header {
                margin-top: 200px;
                font-size: 24px;
            }
        }

        @media only screen and (min-width: 640px) {
            .navbar {
                height: auto;
            }
        }


        @media only screen and (min-width: 1240px) {
            .header {
                margin-top: 120px;
            }
        }

- capstone/capstone/ 
    - **admin.py**: registration for models
        ```python
        from django.contrib import admin
        from .models import User, Profile, Project, Certificate

        # Register your models here.
        admin.site.register(User)
        @admin.register(Profile)
        class ProfileAdmin(admin.ModelAdmin):
            list_display = ('user', 'role')
            list_filter = ('role',)

        admin.site.register(Project)
        admin.site.register(Certificate)

    - **forms.py**: classes for creating forms and associated forms for rendering and editing forms in the ePortfolio.
        ```python
        from django import forms
        from .models import Profile, Project, Certificate

        class ProfileForm(forms.ModelForm):
            class Meta:
                model = Profile
                fields = ['first_name', 'last_name', 'role', 'bio', 'frontend', 'backend', 'database', 'phone_number', 'linkedin', 'github', 'country', 'profile_picture']
        

        class CertificateForm(forms.ModelForm):
            class Meta:
                model = Certificate
                fields = ['url']
                widgets = {
                    'url': forms.URLInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'https://example.com/certificate',
                    }),
                }
                
            
        class ProjectForm(forms.ModelForm):
            class Meta:
                model = Project
                fields = ['title', 'description', 'frontend', 'backend', 'database', 'github', 'link_to_live_demo', 'image']    
        
        
    - **models.py**: models for User, Profile, Project and Certificate.
        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser


        class User(AbstractUser):
            pass


        class Profile(models.Model):
            ROLE_CHOICES = (
                ('frontend', 'Frontend Developer'),
                ('backend', 'Backend Developer'),
                ('fullstack', 'Fullstack Developer'),
                ('devops', 'DevOps Engineer'),
                ('qa', 'QA Engineer'),
            )
            
            user = models.OneToOneField(User, on_delete=models.CASCADE)
            first_name = models.CharField(max_length=100, default="", blank=True)
            last_name = models.CharField(max_length=100, default="", blank=True)
            role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="frontend")
            bio = models.TextField(blank=True)
            frontend = models.CharField(max_length=200, default="", blank=True)
            backend = models.CharField(max_length=200, default="", blank=True)
            database = models.CharField(max_length=200, default="", blank=True)
            phone_number = models.CharField(max_length=15, default="", blank=True)
            github = models.CharField(max_length=100, default="", blank=True)
            linkedin = models.CharField(max_length=200, default="", blank=True)
            country = models.CharField(max_length=200, default="", blank=True)
            profile_picture = models.ImageField(upload_to="images/", 
                                                blank=True, null=True, 
                                                verbose_name="image")
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
            
            
            def __str__(self):
                return self.user.username
            
            
        class Project(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
            title = models.CharField(max_length=100)
            description = models.TextField(blank=True)
            frontend = models.CharField(max_length=200, default="", blank=True)
            backend = models.CharField(max_length=200, default="", blank=True)
            database = models.CharField(max_length=200, default="", blank=True)
            github = models.CharField(max_length=200, default="", blank=True)
            link_to_live_demo = models.URLField(max_length=500, blank=True, null=True)
            image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="image")
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
            
            def __str__(self):
                return self.title
            
        
        class Certificate(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certificates")
            url = models.URLField(max_length=500)

            def __str__(self):
                return self.url
        

    - **tests.py**: tests for projects, profile and views cases.
        ```python
        from django.test import Client, TestCase
        from .models import User, Profile, Project

        class ProfileTestCase(TestCase):
            def setUp(self):
                self.user = User.objects.create(username='johndoe', password='password123', email='johndoe@email.com')
                self.profile = Profile.objects.create(user=self.user, first_name='John', last_name='Doe', bio='I am a software engineer', phone_number='1234567890', github='johndoe', frontend=True, backend=True, database=True, profile_picture='johndoe.jpg')
            
            
            def test_profile(self):
                profile = Profile.objects.get(user=self.user)
                self.assertEqual(profile.first_name, 'John')
                
                
        class ProjectTestCase(TestCase):
            def setUp(self):
                self.user = User.objects.create(username='johndoe', password='password123', email='johndoe@email.com')
                self.project = Project.objects.create(user=self.user, title='My Project', description='This is my project', frontend=True, backend=True, database=True, github='johndoe/myproject', link_to_live_demo='https://github.com/johndoe/myproject', image='myproject.jpg')
                
            def test_project(self):
                project = Project.objects.get(user=self.user)
                self.assertEqual(project.title, 'My Project')
                    

        class ViewsTestCase(TestCase):
            def setUp(self):
                self.client = Client()
                self.user = User.objects.create(username='johndoe', password='password123', email='johndoe@email.com')
                self.profile = Profile.objects.create(user=self.user, first_name='John', last_name='Doe', bio='I am a software engineer', phone_number='1234567890', github='johndoe', profile_picture='johndoe.jpg')
                self.project = Project.objects.create(user=self.user, title='My Project', description='This is my project', frontend=True, backend=True, database=True, github='johndoe/myproject', link_to_live_demo='https://github.com/johndoe/myproject', image='myproject.jpg')
                
                self.client.force_login(self.user)
            
            
            def test_index_view(self):
                response = self.client.get('/')
                self.assertEqual(response.status_code, 200)
                
            def test_profile_view(self):
                response = self.client.get('/profile/')
                self.assertEqual(response.status_code, 200)
                
            def test_projects_view(self):
                response = self.client.get('/projects/johndoe/')
                self.assertEqual(response.status_code, 200)
                
            def test_project_view(self):
                response = self.client.get('/project/1/')
                self.assertEqual(response.status_code, 200)
                
            def test_about_view(self):
                response = self.client.get('/about/johndoe/')
                self.assertEqual(response.status_code, 200)
                
            def test_contact_view(self):
                response = self.client.get('/contact/johndoe/')
                self.assertEqual(response.status_code, 200)
                
                
            def test_edit_profile_view(self):
                response = self.client.get('/edit_profile/')
                self.assertEqual(response.status_code, 200)
                
            def test_add_project_view(self):
                response = self.client.get('/add_project/')
                self.assertEqual(response.status_code, 200)
                
            def test_edit_project_view(self):
                response = self.client.get('/edit_project/1/')
                self.assertEqual(response.status_code, 200)
                
                


    - **urls.py**: contains URLs paths.
        ```python
        from django.urls import path, include
        from . import views

        app_name = "capstone"

        urlpatterns = [
            path("", views.index, name="index"),
            path("about/<str:username>/", views.about, name="about"),
            path("projects/<str:username>/", views.projects, name="projects"),
            path("contact/<str:username>/", views.contact, name="contact"),
            path("profile/", views.profile, name="profile"),
            path("projects_fetch/", views.projects_fetch, name="projects_fetch"),
            path("delete_project/", views.delete_project, name="delete_project"),
            path("fetch_profile/", views.fetch_profile, name="fetch_profile"),
            path('edit_profile/', views.edit_profile, name='edit_profile'),
            path('add_project/', views.add_project, name='add_project'),
            path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
            path('project/<int:project_id>/', views.project, name='project'),
        ]


- capstone/capstone_cache/: contains capstone cache files.

- capstone/media/images/: contains images for profile and projects.

- capstone/project5/settings.py: added SMTP CONFIGURATION and CACHING CONFIGURATION.
    ```python
    
    # SMTP CONFIGURATION

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = '1927samurai@gmail.com'
    EMAIL_HOST_PASSWORD = 'ucztqevmrprmblqc'
    EMAIL_FROM_EMAIL = '1927samurai@gmail.com'
    EMAIL_SUBJECT_PREFIX = 'Password Recovery'

    LOGOUT_REDIRECT_URL = '/'
    LOGIN_REDIRECT_URL = '/'


    # CACHING CONFIGURATION

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'capstone_cache'),
        }
    }


- capstone/project5/urls.py: The project urls for the capstone project.
    ```python
    from django.contrib import admin
    from django.urls import include, path
    from capstone.views import index, registration_view

    from django.conf.urls.static import static
    from django.conf import settings


    urlpatterns = [
        path('admin/', admin.site.urls),
        path("accounts/", include("django.contrib.auth.urls")),
        path('', include('capstone.urls')),
        path('', index, name="index"),
        path("accounts/register/", registration_view, name="register"),     
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

            
    
- capstone/
    - **.dockerignore**: contains Dockerignore files for docker containers.
        ```plaintext
        # Python
        *.pyc
        *.pyo
        *.pyd
        __pycache__/
        *.env

        # Django
        *.log
        *.pot
        *.pyc
        *.mo
        *.swp
        db.sqlite3
        media
        staticfiles

        # Environments
        .env
        .venv
        env/
        venv/
        ENV/
        env.bak/
        venv.bak/

        # IDEs
        .idea/
        .vscode/
        *.sublime-project
        *.sublime-workspace

        # Docker
        Dockerfile
        docker-compose.yml
        .dockerignore

        # Git
        .gitignore
        .git
        .gitattributes
        .gitmodules
        .gitkeep

    - **.gitignore**: contains gitignore files for docker containers.
        ```plaintext
        # Django specific
        *.log
        *.pot
        *.pyc
        __pycache__/
        db.sqlite3
        media/
        staticfiles/

        # Environment variables
        .env

        # Django migrations
        */migrations/*

        # VS Code
        .vscode/

        # PyCharm
        .idea/

        # Byte-compiled / optimized / DLL files
        *.py[cod]
        *$py.class

        # Distribution / packaging
        .Python
        build/
        develop-eggs/
        dist/
        downloads/
        eggs/
        .eggs/
        lib/
        lib64/
        parts/
        sdist/
        var/
        wheels/
        share/python-wheels/
        *.egg-info/
        .installed.cfg
        *.egg

        # Installer logs
        pip-log.txt
        pip-delete-this-directory.txt

        # Unit test / coverage reports
        htmlcov/
        .tox/
        .nox/
        .coverage
        .coverage.*
        .cache
        nosetests.xml
        coverage.xml
        *.cover
        .hypothesis/

        # Translations
        *.mo

        # Django stuff:
        *.log
        local_settings.py

        # Sphinx documentation
        docs/_build/

        # PyBuilder
        target/

        # Jupyter Notebook
        .ipynb_checkpoints

        # pyenv
        .python-version

        # celery beat schedule file
        celerybeat-schedule

        # SageMath parsed files
        *.sage.py

        # Environments
        .env
        .venv
        env/
        venv/
        ENV/
        env.bak/
        venv.bak/

        # Spyder project settings
        .spyderproject
        .spyproject

        # Rope project settings
        .ropeproject

        # mkdocs documentation
        /site

        # mypy
        .mypy_cache/
        .dmypy.json
        dmypy.json

        # Pyre type checker
        .pyre/

    - **docker-compose.yml**: The Docker Compose file that defines the services, networks, and volumes for the application.
        ```yaml
        services:
        db:
            image: postgres
            environment:
                POSTGRES_PASSWORD: password
                POSTGRES_USER: postgres
                POSTGRES_DB: mydatabase

        web:
            build: .
            volumes:
                - .:/usr/src/app
            ports:
                - "8000:8000"

        db_migration:
            build: .
            command: python3 manage.py migrate
            volumes:
                - .:/usr/src/app
            depends_on:
                - db


    - **Dockerfile**: The Docker file that contains the Docker configuration for this project and its dependencies.
        ```docker
        FROM python:3
        COPY .  /usr/src/app
        WORKDIR /usr/src/app
        RUN pip install -r requirements.txt
        CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

    - **README.md**: The documentation for the project.
    - **requirements.txt**: This file lists all the Python dependencies required for the project.
        ```ini
        asgiref==3.8.1
        Django==5.1.3
        pillow==11.1.0
        sqlparse==0.5.2
        typing_extensions==4.12.2
        selenium==4.27.1
        django-cors-headers==4.3.1
        psycopg2-binary==2.9.10


- capstone/capstone/
    - **views.py**: This file contains a list of views for the project.
        - **imports**: imports for the project.
            ```python 
            from django.contrib.auth import authenticate, login, logout
            from django.db import IntegrityError
            from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
            from django.shortcuts import render, redirect
            from django.utils import timezone
            from django import forms
            from .models import User, Profile, Project, Certificate
            import json
            from django.contrib.auth.decorators import login_required
            from django.contrib.auth.forms import UserCreationForm
            from .forms import ProfileForm, ProjectForm, CertificateForm
            from django.shortcuts import get_object_or_404
            from django.core.cache import cache 

        - **RegistrationForm**: class registration form
            ```python
            class RegistrationForm(UserCreationForm):
                email = forms.EmailField(required=True)
                
                class Meta:
                    model = User
                    fields = ("username", "email", "password1", "password2")

        - **registration_view**: renders a registration form.
            ```python
            def registration_view(request):
                if request.method == "POST":
                    form = RegistrationForm(request.POST)
                    if form.is_valid():
                        form.save()
                        username = form.cleaned_data.get('username')
                        password = form.cleaned_data.get('password1')
                        
                        user = authenticate(username=username, password=password)
                        login(request, user)
                        return redirect('index')
                    else:
                        return render(request, 'registration/register.html', {'form': form})
                else:
                    form = RegistrationForm()
                
                return render(request, 'registration/register.html', {'form': form})

        - **index**: renders a homepage for the project.
            ```python
            def index(request):
                return render(request, 'index.html')

        - **about**: renders a profile information.
            ```python
            def about(request, username):
                try:
                    user = User.objects.get(username=username)
                    try:
                        profile = Profile.objects.get(pk=user.id)
                        certificates = Certificate.objects.filter(user=user)
                        certificates_list = list(certificates.values('id', 'url'))
                    except:
                        profile = None
                        certificates_list = []
                except:
                    profile = None
                    
                return render(request, 'capstone/about.html', {
                    'profile': profile,
                    'certificates': certificates_list
                })

        - **projects**: renders template of projects.
            ```python
            @login_required
            def projects(request, username):
                return render(request, 'capstone/projects.html')


        - **contact**: renders template of contact.
            ```python
            def contact(request, username):
                try:
                    user = User.objects.get(username=username)
                    profile = Profile.objects.get(user=user)
                except:
                    profile = None
                return render(request, 'capstone/contact.html', {'profile': profile})

        - **profile**: renders template of profile.
            ```python
            @login_required
            def profile(request):
                user = request.user
                if user.is_authenticated:
                    return render(request, 'capstone/profile.html')
                return render(request, 'capstone/error.html')

        - **projects_fetch**: gets a list of projects from the cache. Returns the list of projects in JSON format that will be display in projects.html template.
            ```python
            @login_required
            def projects_fetch(request):
                user = request.user
                if user.is_authenticated:
                    projects = cache.get('projects')
                    if not projects:
                        projects = Project.objects.filter(user=user).all().values().order_by('-created_at')
                        cache.set('projects', list(projects), 60)  # Cache for 60 seconds
                    else:
                        projects = cache.get('projects')
                    return JsonResponse(list(projects), safe=False)
                else:
                    return JsonResponse({'error': 'User not authenticated'}, status=401)

        - **delete_project**: deletes a project from the database and deletes the cache. Returns Json response.
            ```python
            @login_required
            def delete_project(request):
                if request.method == 'POST':
                    data = json.loads(request.body)
                    project_id = data['project_id']
                    project = Project.objects.get(id=project_id)
                    project.delete()
                    
                    cache.delete('projects')  # Delete cache when a new project is added or updated
                    
                    username = request.user.username
                    
                    return JsonResponse({
                        'success': True,
                        'message': 'Project deleted successfully',
                        'redirect_url': '/projects/{}/'.format(username)
                    }, safe=False)
                return JsonResponse({'error': 'Invalid request'}, status=400)

        - **edit_project**: edits a project, renders the edit_project.html template and ProjectForm. Deletes the cache.
            ```python
            @login_required
            def edit_project(request, project_id):
                user = request.user
                if user.is_authenticated:
                    if project_id:
                        projects = Project.objects.filter(user=user)
                        project = projects.get(pk=project_id)

                        form = ProjectForm(instance=project)
                        
                        if request.method == 'POST':
                            form = ProjectForm(request.POST, request.FILES)
                            if form.is_valid():

                                project.title = form.cleaned_data['title']
                                project.description = form.cleaned_data['description']
                                project.frontend = form.cleaned_data['frontend']
                                project.backend = form.cleaned_data['backend']
                                project.database = form.cleaned_data['database']
                                project.github = form.cleaned_data['github']
                                project.link_to_live_demo = form.cleaned_data['link_to_live_demo']
                                
                                if 'image-clear' in request.POST:
                                    project.image.delete(save=False)
                                    project.image = None 
                                elif 'image' in request.FILES:
                                    project.image = form.cleaned_data['image']
                                
                                project.updated_at = timezone.now()
                                project.save()
                                cache.delete('projects')  # Delete cache when a new project is added or updated
                                # redirect back to edit project page
                                return redirect('capstone:project', project_id=project_id)
                                
                        else:
                            form = ProjectForm(instance=project)
                    return render(request, 'capstone/edit_project.html', {'form': form, 'project': project})
                else:
                    return render(request, 'capstone/error.html')

        - **fetch_project**: this view is responsible for fetching the profile that will be fetched in the profile.html template.
            ```python
            @login_required   
            def fetch_profile(request):
                user = request.user

                if user.is_authenticated:

                    try:
                        # Cache the profile data to improve performance and reduce database load
                        profile = cache.get('profile')
                        if not profile:
                            profile = Profile.objects.get(pk=user.id)
                            cache.set('profile', profile, 60)  # Cache for 60 seconds
                    except:
                        profile = Profile.objects.create(user=user)
                        profile.save()
                        cache.set('profile', profile, 60)  # Cache for 60 seconds
                        
                    certificates = Certificate.objects.filter(user=user)
                    certificates_list = list(certificates.values('id', 'url'))  # Convert QuerySet to list of dictionaries  
                    
                    data = {
                        'id': profile.id,
                        'first_name': profile.first_name,
                        'last_name': profile.last_name,
                        'role': profile.role,
                        'email': user.email,
                        'phone_number': profile.phone_number,
                        'github': profile.github,
                        'linkedin': profile.linkedin,
                        'country': profile.country,
                        'bio': profile.bio,
                        'frontend': profile.frontend,
                        'backend': profile.backend,
                        'database': profile.database,
                        'profile_picture': str(profile.profile_picture),
                        'certificates': certificates_list
                    }

                    return JsonResponse(data, safe=False)
                else:
                    return JsonResponse({'error': 'User not authenticated'}, status=400)

        - **edit_profile**: renders the profile form and certificate form. Returns the updated profile object and certificate object. Delete the cache the profile was changed. Add or delete a certificate. 
            ```python
            @login_required   
            def edit_profile(request):
                user = request.user

                profile = user.profile 
                certificates = Certificate.objects.filter(user=user)
            
                if user.is_authenticated:
                    profile = get_object_or_404(Profile, user=request.user)
                    if request.method == 'POST':
                        form = ProfileForm(request.POST, request.FILES, instance=profile)
                        
                        if 'save_profile' in request.POST and form.is_valid():
                            profile = form.save(commit=False)
                            profile.first_name = form.cleaned_data['first_name']
                            profile.last_name = form.cleaned_data['last_name']
                            profile.role = form.cleaned_data['role']
                            profile.bio = form.cleaned_data['bio']
                            profile.frontend = form.cleaned_data['frontend']
                            profile.backend = form.cleaned_data['backend']
                            profile.database = form.cleaned_data['database']
                            profile.phone_number = form.cleaned_data['phone_number']
                            profile.github = form.cleaned_data['github']
                            profile.linkedin = form.cleaned_data['linkedin']
                            profile.country = form.cleaned_data['country']
                            
                            if 'image-clear' in request.POST:
                                profile.profile_picture.delete(save=False)
                                profile.profile_picture = None 
                            elif 'profile_picture' in request.FILES:
                                profile.profile_picture = form.cleaned_data['profile_picture']
                                
                            profile.save()
                            cache.delete('profile') # Delete cache when the profile is edited
                            return redirect('capstone:profile')
                        
                        certificate_form = CertificateForm(request.POST)
                        if 'add_certificate' in request.POST and certificate_form.is_valid():
                            certificate = certificate_form.save(commit=False)
                            certificate.user = user
                            certificate.url = certificate_form.cleaned_data['url']
                            certificate.save()
                            
                            return redirect('capstone:edit_profile')
                        
                        if 'delete_certificate' in request.POST:
                            certificate_id = request.POST.get('certificate_id')
                            Certificate.objects.filter(id=certificate_id, user=user).delete()
                            return redirect('capstone:edit_profile')
                        
                    else:
                        form = ProfileForm(instance=profile)
                        certificate_form = CertificateForm()
                    
                    return render(request, 'capstone/edit_profile.html', {
                        'form': form,
                        'certificate_form': certificate_form,
                        'certificates': certificates,
                        
                        })
                else:
                    return render(request, 'capstone/error.html')


        - **add_project**: Renders the ProjectForm in add_project.html template. Creates a new project. Deletes the cache. Redirects to the projects.html template.
            ```python
            @login_required       
            def add_project(request):
                user = request.user
                if user.is_authenticated:
                    if request.method == 'POST':
                        form = ProjectForm(request.POST, request.FILES)
                        if form.is_valid():
                            project = Project.objects.create(user=user, 
                                            title=form.cleaned_data['title'], 
                                            description=form.cleaned_data['description'], 
                                            frontend=form.cleaned_data['frontend'],
                                            backend=form.cleaned_data['backend'], 
                                            database=form.cleaned_data['database'],
                                            github=form.cleaned_data['github'],
                                            link_to_live_demo=form.cleaned_data['link_to_live_demo'], 
                                            image=form.cleaned_data['image'],
                                            created_at=timezone.now()
                                        )
                            
                            project.save()
                            cache.delete('projects')  # Delete cache when a new project is added or updated
                            return redirect('capstone:projects', username=user.username)
                    else:
                        form = ProjectForm()
                    return render(request, 'capstone/add_project.html', {'form': form})
                else:
                    return render(request, 'capstone/error.html')


        - **project**: get a project by id and renders it in project.html template.
            ```python  
            @login_required
            def project(request, project_id):
                if project_id:
                    project = Project.objects.get(pk=project_id)
                    return render(request, 'capstone/project.html', {'project': project})
                else:
                    return redirect('capstone:index')
                

        - **error**:  renders the error page
            ```python   
            def error(request):
                return render(request, 'capstone/error.html')



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
