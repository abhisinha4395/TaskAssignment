# TaskAssignment

## Design Approach
* Create 2 tables in mysql database named Tasks And Persons which will store all the data related to the jobs available and employee data
* Each record in both the tables will have a boolean flag through which we can figure if the qc task is completed or not and if the employee is free or not
* The DB should be in a different server from where the flask app is running for better flexibility
* The Flask service will be used to perform the CRUD operations on the database, thus following the MVC architecture.
* The main application of assigning the tasks should be a daemon process or should run every minute which will assign jobs every minute in FIFO fashion
  
