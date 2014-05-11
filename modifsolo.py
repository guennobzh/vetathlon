# -*- coding: utf-8 -*-
from mod_python import apache, Session
from tools import _Head, _checkVarSolo, _Zero
from datab import _Datab
from formulaires import _formsolo
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

    #recupere les informations sur le participant
    infoPart = objBdd.execute("select * from participants where id = %s"%(infoDossard[1]))[0]

    #mise en forme de la date de naissance
    daten=_Zero(infoPart[3].day)+'/'+_Zero(infoPart[3].month)+'/'+_Zero(infoPart[3].year)

    retour = '<center><h1>Modifier le dossard N°%s</h1></center>'%(dossard)
    retour += _formsolo('modifsolo/suite', nom=infoPart[1], prenom=infoPart[2], daten=daten, sexe=infoPart[4], idcommune=infoPart[6], dept=infoPart[7], mail=infoPart[8], dossard=dossard, certi=infoPart[5], payer=infoDossard[3], modif=1)
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
    dicArgum = _checkVarSolo(dicArgum)

    #Si il y a une erreure repropose le formulaire avec le message d'erreur
    if dicArgum['txterr']:
        retour = '<center><H1>Modifier le dossard N° %s</H1></center>'%(dossard)
        retour += _formsolo('suite', nom=dicArgum['nom'], prenom=dicArgum['prenom'], daten=dicArgum['daten'], sexe=dicArgum['sexe'], commune=dicArgum['commune'], idcommune=dicArgum['idcommune'], dept=dicArgum['dept'], mail=dicArgum['mail'], dossard=dossard, certi=dicArgum['certi'], payer=dicArgum['payer'], error=dicArgum['txterr'], modif=1)
        return _Head(retour)

    #si tout est ok ajoute les entrée dans la base de donnée
    else:
        #Met le sertifica en boleun
        if dicArgum['certi'] == 'on':
            dicArgum['certi'] = 1
        else:
            dicArgum['certi'] = 0

        #met le payment en boleun
        if dicArgum['payer'] == 'on':
            dicArgum['payer'] = 1
        else:
            dicArgum['payer'] = 0
            
        #Mise en forme de la date
        date = dicArgum['daten'].split('/')[2]+'-'+dicArgum['daten'].split('/')[1]+'-'+dicArgum['daten'].split('/')[0]

        #Si la commune n'existe pas regarde si une ortographe approcher existe sinon ajoute la a la base de donnée
        if dicArgum['commune']:
            dicArgum['idcommune'] = objBdd.insertCommune(dicArgum['commune'])

        #Recupere l'id du participant correspondant a ce dossard
        idParti = objBdd.execute("select pieton from dossards where numero=%s;"%(dicArgum['dossard']))[0][0]

        #Met a jour la base participant
        objBdd.execute("UPDATE `participants` SET `nom` = '%s', `prenom` = '%s', `date_nais` = '%s', `sexe` = '%s', `certif` = '%s', `commune` = '%s', `departement` = '%s', `mail` = '%s' WHERE `id` =%s;"%(dicArgum['nom'], dicArgum['prenom'], date, dicArgum['sexe'], dicArgum['certi'], dicArgum['idcommune'], dicArgum['dept'], dicArgum['mail'], idParti))

        #met a jout la base dossart
        objBdd.execute("UPDATE `dossards` SET `payer` = '%s' WHERE `numero` =%s;"%(dicArgum['payer'], dicArgum['dossard']))

        return  _Head('''<center><h2>Le dossard N°%s a bien ete mis a jour pour %s %s</h2><br><br>
        <input type="button" name="adda" value="Retourner au menu" onclick="self.location.href='../index'">

        </center>'''%(dicArgum['dossard'], dicArgum['nom'], dicArgum['prenom']))
