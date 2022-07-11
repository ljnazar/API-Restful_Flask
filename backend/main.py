from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import json


app = Flask(__name__)
# Soluciona los errores de intercambio de recursos de origen cruzado - Control de acceso HTTP (CORS)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
###############
api = Api(app)
###############
app.config.from_object(__name__)
# The secret key is needed to keep the client-side sessions secure
app.config['SECRET_KEY'] = '\xaf\r\xedP\xa0\x15\x106\xa8w\x05\xc3\x85gY\xe4\x0b\x8f#\xbcu\x1f\xf4\xb5'


class ApiRestFul(Resource):
	def get(self, data):

		### Formateo de datos a JSON ###
		data_json = {
			'dato_enviado': data
					}

		return data_json

api.add_resource(ApiRestFul, '/api/<string:data>') # http://127.0.0.1:5000/data
######################################################################


if __name__ == "__main__":

###########################################################
	#app.config['TEMPLATES_AUTO_RELOAD'] = True      
	#app.jinja_env.auto_reload = True
###########################################################
	# Al colocar la red 0.0.0.0 permite que la web se vea en la red local
	app.run(debug=True, host='0.0.0.0', port='5008')


