# ml_test : This can classify any  data containing numeric  independent variable
# Code-Challenge
# Code tested in python 3.9 environment
# Followed Pep-8 rules

Please follow  the steps how to run the code

PreRequisites: python version > =3.9


How to Run:

step -1:  Download the code from github 
        https://github.com/PriyatamNayak/ml_test

step-2: unzip the code

step-3: go to ml_test Folder and install the python libary mentioned in requirements.txt file (you can create virtul env but that is optional)
         cd ml_test
         pip3 install -r requirements.txt
         
step-4: go to src folder
         cd src
         
step-5: Run the below command
        python run_app.py
        
step-6:
    hurray! your flask app is started successfully

    you can visit : http://localhost:5000
    
 
 step-7:
  how to use: 
     
     Create Model:
          curl -X POST -F "csv_file=@iris.csv" "http://localhost:5000/create?target=Species"
     
     predict using model:     
          curl -X POST -F "input_line=5.1,3.5,1.4,0.2" "http://localhost:5000/predict"

How to Run test cases:
   
    go to src folder and run below command
    
    pytest test\test.py (windows)
    
    pytest test/test.py (Linux)
    
    
Notes: I can add more features and test cases
also can add celery queue and threading to optimize more
and also add async to process different models by keeping in queue