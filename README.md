# Set Up And Run Flask API

1. Set Up Your Environment
 - `python3 -m venv venv`
 - `source venv/bin/activate`


2. Install Dependencies
 - `pip install -r requirements.txt`


3. Set Up the Database
 - Create a psql database with Database name  `assignment`


4. Load Data into the Database
 - `python load_data.py`


5. Start the Flask API
 - `python app.py`


6. REST API Endpoints :

- Get All Banks: http://localhost:5000/banks/

- Get Branch Details:  http://localhost:5000/branches/1

- Get Specific Branch Details By IFSC code :  http://localhost:5000/branches/ifsc/ABHY0065001


- Get All Branches Of a Specific Bank :  http://localhost:5000/branches/bank/60


