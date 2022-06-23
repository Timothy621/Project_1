# TRMS - Python 
## Project Description
The Tuition Reimbursement System, TRMS, allows users to submit reimbursements for courses and training.
The submitted reimbursement must be approved by that employee's supervisor, department head, and benefits coordinator.
The benefits coordinator then reviews the grade received before finalizing the reimbursement.

## Technologies Used
 * pgAdmin 4 v6
 * psycopg2 v2.9.3 
 * Flask v2..1.1
 * Flask cors v3.0.10
 * Postman
## Features
List of features ready and TODOs for future development

 * Login using employee database
 * employee is able to Submit Requests for tuition reimbursement.
 * employee is able to Update Requests with new information.
 * employee is able to Dekete Request.
 * employee is able to see all request they have made via a Table that auto populate with their requests.
 * Supervisor(S), Department Head(DH), Benifit Coordinator(BC) are able to see all request related to them via table populate with all request they are related to.
 * S, DH, BC are able to aprove a request.
 * BC are able to adjust reimbursement ammount.
 * S, DH, BC are able to remove request.
 
 To-do list: 
 *  Add more Functionality to the front end by changing The Table view to show both tables when user is superviser
 *  Add try catch blocks to allow execution of code even if an error occurs. allows for fail state alerts to work.
 *  Revamp Site Style to look better. Grab images to embed so on and so forth.
 *  Revert GET_ALL_REQUEST back to previous version and fix fatal error on DH and Supervisor checks.
 *  Add restriction to the reimbursement ammount.
 
 ## Getting Started
 git commands `git clone https://github.com/Timothy621/TRMS---Python-The-Tuition-Reimbursement-System.git`
 This project was writen in pycharm for the backend and uses Visual studio code for its frontend as well as uses pycopg2, flask and flask cors which can be installed using pip. 
in addition you will need to set up a file for your database connection called DBconnection.py
 ## Usage 
 You will need to have both the front end (tuition_reimbursement_login.html) running as well as the backend (app.py). once up and running you can login with the credentals in your database. upon login you will be redirected to the main page the tables will auto populate if any requests exist. you will also see several buttons that allow you to preform various actions like creating request updating and removingthem.
if you are logged in as an S, DH or BC you will have access to the approval/removal process and if your the BC you can adjust the reimbursement ammount.
 
