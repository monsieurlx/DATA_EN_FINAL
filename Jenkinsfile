pipeline{
  agent any
  stages {
  	stage('Build docker image'){
  		script{
  			if (env.BRANCH_ENV == 'Docker') {
		  		steps{
		    		sh 'docker build -t tweet_app .'
		  		}
				}
    	}
    }
    
    stage('Run containerized application){
  		script{
  			if (env.BRANCH_ENV == 'Docker') {
		  		steps{
		    		sh 'docker RUN -p 5000:5000 tweet_app'
		  		}
				}
    	}
    }
		
    stage('Input_testing'){
     		steps{
     			script{
     				if (env.BRANCH_NAME == 'Input_Testing') {
							sh 'python test_app.py'
		    	}
				}
			}
		}
		 stage('stress_test'){
				steps{
					script{
    				if (env.BRANCH_NAME == 'stress_test') {
      				sh 'python request_loop.py'
        			sh 'locust -f locust_test.py --headless -u 1000'
					}
				}
				
		  }
		}
	}
}

