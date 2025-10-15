pipeline {
    agent any
    stages {
        stage('Health Check') {
            steps {
                // Run your health check script
                sh 'python3 AutomationONkube.py'
            }
        }
    }
    post {
        always {
            // Archive health check logs or send notifications if needed
        }
    }
}

