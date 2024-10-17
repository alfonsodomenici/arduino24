from flask import Blueprint, request,json, Response
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256  
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from .arduinosService import findAllArduino,createArduino,findArduino, findArduinoDati, createArduinoDati, deleteArduino

arduinos = Blueprint('arduinos',__name__,url_prefix='/arduinos')

@arduinos.get("/")
def all():
    result = findAllArduino()
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')
    
@arduinos.post("/")
def registration():
    nome,macaddress = request.json['nome'], request.json['macaddress']
    result = createArduino(nome,macaddress)
    return Response(response=json.dumps(result), status=HTTPStatus.CREATED, content_type='application/json')

@arduinos.get("/<int:id>")
@jwt_required()
def find(id):
    sub = get_jwt_identity()
    if id != sub:
        return Response(response="access is not allowed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')
    
    user = findArduino(id)
    return Response(response=json.dumps(user), status=HTTPStatus.OK, content_type='application/json')

@arduinos.delete("/<int:id>")
def delete(id):
    deleteArduino(id)
    return Response(status=204) 

@arduinos.get("/<int:id>/dati/")
@jwt_required()
def findDati(id):
    sub = get_jwt_identity()
    if id != sub:
        return Response(response="access is not allowed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')
    
    result = findArduinoDati(id)
    return Response(response=json.dumps(result), status=HTTPStatus.OK, content_type='application/json')

@arduinos.post("/<int:id>/dati/")
@jwt_required()
def createDati(id):
    sub = get_jwt_identity()
    if id != sub:
        return Response(response="access is not allowed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')
    
    tipo,valore,valoretx = request.json['tipo'],request.json['valore'],request.json['valoretx'] 
    result = createArduinoDati(id,tipo,valore,valoretx)
    return Response(response=json.dumps(result), status=HTTPStatus.CREATED, content_type='application/json')