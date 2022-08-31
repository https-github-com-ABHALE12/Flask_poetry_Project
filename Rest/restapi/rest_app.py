from flask import Flask ,request
from flask_restx import Resource ,Api ,fields
import datetime

app = Flask('__name__')
api = Api(app)

model1= api.model('model1', {
    'Timestamp': fields.String,
    'Temperature': fields.Integer(min=0) ,
    'Note': fields.String
})


@api.route('/Temp/<int:Temperature>,<Note>',endpoint='/Temp')
@api.doc(params={"Temperature":"Put current Temperature","Note":"Input note if any"})
class MyResource(Resource):
    @api.doc(model=model1)
    def post(self,Temperature,Note):
        x=datetime.datetime.now()
        x=str(x)
        return {"Timestamp":x,"Temperature":"{0}°C".format(Temperature),"Note":Note}

# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
########################################################


if __name__ =='__main__':
    app.run(debug=True)
