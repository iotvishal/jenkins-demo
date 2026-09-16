pipeline {

    agent any

    stages {

        stage('Run Tests') {
            steps {
                sh '''
                    echo "===== JENKINS WORKSPACE ====="
                    pwd

                    echo "----- files -----"
                    find . -maxdepth 2 -type f -print

                    echo "===== DOCKER MOUNT TEST ====="

                    docker run --rm \
                        -v "$PWD:/app" \
                        -w /app \
                        python:3.12-slim \
                        bash -c '
                            echo "Inside Python container:"
                            pwd

                            echo "----- files -----"
                            find . -maxdepth 2 -type f -print
                        '
                '''
            }
        }

    }
}