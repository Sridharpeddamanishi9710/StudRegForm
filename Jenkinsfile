pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Sridharpeddamanishi9710/StudRegForm.git'
            }
        }
        stage('Publish') {
            steps {
                bat 'xcopy reg.html C:\\inetpub\\wwwroot\\ /Y'
            }
        }
    }
}
