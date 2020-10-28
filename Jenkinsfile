properties([pipelineTriggers([githubPush()])])
pipeline {

    environment {
        REGISTRY_CREDENTIAL = 'docker-registry'
        REGISTRY = 'rwhites/eosc'
        RELEASE = 'flaskapp'
        NAMESPACE = 'dev'
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
                        sh "docker push ${REGISTRY}:${env.GIT_COMMIT.take(7)}"
                    }
                }
            }
        }
        stage('Update Flask App') {
            steps {
                dir('helm/App') {
                    container('helm') {
                        sh "helm upgrade --install --namespace ${NAMESPACE} --create-namespace --force --set image.tag=${env.GIT_COMMIT.take(7)} ${RELEASE} ./"
                    }
                }
            }
        }
    }
}
