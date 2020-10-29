properties([pipelineTriggers([githubPush()])])
pipeline {

    environment {
        REGISTRY_CREDENTIAL = 'docker-registry'
        REGISTRY = 'rwhites/flaskapp'
        RELEASE = 'flaskapp'
        NAMESPACE = "${env.BRANCH_NAME == "master" ? "prod" : "dev"}"
    }

    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'jenkins/build_pod.yaml'
        }
    }

    stages {
        stage('Test App') {
            steps {
                dir('App') {
                    container('python') {
                        sh 'pytest -v'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                dir('App') {
                    container('docker') {
                        sh "docker build -t ${REGISTRY}:${env.GIT_COMMIT.take(7)} ."
                    }
                }
            }
        }
        stage('Publish Docker Image') {
            steps {
                container('docker') {
                    withDockerRegistry([credentialsId: "${REGISTRY_CREDENTIAL}", url: ""]) {
                        sh "docker push ${REGISTRY}:${env.GIT_COMMIT.take(7)}"
                    }
                }
            }
        }
        stage('Update Cluster') {
            steps {
                dir('helm/App') {
                    container('helm') {
                        sh "helm upgrade --install --namespace ${NAMESPACE} --set image.tag=${env.GIT_COMMIT.take(7)} ${RELEASE} --values values_${NAMESPACE}.yaml ./"
                    }
                }
            }
        }
    }
}
