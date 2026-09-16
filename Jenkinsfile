pipeline {
    agent any

    environment {
        PYTHONPATH = '/workspace/jenkins-demo'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-demo:latest .'
            }
        }
    }
}
