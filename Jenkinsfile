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
            dir('SDIA/manager') {
                steps {
                    container('maven') {
                        sh 'pwd'
                    }
                }
            }   
        }
    }
}