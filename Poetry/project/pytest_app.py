#flask project to implement authentication with help of flask-pydantic

from flask import Flask,render_template,request
import sqlite3
from pydantic import BaseModel
from flask_pydantic import validate

app=Flask(__name__)

##################################################Validation using flask-pydantic############################

#class for validation
class RequestFormDataModel(BaseModel):
  id: int
  Name: str
  Address: str


  
#Method to validate input data through form and post 
@app.route("/post", methods=["POST"])
@validate()
def post(form: RequestFormDataModel): 
  id= form.id
  Name = form.Name
  Address =form.Address
  
  con = sqlite3.connect('example.db')
  cur = con.cursor()

  cur.execute('''INSERT INTO Information(Name, Address) VALUES("%s","%s")''' % (Name,Address))
  con.commit()
  return "Successful"

###############################Get methode to retrive data from database also used for pytest #####################

#Get method for run test using pytest 
@app.route("/pytest",methods = ["GET"])
def pytest():
    """ function to get all books """
    if request.method == "GET":  
        con=sqlite3.connect(r"example.db")
        cur=con.cursor()
        cur.execute("""SELECT * FROM Information""")
        data=cur.fetchall()
        con.commit()
        return {"Info":data}

##############################Simple Post methode to give json input to app ######################### 

#Post method to take json format input 
@app.route('/new',methods=["POST"])
def new():
    if request.method=='POST':
        data=request.get_json()
        Name=data['Name']
        Address=data['Address']

        con = sqlite3.connect('example.db')
        cur = con.cursor()

        def Insert(a,b):
            cur.execute('''INSERT INTO Information(Name, Address) VALUES("%s","%s")''' % (a,b))

        Insert(Name,Address)
        con.commit()
    return "Successful"

#######################################################################################################

if __name__=='__main__':
    app.run(debug=True)