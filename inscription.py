# -*- coding: utf-8 -*-
from mod_python import apache, Session
from tools import _Head
from datab import _Datab
from formulaires import _formsolo, _formequipe


def index(req, jeune=''):
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"

    #Définie la variable de retour
    retour = ''

    #Crée l'objet base de donnée
    objBdd = _Datab()

    #Determine le numero du prochain dossard attribuable
    #Si il s'agit de jeunes
    if jeune:
        dossard = objBdd.nextDossard(True)
    #si il sagit d'adulte
    else:
        dossard = objBdd.nextDossard(False)

    #Ajoute le numero de dossard comme titre
    retour += '<center><H1>Dossard N° %s</H1>'%(dossard)

    #Ajoute le formulaire d'inscription solo
    retour += _formsolo('addsolo', dossard=dossard, message='Ajout d\'un particimant solo')

    #Ajoute quelques retour a la ligne
    retour += '<br><br><br><br><br>'

    #Ajoute le formulaire d'inscription d'une equipe
    retour += _formequipe('addequipe', dossard=dossard, message='Ajout d\'un equipe')

    return _Head(retour)

    
