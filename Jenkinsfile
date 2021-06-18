pipeline {
    agent any

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
    }
}