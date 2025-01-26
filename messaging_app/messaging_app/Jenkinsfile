pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('74a0b522-6290-43be-9af8-554fac6ca19c')
        DOCKER_IMAGE_NAME = 'malakehab2003/messaging-app'
        DOCKER_IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the specified Git branch
                git branch: 'master',
                    credentialsId: '74a0b522-6290-43be-9af8-554fac6ca19c', 
                    url: 'https://github.com/malakehab2003/alx-backend-python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Create a Python virtual environment
                sh 'python3 -m venv venv'
                // Activate the virtual environment and install dependencies from requirements.txt
                sh 'source venv/bin/activate && pip3 install -r messaging_app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh 'source venv/bin/activate && pytest --junitxml=test-results.xml'
            }
            post {
                always {
                    // Publish test results
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    docker.build("${env.DOCKER_IMAGE_NAME}:${env.DOCKER_IMAGE_TAG}", './messaging_app')
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                // Log in to Docker Hub
                script {
                    docker.withRegistry('https://registry.hub.docker.com', "${env.DOCKER_HUB_CREDENTIALS}") {
                        // Push the Docker image to Docker Hub
                        docker.image("${env.DOCKER_IMAGE_NAME}:${env.DOCKER_IMAGE_TAG}").push()
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up the workspace
            cleanWs()
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}