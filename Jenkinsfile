pipeline {
    agent any

    stages {
        stage('Git Status') {
            steps {
                bat "git status"
                copyArtifacts projectName: "build_tcm_lang_assets", target: './langs/', flatten: True
            }
        }
    }
}