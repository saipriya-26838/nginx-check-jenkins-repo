pipeline {
    agent any

    triggers {
        cron('H H/4 * * *')  // Runs every 4 hours at a randomized minute
    }

    environment {
        LOG_FILE = "/var/log/nginx_monitor.log"
    }

    stages {
        stage('Run Nginx Monitor Script') {
            steps {
                script {
                    // Run the Python script
                    sh '''
                        #!/bin/bash
                        echo "Running Nginx monitor..."
                        /usr/bin/env python3 check_nginx.py
                    '''
                }
            }
        }
    }

    post {
        failure {
            echo "Script failed. Check Jenkins logs and $LOG_FILE"
        }
    }
}
