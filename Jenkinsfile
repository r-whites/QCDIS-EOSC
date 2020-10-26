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
                            sh 'docker build -t eosc/test-flask-app:1.0.0 .'
                        }
                    }
                }
        }
    }
}
