# -*- coding: utf-8 -*-
from mod_python import apache, Session
import sys
from datab import _Datab
from tools import _Head



def index(req, dossard=0):
    '''Modifier un dossard'''

    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"

    #si aucun dossard n'est demander
    if dossard == 0 or not dossard:
        return _Head('<center><h1>Veuillez entrée un numero de dossard</h1><center>')

    #Crée l'objet base de donnée
    objBdd = _Datab()

    #Recupere les informations consernant le dossard
    infoDossard = objBdd.execute("select * from dossards where numero = %s"%(dossard))

    #Si aucun dossard ne correspond avec celui demander retourne une erreure
    if not infoDossard:
        return _Head('<center><h1>Le numere de dossard est incorecte</h1><center>')

    infoDossard = infoDossard[0]
    
    #Si il sagit d'un coureur en solo
    if infoDossard[1] == infoDossard[2]:
        return _Head('<meta http-equiv="refresh" content="0;URL=modifsolo?dossard=%s">'%(dossard))
    else:
        return _Head('<meta http-equiv="refresh" content="0;URL=modifequipe?dossard=%s">'%(dossard))
