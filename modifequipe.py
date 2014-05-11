# -*- coding: utf-8 -*-
from mod_python import apache, Session
from tools import _Head, _checkVarEquipe, _Zero
from datab import _Datab
from formulaires import _formequipe
import time

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
    infoDossard = objBdd.execute("select * from dossards where numero = %s"%(dossard))[0]

    #Si aucun dossard ne correspond avec celui demander retourne une erreure
    if not infoDossard:
        return _Head('<center><h1>Le numere de dossard est incorecte</h1><center>')

    #recupere les informations sur le coureur
    infoCour = objBdd.execute("select * from participants where id = %s"%(infoDossard[1]))[0]

    #recupere les informations sur le vététiste
    infoVtt = objBdd.execute("select * from participants where id = %s"%(infoDossard[2]))[0]

    #mise en forme de la date de naissance
    datenc=_Zero(infoCour[3].day)+'/'+_Zero(infoCour[3].month)+'/'+_Zero(infoCour[3].year)
    datenv=_Zero(infoVtt[3].day)+'/'+_Zero(infoVtt[3].month)+'/'+_Zero(infoVtt[3].year)

    retour = '<center><h1>Modifier le dossard N°%s</h1></center>'%(dossard)
    retour += _formequipe('modifequipe/suite', nomc=infoCour[1], prenomc=infoCour[2], datenc=datenc, sexec=infoCour[4], idcommunec=infoCour[6], deptc=infoCour[7], mailc=infoCour[8], certic=infoCour[5], nomv=infoVtt[1], prenomv=infoVtt[2], datenv=datenv, sexev=infoVtt[4], idcommunev=infoVtt[6], deptv=infoVtt[7], mailv=infoVtt[8], certiv=infoVtt[5], dossard=infoDossard[0], payer=infoDossard[3], modif=1)

    return _Head(retour)

def suite(req, dossard=0):
    
    #Crée l'objet base de donnée
    objBdd = _Datab()

    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"

    #teste si des variable ont ete passer en post sinon les recupere de la session
    if req.form:
        dicArgum = req.form

    #recupere les variable de la session
    else:
        req.session = Session.Session(req) 
        dicArgum = req.session

    #vérifie les variables et donne le message d'erreure si besoin
    dicArgum = _checkVarEquipe(dicArgum)

    #Si il y a une erreure repropose le formulaire avec le message d'erreur
    if dicArgum['txterr']:
        retour = '<center><H1>Modifier le dossard N° %s</H1></center>'%(dossard)
        retour += _formequipe('modifequipe/suite', nomc=dicArgum['nomc'], prenomc=dicArgum['prenomc'], datenc=dicArgum['datenc'], sexec=dicArgum['sexec'], idcommunec=dicArgum['idcommunec'], deptc=dicArgum['deptc'], mailc=dicArgum['mailc'], certic=dicArgum['certic'], nomv=dicArgum['nomv'], prenomv=dicArgum['prenomv'], datenv=dicArgum['datenv'], sexev=dicArgum['sexev'], idcommunev=dicArgum['idcommunev'], deptv=dicArgum['deptv'], mailv=dicArgum['mailv'], certiv=dicArgum['certiv'], dossard=dicArgum['dossard'], payer=dicArgum['payer'], error=dicArgum['txterr'], modif=1)
        return _Head(retour)

    #si tout est ok ajoute les entrée dans la base de donnée
    else:
        
            #Met le sertifica en boleun
        if dicArgum['certic'] == 'on':
            dicArgum['certic'] = 1
        else:
            dicArgum['certic'] = 0
        if dicArgum['certiv'] == 'on':
            dicArgum['certiv'] = 1
        else:
            dicArgum['certiv'] = 0

        #met le payment en boleun
        if dicArgum['payer'] == 'on':
            dicArgum['payer'] = 1
        else:
            dicArgum['payer'] = 0

        #Mise en forme de la date
        dicArgum['datec'] = dicArgum['datenc'].split('/')[2]+'-'+dicArgum['datenc'].split('/')[1]+'-'+dicArgum['datenc'].split('/')[0]
        dicArgum['datev'] = dicArgum['datenv'].split('/')[2]+'-'+dicArgum['datenv'].split('/')[1]+'-'+dicArgum['datenv'].split('/')[0]

        #Si la commune n'existe pas regarde si une ortographe approcher existe sinon ajoute la a la base de donnée
        if dicArgum['communec']:
           dicArgum['idcommunec'] = objBdd.insertCommune(dicArgum['communec'])

        if dicArgum['communev']:
           dicArgum['idcommunev'] = objBdd.insertCommune(dicArgum['communev'])

        #Recupere l'id du coureur correspondant a ce dossard
        idCour = objBdd.execute("select pieton from dossards where numero=%s;"%(dicArgum['dossard']))[0][0]

        #Recupere l'id du vététiste correspondant a ce dossard
        idVtt = objBdd.execute("select vtt from dossards where numero=%s;"%(dicArgum['dossard']))[0][0]

        #Met a jour la base participant pour le coureur
        objBdd.execute("UPDATE `participants` SET `nom` = '%s', `prenom` = '%s', `date_nais` = '%s', `sexe` = '%s', `certif` = '%s', `commune` = '%s', `departement` = '%s', `mail` = '%s' WHERE `id` =%s;"%(dicArgum['nomc'], dicArgum['prenomc'], dicArgum['datec'], dicArgum['sexec'], dicArgum['certic'], dicArgum['idcommunec'], dicArgum['deptc'], dicArgum['mailc'], idCour))

        #Met a jour la base participant pour le vététiste
        objBdd.execute("UPDATE `participants` SET `nom` = '%s', `prenom` = '%s', `date_nais` = '%s', `sexe` = '%s', `certif` = '%s', `commune` = '%s', `departement` = '%s', `mail` = '%s' WHERE `id` =%s;"%(dicArgum['nomv'], dicArgum['prenomv'], dicArgum['datev'], dicArgum['sexev'], dicArgum['certiv'], dicArgum['idcommunev'], dicArgum['deptv'], dicArgum['mailv'], idVtt))

        #met a jout la base dossart
        objBdd.execute("UPDATE `dossards` SET `payer` = '%s' WHERE `numero` =%s;"%(dicArgum['payer'], dicArgum['dossard']))

        return  _Head('''<center><h2>Le dossard N°%s a bien ete mis a jour pour %s %s</h2><br><br>
        <input type="button" name="adda" value="Retourner au menu" onclick="self.location.href='../index'">

        </center>'''%(dicArgum['dossard'], dicArgum['nomc'], dicArgum['nomv']))
