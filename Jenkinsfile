pipeline{
  agent any
  stages {
  	stage('Build docker image'){
  		steps{
  			script{
  				if (env.BRANCH_ENV == 'Docker' || env.BRANCH_ENV == 'development' || env.BRANCH_ENV == 'release' || env.BRANCH_ENV == 'main') {
		    		sh 'docker build -t tweet_app .'
		  		}
				}
    	}
    }
    
    stage('Run containerized application'){
      steps{
  			script{
  				if (env.BRANCH_ENV == 'Docker' || env.BRANCH_ENV == 'development' || env.BRANCH_ENV == 'release' || env.BRANCH_ENV == 'main' ) {
		    		sh 'docker RUN -p 5000:5000 tweet_app'
		  		}
				}
    	}
    }
		
    stage('Input_testing'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'Input_Testing') {
							sh 'python3 test_app.py'
		    	}
				}
			}
		}
		 stage('stress_test'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'stress_test' ) {
      				sh 'python3 request_loop.py'
        			sh 'locust -f locust_test.py --headless -u 1000'
					}
				}
				
		  }
		}
		
		
		stage('push to release'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'development') {
    					sh 'git fetch'
    					//sh 'git checkout -b release'
    					//sh 'git merge origin/development'
    					sh'git push -u origin release'
					}
				}
				
		  }
		}
		
		
		stage('Release phase'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							echo '"deploying"' 
		    	}
				}
			}
		}
		
		stage('User validation'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							input 'Accept merge to master ??'
		    	}
				}
			}
		}
		
		stage('Final merging'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'release') {
							sh 'git checkout main'
							sh 'git merge release'
		    	}
				}
			}
		}
				
				
		stage('Delete container'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'development' || env.BRANCH_NAME == 'Docker' || env.BRANCH_ENV == 'development'|| env.BRANCH_ENV == 'main') {
							sh 'docker rmi -f tweet_app'
		    	}
				}
			}
		}
		
		
	}
}




