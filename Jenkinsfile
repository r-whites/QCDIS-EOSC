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
                container('maven') {
                    sh 'mvn -h'
                }
            }
        }
    }
}