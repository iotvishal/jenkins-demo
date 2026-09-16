pipeline {

    agent any

    stages {

        stage('Run Tests') {
            steps {
                sh '''
                    echo "===== BUILD TEST IMAGE ====="

                    docker build \
                        -f Dockerfile.test \
                        -t jenkins-demo-test:${BUILD_NUMBER} \
                        .

                    echo "===== RUN TESTS ====="

                    docker run --rm \
                        jenkins-demo-test:${BUILD_NUMBER}
                '''
            }
        }

    }

    post {
        success {
            echo 'TESTS PASSED'
        }

        failure {
            echo 'TESTS FAILED'
        }
    }
}