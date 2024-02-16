pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('build') {
            steps {
                bat 'python --version'
                bat 'python main.py'
            }
        }
        stage('test') {
            steps {
                bat 'python test.py'
            }
        }
    }
}
