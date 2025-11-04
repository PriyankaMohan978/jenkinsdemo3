pipeline{
    agent any
    environment{
        PYTHON='C:\\Users\\priya\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages{
        stage('checkout code'){
            steps{
                checkout scm


            }
        }

        stage('Install dependencies'){
            steps{
                bat " ${env.python} -m pip install -r requirements.txt"
                
            }
        }

        stage('extract data'){
            steps{
                bat "${env.python} extractdata.py"

                
            }
        }
    }
}