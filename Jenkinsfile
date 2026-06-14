pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<your-username>/<your-repo>.git'
            }
        }
        stage('Publish') {
            steps {
                bat 'xcopy reg.html C:\\inetpub\\wwwroot\\ /Y'
            }
        }
    }
}
