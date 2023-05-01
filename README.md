## Social Media API

<p>RESTful API service that provides functionality for managing a social media system.</p>

___

### Features

<ul>
<li><strong>Authentication:</strong> Secure access to API endpoints using JWT token-based authentication.</li>
<li><strong>Post management:</strong> Full CRUD functionality for managing posts, including creation, retrieval, updating, and deletion. Filter posts by title and content.</li>
<li><strong>User management:</strong> Allow users to register, update their profile information (e.g., bio and avatar), and search for other users by username.</li>
<li><strong>API documentation:</strong> Use Swagger UI to generate interactive API documentation that helps developers easily explore and test the endpoints of the API.</li>
<li><strong>Deployment:</strong> Easy deployment with Docker and docker-compose.</li>
</ul>

___

### Getting Started

#### Installation using Docker

<p>Before you begin, make sure you have Docker installed on your computer. To do this, run the following command:</p>

```shell
docker --version
```

<p>The result of the execution should be the docker version. If it is not, install docker on your computer, if everything is ok, follow these steps:</p>

1. Clone the project repository to your computer using the following command:
    ```shell
    git clone https://github.com/bihunva/social-media-api.git
    ```

2. Add the <strong>.env</strong> file to the root of the project. In this file you must specify the values of the
   environment variables, an example is in the file <strong>.env.sample</strong>.


3. Build Docker images by running the following command:
   ```shell
   docker-compose build
   ```

4. Run Docker containers by running the following command:
   ```shell
   docker-compose up
   ```

#### Local installation

<p>Before you begin, make sure you have Python and PostgreSQL installed on your computer. To do this, run the following commands:</p>

```shell
python3 --version
```

```shell
psql --version 
```

<p>The command output should be Python and PostgreSQL versions, respectively. If it is not, you need to install Python and PostgreSQL on your computer. If everything is ok, follow these steps:</p>

1. Clone the repository:
    ```shell
    git clone https://github.com/bihunva/social-media-api.git
    ```

2. Create and activate a virtual environment (venv):
    ```shell
    python3 -m venv venv
    source venv/bin/activate # for Unix-based systems
    venv\Scripts\activate # for Windows
    ```

3. Install dependencies:
    ```shell
    pip install -r requirements.txt
    ```

4. Set the following environment variables with your own values in a .env file in the root directory of the project:

   ```
   POSTGRES_DB=<POSTGRES_DB>
   POSTGRES_USER=<POSTGRES_USER>
   POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
   POSTGRES_HOST=<POSTGRES_HOST>
   POSTGRES_PORT=<POSTGRES_PORT>
   DJANGO_SECRET_KEY=<DJANGO_SECRET_KEY>
   ```

5. Run migrations
    ```shell
   python manage.py migrate
    ```

6. Start the development server
    ```shell
    python manage.py runserver
    ```


Now, you should be able to access the development server at http://localhost:8000/.