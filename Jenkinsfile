pipeline {
    agent any

    parameters{
        string(name: 'lang_version', defaultValue: "1", description: "The language version to publish")
    }


    stages {
        stage('Git Status') {
            steps {
                bat "git status"
            }
        }

        stage('Get artifacts') {
            steps {
                copyArtifacts projectName: "build_tcm_lang_assets", target: './langs/', flatten: true
            }
        }

        
        stage('Add to git') {
            steps {
                bat 'git add langs'
            }
        }

        stage('get git commit id and update lang config.'){
            steps{
                script{
                    commitId = bat(returnStdout: true, script: 'git rev-parse --short HEAD')
                    bat "python scripts/update_langs_config.py ${lang_version} ${commitId}"
                }
            }
        }
    }
}