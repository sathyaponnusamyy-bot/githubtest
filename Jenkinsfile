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
            python3 - <<'PY'
import os
import zipfile

files = [
    f for f in os.listdir('.')
    if f.endswith('.py') and not f.startswith('test_')
]

if not files:
    raise Exception("No application Python files found in workspace")

with zipfile.ZipFile('calculator.zip', 'w') as z:
    for f in files:
        z.write(f)

print("Created calculator.zip containing:", files)
PY
            ls -lh calculator.zip
        '''
        archiveArtifacts artifacts: 'calculator.zip', fingerprint: true
    }
}
        
stage('Docker Build') {
    steps {
        sh 'docker build -t sathya-calculator:latest .'
    }
}

stage('Docker Deploy') {
    steps {
        sh '''
            docker rm -f sathya-calculator || true
            docker run -d --name sathya-calculator sathya-calculator:latest
            docker ps -a --filter name=sathya-calculator
        '''
    }
}

        stage('Deploy') {
            steps {
                echo 'Tests passed. Ready for deployment!'
            }
        }
    }
}
