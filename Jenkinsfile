pipeline {
    agent any
    environment {
        APP_NAME = "flask-app"
        DEPLOY_USER = "ubuntu"
        DEPLOY_HOST = "your-server-ip"
        DEPLOY_PATH = "/home/ubuntu/flask-app"
        RESTART_SCRIPT = "/home/ubuntu/restart_flask.sh"
        GIT_REPO = "https://github.com/yourusername/your-flask-repo.git"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: "${GIT_REPO}"
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Deploy to Remote Server') {
            steps {
                sshagent (credentials: ['flask-deploy-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_HOST} '
                        mkdir -p ${DEPLOY_PATH}
                        rm -rf ${DEPLOY_PATH}/*
                    '
                    scp -r * ${DEPLOY_USER}@${DEPLOY_HOST}:${DEPLOY_PATH}/
                    ssh ${DEPLOY_USER}@${DEPLOY_HOST} '
                        chmod +x ${RESTART_SCRIPT}
                        ${RESTART_SCRIPT}
                    '
                    """
                }
            }
        }
    }
    post {
        success {
            echo " Flask app deployed successfully!"
            mail to: 'team@example.com',
                 subject: "SUCCESS: ${APP_NAME} deployed (Build #${BUILD_NUMBER})",
                 body: "Flask app deployed successfully.\n\nBuild URL: ${BUILD_URL}"
        }
        failure {
            echo " Deployment failed!"
            mail to: 'team@example.com',
                 subject: "FAILURE: ${APP_NAME} deployment (Build #${BUILD_NUMBER})",
                 body: "Deployment failed. Please check Jenkins logs.\n\nBuild URL: ${BUILD_URL}"
        }
    }
}

