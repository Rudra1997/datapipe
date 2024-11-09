@Library('jenkins-shared-library@master') _
pipeline {
    agent any

    stages {
        stage('Checkout GitHub Repository') {
            steps {
                script {
                    echo "Checking out repository from GitHub..."
                    git branch: 'main', changelog: false, poll: false, url: 'https://github.com/Rudra1997/datapipe.git'
                    echo "Successfully checked out repository."
                }
            }
        }

        stage('Data Extraction') {
            steps {
                script {
                    echo "Starting Data Extraction..."
                    if (fileExists("extract_data.py")) {
                        def result = sh(script: "python3 extract_data.py data.csv", returnStdout: true).trim()
                        if (result) {
                            echo "Data Extraction Output: ${result}"
                        }
                        echo "Data Extraction completed successfully."
                    } else {
                        echo "Extract script not found, skipping this stage."
                    }
                }
            }
        }

        stage('Data Transformation') {
            steps {
                script {
                    echo "Starting Data Transformation..."
                    if (fileExists("transform_data.py")) {
                        def result = sh(script: "python3 transform_data.py data.csv", returnStdout: true).trim()
                        if (result) {
                            echo "Data Transformation Output: ${result}"
                        }
                        echo "Data Transformation completed successfully."
                    } else {
                        echo "Transform script not found, skipping this stage."
                    }
                }
            }
        }

        stage('Data Ingestion') {
            steps {
                script {
                    echo "Starting Data Ingestion..."
                    if (fileExists("ingest_data.py")) {
                        def result = sh(script: "python3 ingest_data.py data.csv", returnStdout: true).trim()
                        if (result) {
                            echo "Data Ingestion Output: ${result}"
                        }
                        echo "Data Ingestion completed successfully."
                    } else {
                        echo "Ingest script not found, skipping this stage."
                    }
                }
            }
        }

        stage('Data Quality Checks') {
            steps {
                script {
                    echo "Starting Data Quality Checks..."
                    if (fileExists("dq_check.py")) {
                        def result = sh(script: "python3 dq_check.py data.csv", returnStdout: true).trim()
                        if (result) {
                            echo "Data Quality Check Output: ${result}"
                        }
                        echo "Data Quality Check completed successfully."
                    } else {
                        echo "Data Quality Check script not found, skipping this stage."
                    }
                }
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'Data_Quality_Report.pdf, data.csv', allowEmptyArchive: true
            cleanWs()
        }
        failure {
            script {
                emailNotification("Rudradeep.Deb@in.ey.com")
                echo "Pipeline failed. Please check the logs."
            }
        }
        success {
            script {
                emailNotification("Rudradeep.Deb@in.ey.com")
                echo "Pipeline completed successfully."
            }
        }
    }
}
