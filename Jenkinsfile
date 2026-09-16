pipeline {

    agent any

    environment {
        IMAGE_NAME = "jenkins-demo-api"
        CONTAINER_NAME = "jenkins-demo-api"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                        -v "$PWD:/app" \
                        -w /app \
                        python:3.12-slim \
                        bash -c "
                            pip install --no-cache-dir -r requirements.txt &&
                            pytest -v
                        "
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                        -t ${IMAGE_NAME}:${BUILD_NUMBER} \
                        -t ${IMAGE_NAME}:latest \
                        .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true

                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p 5000:5000 \
                        ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 5
                    curl -f http://localhost:5000/health
                '''
            }
        }
    }

    post {
        success {
            echo 'DEPLOYMENT SUCCESSFUL'
        }

        failure {
            echo 'PIPELINE FAILED'
        }
    }
}