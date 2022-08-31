# from crypt import methods
from pyexpat import model
from sqlite3 import Timestamp
from unicodedata import name
from flask import Flask ,request
from flask_restx import Resource ,Api, fields
from datetime import datetime
app = Flask('__name__')
api = Api(app)
# resource_fields = api.model('Temperature', {
#     'Timestamp': fields.String(),
#     'Temp': fields.Integer(),
#     'Notes': fields.String(),
#     })
@api.route('/temp<int:Temp><Notes>', endpoint='/temp') #/<Temp>,<Timestamp>,<Notes>
@api.doc(params={'Temp':'Temprature in Degree celcius','Notes':'Description of temprature'})
class temp(Resource):
    # @api.doc(resource_fields)
    def post(self,Temp,Notes):
        Timestamp=datetime.now()
        Timestamp=str(Timestamp)
        return {"Temperature":Temp,"Timestamp":Timestamp, "Notes":Notes }
# api.add_resource(temp,'/')

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')
