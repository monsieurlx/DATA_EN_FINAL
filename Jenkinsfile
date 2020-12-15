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
     				if (env.BRANCH_NAME == 'Input_Testing' || env.BRANCH_NAME == 'test') {
							sh 'python3 test_app.py'
		    	}
				}
			}
		}
		 stage('stress_test'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'stress_test' || env.BRANCH_NAME == 'test') {
      				sh 'python3 request_loop.py'
        		//	sh 'locust -f locust_test.py --headless -u 1000'
					}
				}
				
		  }
		}
		
		// If the test succeeded then : 
		
		stage('development stage'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'test') {
    					//sh 'git config --global user.email "leoixeu@hotmail.fr"'
    					//sh 'git branch -a'
    					//sh 'git remote add origin https://github.com/monsieurlx/DATA_EN_FINAL.git'
    					sh 'git checkout -b Docker || git checkout Docker'
    					sh 'git pull'
    					sh 'git checkout -b development || git checkout development'	
    					sh 'git fetch'	
    					sh 'git pull'
    					//sh 'git fetch --all'			
    					sh 'git merge origin/Docker'
    					//sh'git add *'
    					sh'git commit --allow-empty -m "add image to development"'
    					sh'git push -f https://monsieurlx:Jenkinspwd1234@github.com/monsieurlx/DATA_EN_FINAL.git'
    					//sh'git push https://github.com/monsieurlx/DATA_EN_FINAL.git'
					}
				}
				
		  }
		}
		/*
		stage('push to release'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'development') {
    					sh 'git checkout -b release || git checkout release'	
    					sh 'git fetch'	
    					sh 'git pull'
    					sh 'git merge development'
    					sh'git commit --allow-empty -m "release the application"'
    					sh'git push -f https://monsieurlx:Jenkinspwd1234@github.com/monsieurlx/DATA_EN_FINAL.git'
    					//sh'git push https://github.com/monsieurlx/DATA_EN_FINAL.git'
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
     				if (stage('push to release'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'development') {
    					sh 'git checkout -b release || git checkout release'	
    					sh 'git fetch'	
    					sh 'git pull'
    					sh 'git merge development'
    					sh'git commit --allow-empty -m "release the application"'
    					sh'git push -f https://monsieurlx:Jenkinspwd1234@github.com/monsieurlx/DATA_EN_FINAL.git'
    					//sh'git push https://github.com/monsieurlx/DATA_EN_FINAL.git'
					}
				}
				
		  }
		}env.BRANCH_NAME == 'development' || env.BRANCH_NAME == 'Docker' || env.BRANCH_ENV == 'development'|| env.BRANCH_ENV == 'main') {
							sh 'docker rmi -f tweet_app'
		    	}
				}
			}
		}
		
	*/	
	}
}




