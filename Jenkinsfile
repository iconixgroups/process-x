pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'processx/webapp:latest'
        CONTAINER_NAME = 'processx-webapp'
        REGISTRY_CREDENTIALS_ID = 'dockerhub-credentials'
        DEPLOYMENT_ENVIRONMENT = 'production'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build("$DOCKER_IMAGE").push()
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', REGISTRY_CREDENTIALS_ID) {
                        sh "docker pull $DOCKER_IMAGE"
                        sh "docker stop $CONTAINER_NAME || true"
                        sh "docker rm $CONTAINER_NAME || true"
                        sh "docker run -d --name $CONTAINER_NAME -p 80:80 $DOCKER_IMAGE"
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Define test stages here, for example:
                    sh 'npm install'
                    sh 'npm test'
                }
            }
        }
    }
    post {
        success {
            echo 'Deployment and tests successful!'
        }
        failure {
            echo 'The process failed!'
        }
        always {
            echo 'Cleaning up...'
            sh 'docker system prune -f'
        }
    }
}