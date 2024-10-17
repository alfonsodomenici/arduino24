from flask import Blueprint,request,json,Response
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256
from .arduinosService import findArduinoByMacaddress, createArduino
from flask_jwt_extended import create_access_token, jwt_required
from names_generator import generate_name

auths = Blueprint('auths',__name__, url_prefix='/auths')

@auths.post("/")
def login():
    macaddress = request.json['macaddress']
    found = findArduinoByMacaddress(macaddress)
    if found is None:
       nome = generate_name() 
       found = createArduino(nome,macaddress)

    claims={
        'nome':found['nome']
    }
    accessToken = create_access_token(identity=found['id'], 
        additional_claims=claims)
    result = {
        "id": found['id'],
        "nome":found['nome'],
        "access_token":accessToken
    }
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')