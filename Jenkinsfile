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
                // Install Python and create a virtual environment
                sh 'sudo apt-get update'
                sh 'sudo apt-get install python3 python3-venv python3-pip -y'
                sh 'python3 -m venv venv' // Create a virtual environment

                // Activate the virtual environment
                sh '. venv/bin/activate'

                // Install Flask and other dependencies (if any)
                sh '/usr/bin/pip install Flask'  // Replace with the correct path to pip

                // Additional commands for dependency installation if needed
                // sh '/usr/bin/pip install package-name'
            }
        }

        stage('Deploy') {
            steps {
                // Run the chatbot within the virtual environment
                sh 'source venv/bin/activate && python chatbot.py &'
            }
        }
    }

    post {
        always {
            // Clean up the virtual environment
            sh 'de
