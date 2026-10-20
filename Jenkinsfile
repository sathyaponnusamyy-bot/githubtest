pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Checking Python environment...'
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python tests...'
                sh 'python3 -m unittest discover -v'
            }
        }
        stage('Package') {
            steps {
                sh '''
                   mkdir -p dist
                   zip -j dist/calculator.zip calculator.py
                '''
                archiveArtifacts artifacts: 'dist/calculator.zip',
                                 fingerprint: true
            }
        }
        stage('Deploy') {
            steps {
                echo 'Tests passed. Ready for deployment!'
            }
        }
    }
}
