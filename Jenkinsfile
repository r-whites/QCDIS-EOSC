properties([pipelineTriggers([githubPush()])])
pipeline {

    environment {
        VERSION = '1.0.0'
        REGISTRY_CREDENTIAL = 'docker-registry'
        REGISTRY = 'rwhites/eosc'
        CHART_RELEASE = 'flaskapp'
        NAMESPACE = 'test'
    }

    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'build_pod.yaml'
        }
    }

    stages {
        stage('Build Flask App') {
            steps {
                dir('App/src') {
                    container('docker') {
                        sh "docker build -t ${REGISTRY}:${VERSION} ."
                    }
                }
            }
        }
        stage('Publish Flask App') {
            steps {
                container('docker') {
                    withDockerRegistry([credentialsId: "${REGISTRY_CREDENTIAL}", url: ""]) {
                        sh "docker push ${REGISTRY}:${VERSION}"
                    }
                }
            }
        }
        stage('Update Flask App') {
            steps {
                dir('App/helm') {
                    container('helm') {
                        sh "helm upgrade -n ${NAMESPACE} ${CHART_RELEASE} ./"
                    }
                }
            }
        }
    }
}
