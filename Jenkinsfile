pipeline{
    agent any
    environment{
        PYTHON='C:\\Users\\priya\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        APP_TOKEN= credentials("App_Token")
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
                bat """
                 SET TOKEN=%APP_TOKEN%
                 %PYTHON% extractdata.py
                  """

                
            }
        }
    }
}