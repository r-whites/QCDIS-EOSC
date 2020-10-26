properties([pipelineTriggers([githubPush()])])
pipeline {

    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'build_pod.yaml'
        }
    }

    stages {
        stage('Build') {
                steps {
                    dir('Test') {
                        container('docker') {
                            sh 'echo \'Building Test app Docker image ..\''
                            sh 'docker image build test-flask-app .'
                        }
                    }
                }
        }
    }
}
