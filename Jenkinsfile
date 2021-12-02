pipeline {
	agent any
	stages {	
		
		stage('Test') {
			steps {
                git branch:'main',url:'https://github.com/Kchanglong/ict3103labtest.git'
            }
		}

		stage('Code Quality Check via SonarQube') {
		steps {
			script {
				def scannerHome = tool 'SonarQube';
				withSonarQubeEnv() {
					sh "${tool("SonarQube")}/bin/sonar-scanner \
					-Dsonar.projectKey=ict3103 \
					-Dsonar.sources=. \
					-Dsonar.host.url=http://18.118.132.117:9000 \
					-Dsonar.login=55e2454a5dc733d5bc240210114e56a387b8bfff"
					}
				}
			}
		}

		stage('OWASP DependencyCheck') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'OWASP Dependency-Check'
			}
		}
	}
	post {
		always{
			
			recordIssues enabledForFailure: true, tools: sonarQube()
		
		}
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}
