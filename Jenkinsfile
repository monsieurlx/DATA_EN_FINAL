pipeline{
  agent any
  stages {
    stage('Run Web page'){
    	steps{
				script{
					if (env.BRANCH_NAME == 'webinterface') {
	  				sh 'python Project.py'
	 			}	
      }
    }
		
    if (env.BRANCH_NAME == 'Input_Testing') {
      stage('Testing'){
        steps{
          sh 'python test_app.py'
		    }
    if (env.BRANCH_NAME == 'stress_test') {
      sh 'python request_loop.py'
        sh 'locust -f locust_test.py --headless -u 1000'
		   }
		 }
		}
	  }
	}
}
