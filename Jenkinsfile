pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'make setup'
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                sh 'make test'
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                archiveArtifacts artifacts: '**/htmlcov/**', fingerprint: true 
            }
        }
    }
}
