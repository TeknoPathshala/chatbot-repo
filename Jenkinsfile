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

                // Activate the virtual environment using the appropriate command for your shell
                // For Bash, use 'source venv/bin/activate'
                // For sh, use '. venv/bin/activate'
                sh '. venv/bin/activate'

                // Use the full path to pip to install Flask
                sh '/usr/bin/pip install Flask'  // Replace with the correct path to pip
            }
        }

        stage('Deploy') {
            steps {
                // Run the chatbot within the virtual environment
                sh 'python chatbot.py &'
            }
        }
    }
}
