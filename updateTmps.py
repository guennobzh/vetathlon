# -*- coding: utf-8 -*-
from mod_python import apache, Session
from tools import _Head
from datab import _Datab
import re

def index(req):
    '''traite les modification sur les temps et l\'etat des equipes'''
    #Recupere la liste des dossards traiter
    listd = re.findall("'([^']*)'", req.form['listd'])

    #crée l'objet base de donnée
    objBdd = _Datab()
    retour = ''
    #Liste tous les dossars traiter et modifie la base de donnée
    for dossar in listd:
        #Recupere les informations envoyer correspondant au dossard traiter
        tmpPiet, tmpTot, etat = req.form['tp%s'%(dossar)], req.form['tt%s'%(dossar)], req.form['etat%s'%(dossar)]

        #Si un temps total est entrée calcule le temps vtt
        if tmpTot != '00:00:00' and tmpTot != '0:00:00':
            objBdd.execute("update `dossards` set etat='%s', tmp_total = '%s', tmp_pieton = '%s', tmp_vtt = SEC_TO_TIME(TIME_TO_SEC(tmp_total) - TIME_TO_SEC(tmp_pieton)) where numero = %s"%(etat, tmpTot, tmpPiet, dossar))

        #Sinon calcule rien
        else:
            objBdd.execute("update `dossards` set etat='%s', tmp_total = '%s', tmp_pieton = '%s' where numero = %s"%(etat, tmpTot, tmpPiet, dossar))

    return _Head('<meta http-equiv="refresh" content="0;URL=pointage">')
