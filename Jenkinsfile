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
                parallel {
                    stage('Build SDIA Manager') {
                        steps {
                            dir('SDIA/manager') {
                                container('maven') {
				    sh 'pwd'
                                    sh 'mvn -Dmaven.test.skip=true install'
                                    sh 'mvn -Dmaven.test.skip=true dockerfile:build'
                                }
                            }
                        }
                    }
                    stage('Build SDIA Planner') {
                        steps {
                            dir('SDIA/planner') {
                                container('maven') {
                                    sh 'mvn -Dmaven.test.skip=true install'
                                    sh 'mvn -Dmaven.test.skip=true dockerfile:build'
                                }
                            }
                        }
                    }
                }
        }
    }
}
