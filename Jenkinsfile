pipeline {
    agent any

    parameters {
        file(name: 'input.txt')   // File parameter for Java/Python programs
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Sridharpeddamanishi9710/StudRegForm.git'
            }
        }

        stage('Compile Java') {
            steps {
                bat 'javac SimplePattern.java'
            }
        }

        stage('Run Java') {
            steps {
                bat 'java SimplePattern'
            }
        }

        stage('Run Python') {
            steps {
                bat 'python simple_pattern.py'
            }
        }

        stage('Publish HTML') {
            steps {
                bat 'xcopy index.html C:\\inetpub\\wwwroot\\ /Y'
            }
        }
    }
}
