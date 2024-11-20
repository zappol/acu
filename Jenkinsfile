pipeline {
    agent any

    parameters{
        string(name: 'lang_version', defaultValue: "${env.BUILD_NUMBER}", description: "The language version to publish")
    }


    stages {
        stage('Git Status') {
            steps {
                bat "git status"
                // bat "echo Credential: $GIT_USERNAME, $GIT_PASSWORD"
            }
        }

        stage('Get artifacts') {
            steps {
                copyArtifacts projectName: "build_tcm_lang_assets", target: './langs/', flatten: true
            }
        }

        
        stage('Add to git') {
            steps {
                bat 'call scripts/commit_lang_zips.bat'
            }
        }

        stage('get git commit id and update lang config.'){
            steps{
                script{
                    commitId = bat(returnStdout: true, script: "git rev-parse --short HEAD").trim()
                    commitId = commitId.readLines().drop(1).join(" ")
                    bat "python scripts/update_langs_config.py ${lang_version} ${commitId}"
                }
            }
        }

        stage('commit and push'){
            steps{
                bat 'git commit -m "update lang version to ${lang_version}" .'
                // withCredentials(usernamePassword(passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME' )){
                //  // Get some code from a GitHub repository
                // .ssh is configured in .ssh folder.
                    bat "git push origin HEAD:master"
                // }
            }
        }
    }
}