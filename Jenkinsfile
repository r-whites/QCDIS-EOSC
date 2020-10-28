properties([pipelineTriggers([githubPush()])])
pipeline {

    environment {
        VERSION = '1.0.0'
        REGISTRY_CREDENTIAL = 'docker-registry'
        REGISTRY = 'rwhites/eosc'
        RELEASE = 'flaskapp'
    }

    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'jenkins/build_pod.yaml'
        }
    }

    stages {
        stage('Build Flask App') {
            steps {
                dir('App') {
                    container('docker') {
                        sh "docker build -t ${REGISTRY}:${env.GIT_COMMIT.take(7)} ."
                    }
                }
            }
        }
        stage('Publish Flask App') {
            steps {
                container('docker') {
                    withDockerRegistry([credentialsId: "${REGISTRY_CREDENTIAL}", url: ""]) {
                        sh 'echo hello'
                        sh "docker push ${REGISTRY}:${env.GIT_COMMIT.take(7)}"
                    }
                }
            }
        }
        stage('Update Flask App') {
            steps {
                dir('helm/App') {
                    container('helm') {
                        sh "helm upgrade --set image.tag=${env.GIT_COMMIT.take(7)} ${RELEASE} ./"
                    }
                }
            }
        }
    }
}
