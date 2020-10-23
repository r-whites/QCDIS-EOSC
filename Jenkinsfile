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
                    dir('SDIA/manager') {
                        container('maven') {
                            sh 'mvn -Dmaven.test.skip=true install'
                            sh 'mvn -Dmaven.test.skip=true dockerfile:build'
                        }
                    }
                }
        }
    }
}