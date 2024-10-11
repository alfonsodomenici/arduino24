from flask import Blueprint,request,json,Response
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256
from .arduinosService import findArduinoByMacaddress
from flask_jwt_extended import create_access_token, jwt_required

auths = Blueprint('auths',__name__, url_prefix='/auths')

@auths.post("/")
def login():
    macaddress = request.json.values()
    found = findArduinoByMacaddress(macaddress)
    if found is None:
        return Response(response="login failed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')
    
    claims={
        'nome':found['nome']
    }
    accessToken = create_access_token(identity=found['id'], 
        additional_claims=claims)
    result = {
        "access_token":accessToken
    }
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')