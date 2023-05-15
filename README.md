# Finger Counting Game 
  
This project is a browser-based game that teaches children how to count using their fingers. It uses computer vision, a Vue.js front end, and a Node.js backend.  
  
## Prerequisites  
  
Make sure you have the following installed on your system:  
  
 - Docker  
 - Docker Compose  
  
## Directory Structure  
  
The project has the following structure:  
  
 - root
	 - ./client - Vue.js front-end application  
	 - ./server - Node.js back-end application  
	 - ./computer-vision - MediaPipe hand gesture detection  
	 - docker-compose.yml - Docker Compose file to run all services  
  
Each of the `client`, `server`, and `computer-vision` directories contains a Dockerfile that sets up the respective service.  

## Running the Project in Development Mode

To run the project in development mode, follow these steps:

1. Clone the repository and navigate to the project root:

\`\`\`bash
git clone <repository-url>
cd <repository-name>
\`\`\`

2. Build and start the services using Docker Compose:

\`\`\`bash
docker-compose up
\`\`\`

Your services should now be running in development mode:

- The Vue.js client is accessible at `http://localhost:8080`.
- The Node.js server is running at `http://localhost:3000`.
- The MediaPipe application is also running (communication and ports will depend on your specific implementation).

Any changes you make to your source code will be reflected in the running services due to Docker's bind mount feature.

  
## Contributing  
  
Please see this project's [google sheet](https://docs.google.com/spreadsheets/d/1jaIPuNwF-i3fqD9bjewAQPJpkfOkL35NymzIX4QvaJY/edit?usp=sharing) for contribution.