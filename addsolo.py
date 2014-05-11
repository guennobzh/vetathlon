# -*- coding: utf-8 -*-
from mod_python import apache, Session
from datab import _Datab
from tools import _Head, _checkVarSolo
from formulaires import _formsolo
import time, re

def index(req):
    '''Crée l\'entrée pour un coureur sole apres avoir tester si toutes les entrées sont correcte
    et reproposer le sormulaire si nesesaire'''
    
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

    dicArgum = _checkVarSolo(dicArgum)
    
    #Si il y a une erreure repropose le formulaire avec le message d'erreur
    if dicArgum['txterr']:
        retour = '<center><H1>Dossard N° %s</H1></center>'%(dicArgum['dossard'])
        retour += _formsolo('addsolo', nom=dicArgum['nom'], prenom=dicArgum['prenom'], daten=dicArgum['daten'], sexe=dicArgum['sexe'], commune=dicArgum['commune'], idcommune=dicArgum['idcommune'], dept=dicArgum['dept'], mail=dicArgum['mail'], dossard=dicArgum['dossard'], certi=dicArgum['certi'], payer=dicArgum['payer'], error=dicArgum['txterr'])
        return _Head(retour)

    #si tout est bon ajoute l'entrée dans la base de donnée
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

        #Ajoute l'entrée dans la base participant          
        idPart = objBdd.insert("INSERT INTO `participants` (`id` ,`nom` ,`prenom` ,`date_nais` ,`sexe` ,`certif` ,`commune` ,`departement` ,`mail`)VALUES (NULL , '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(dicArgum['nom'], dicArgum['prenom'], date, dicArgum['sexe'], dicArgum['certi'], dicArgum['idcommune'], dicArgum['dept'], dicArgum['mail']))

        #teste si le dossard n'a pas ete ajouter entre temps et boucle jusqu'a qu'il soit unique
        nDosChance = False
        if objBdd.execute("select `numero` from `dossards` where `numero` = '%s'"%(dicArgum['dossard'])):
            while objBdd.execute("select `numero` from `dossards` where `numero` = '%s'"%(dicArgum['dossard'])):
                dicArgum['dossard'] = str(int(dicArgum['dossard'])+1)
                nDosChance = True
        
        #Ajoute l'entrée dans la base dossard
        objBdd.execute("INSERT INTO `dossards` (`numero`, `pieton`, `vtt`, `payer`, `etat`, `tmp_pieton`, `tmp_vtt`, `tmp_total`) values ('%s', '%s', '%s', '%s', '0', '00:00:00', '00:00:00', '00:00:00');"%(dicArgum['dossard'], idPart, idPart, dicArgum['payer']))

        if nDosChance:
            return _Head('''<center><font color="red"><h2>Attention Le numero de dossard a changer <br>Le nouveau numero pour %s %s est le %s</h2></font><br><br>
            <table border=0>
    
        <tr>
            <td>
                <input type="button" name="adda" value="Ajouter un senior" onclick="self.location.href='inscription'">
            </td>
            <td>
                <input type="button" name="addj" value="Ajouter un jeune" onclick="self.location.href='inscription?jeune=on'"
            </td>
        </tr>
        </table>
        <input type="button" name="adda" value="Retourner au menu" onclick="self.location.href='index'">
            </center>'''%(dicArgum['nom'], dicArgum['prenom'], dicArgum['dossard']))
        else:
            return _Head('''<center><h2>Le dossard N°%s a bien ete ajouter pour %s %s</h2><br><br>
   
        <tr>
            <td>
                <input type="button" name="adda" value="Ajouter un senior" onclick="self.location.href='inscription'">
            </td>
            <td>
                <input type="button" name="addj" value="Ajouter un jeune" onclick="self.location.href='inscription?jeune=on'"
            </td>
        </tr>
        </table>
        <input type="button" name="adda" value="Retourner au menu" onclick="self.location.href='index'">

            </center>'''%(dicArgum['dossard'], dicArgum['nom'], dicArgum['prenom']))
