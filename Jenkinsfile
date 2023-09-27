pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                // Install dependencies and perform any necessary build steps
                sh 'pip install Flask'
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the chatbot to your server
                sh 'python chatbot.py &'
            }
        }
    }
}
