pipeline{
  agent any
  stages {
/*
  	stage('Build docker image'){
  		steps{
  		
  			script{
  				if (env.BRANCH_ENV == 'Docker' || env.BRANCH_ENV == 'development') {
		    		sh 'docker build -t tweet_app .'
		  		}
				}
    	}
    }
    
    stage('Run containerized application'){
      steps{
  			script{
  				if (env.BRANCH_ENV == 'Docker') {
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
*/
		 stage('stress_test'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'stress_test') {
      				sh 'python3 request_loop.py'
      				sh 'python3 post_loop.py'
        			//sh 'locust -f locust_test.py --headless -u 1000'
					}
				}
				
		  }
		}
/*
		stage('Delete container'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'development' || env.BRANCH_NAME == 'Docker') {
							sh 'docker rmi -f tweet_app'
		    	}
				}
			}
		}
*/
		
	}
}
