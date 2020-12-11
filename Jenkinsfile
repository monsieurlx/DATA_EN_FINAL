pipeline{
	agent any
  stages {
  	stage('Run Web page'){
    	steps{
				script{
					if (env.BRANCH_NAME == 'webinterface') {
	  				sh 'python3 Project.py'
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
    					if (env.BRANCH_NAME == 'stress_test') {
      					sh 'python3 request_loop.py'
        				sh 'locust -f locust_test.py --headless -u 1000'
							}
						}
					}
				
		   }
		 }
}
