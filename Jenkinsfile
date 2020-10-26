properties([pipelineTriggers([githubPush()])])
pipeline {

    environment {
        VERSION = '1.0.0'
        REGISTRY_CREDENTIAL = 'docker-registry'
        REGISTRY = 'rwhites/eosc'
    }

    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'build_pod.yaml'
        }
    }

    stages {
        stage('Build Flask Test App') {
            steps {
                dir('Test') {
                    container('docker') {
                        sh "docker build -t ${REGISTRY}:${VERSION} ."
                    }
                }
            }
        }
        stage('Push Flask Test App Image') {
            steps {
                container('docker') {
                    withDockerRegistry([credentialsId: "${REGISTRY_CREDENTIAL}", url: ""]) {
                        sh "docker push ${REGISTRY}:${VERSION}"
                    }
                }
            }
        }
    }
}
