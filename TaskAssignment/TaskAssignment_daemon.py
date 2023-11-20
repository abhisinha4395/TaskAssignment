import requests
import json

from time import time

class TaskAssignmentDaemon(object):
    
    def __init__(self):
        pass
    
    def run(self):
        while True:
            free_emps = requests.get("localhost:4000/get_free_emps")
            if free_emps:
                available_jobs = requests.get("localhost:4000/get_available_jobs")
                
                "Assign task in round robin fashion and update the status of the task and Person"
                    
            time.sleep(1)
            
    

if __name__ == "__main__":
    TaskAssignmentDaemon().run()
