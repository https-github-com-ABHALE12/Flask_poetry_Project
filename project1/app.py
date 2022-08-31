from lib2to3.pytree import Base
from flask_pydantic import validate
from flask import Flask,render_template,request
import pickle
import sqlite3
from datetime import datetime
from pydantic import BaseModel

class rev1(BaseModel):
    review: str

#creating list 
sentiments=["Negative","Some what negative","Neutral","Some what positive","Positive"]

# load saved model
with open(r'model_pkl' , 'rb') as f:
    model = pickle.load(f)

#Creating Flask API
app=Flask(__name__)
#Post Method
@app.route('/submit',methods=["POST"])
@validate()
def post(form:rev1):
    '''
    This method will be called when we want to post the data.
    So This method will post the review and return the appropriate sentiment of the review
    '''
    if request.method=='POST':
        # Getting the details in json format using postman
        review= form.review
        date1=datetime.now()
        # data=request.get_json()
        # review=data['review']
        res=(model.predict([review])) #Model doing prediction
        res=sentiments[res[0]]        # converting the output of int to string in list sentiments
        res=str(res) #typecasting
        print(res) #printing result to terminal
        connection=sqlite3.connect("details2.db") #Connecting to the database
        cursor=connection.cursor() #Creating cursor
        #Executing the query
        cursor.execute("""INSERT INTO details(review,result,timedetails) VALUES(?,?,?)"""  ,(review,res,date1,)) 
        #Closing the connection
        connection.commit()
        #Returning result in Json format
        return {"response": res}
@app.route('/getting',methods=["GET"])
# @validate
def getting():
    '''
    This method will be using GET method.
    This method return the data in the database in the form of JSON
    '''
    # a={'review':review}
    # rev1=rev(**a)
    #Creating connection and cursor
    connection=sqlite3.connect("details2.db")
    cursor=connection.cursor()
    # Executing query
    # cursor.execute("""SELECT * FROM details where review=?""",(rev1.review,))
    cursor.execute("""SELECT * FROM details""")
    A=cursor.fetchall()
    connection.commit()
    # returning the result
    return{"response":A}
@app.route("/delete",methods=["DELETE"])
def delete():
    '''
    Method to delete elements from the database
    '''
    a=datetime.now()
    connection=sqlite3.connect("details2.db")
    cursor=connection.cursor()
    cursor.execute(""" DELETE FROM details where timedetails<=(?) """ ,(a,))
    A=cursor.fetchall()
    connection.commit()
    return {"Data":A}
#Main Method (Driver Code)
if __name__=='__main__':
    app.run(debug=True) #Running with debug

"""
Output using Get method:
{
"response": [
        [
            "Good",
            "Somewhat Positive"
        ],
        [
            "bad",
            "[2]"
        ],
        [
            "bad",
            "[2]"
        ],
        [
            "bad",
            "[2]"
        ],
        [
            "bad",
            "Neutral"
        ],
        [
            "bad",
            "Neutral"
        ],
        [
            "bad",
            "Neutral"
        ]
    ]
}
"""
"""
Output Using Post method:
Input:
Body->Json->
{
    "review": "Very good"
}
Output:
{
    "response": "Some what positive"
}
"""