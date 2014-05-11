# -*- coding: utf-8 -*-
from mod_python import apache, Session
from datab import _Datab
from tools import _Head, _checkVarEquipe
from formulaires import _formequipe
import time, re

def index(req):
    
    '''Crée l\'entrée pour une equipe apres avoir tester si toutes les entrées sont correcte
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

    dicArgum = _checkVarEquipe(dicArgum)

    #Si il y a une erreure repropose le formulaire avec le message d'erreur
    if dicArgum['txterr']:
        
        retour = '<center><H1>Dossard N° %s</H1></center>'%(dicArgum['dossard'])
        retour += _formequipe('addequipe', nomc=dicArgum['nomc'], prenomc=dicArgum['prenomc'], datenc=dicArgum['datenc'], sexec=dicArgum['sexec'], communec=dicArgum['communec'], idcommunec=dicArgum['idcommunec'], deptc=dicArgum['deptc'], mailc=dicArgum['mailc'], certic=dicArgum['certic'], nomv=dicArgum['nomv'], prenomv=dicArgum['prenomv'], datenv=dicArgum['datenv'], sexev=dicArgum['sexev'], communev=dicArgum['communev'], idcommunev=dicArgum['idcommunev'], deptv=dicArgum['deptv'], mailv=dicArgum['mailv'], certiv=dicArgum['certiv'], dossard=dicArgum['dossard'], payer=dicArgum['payer'], error=dicArgum['txterr'])
        return _Head(retour)

    #si tout est bon ajoute les entrées dans la base de donnée
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

        #Ajoute les entrées dans la base participant          
        idPartc = objBdd.insert("INSERT INTO `participants` (`id` ,`nom` ,`prenom` ,`date_nais` ,`sexe` ,`certif` ,`commune` ,`departement` ,`mail`)VALUES (NULL , '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(dicArgum['nomc'], dicArgum['prenomc'], dicArgum['datec'], dicArgum['sexec'], dicArgum['certic'], dicArgum['idcommunec'], dicArgum['deptc'], dicArgum['mailc']))
        idPartv = objBdd.insert("INSERT INTO `participants` (`id` ,`nom` ,`prenom` ,`date_nais` ,`sexe` ,`certif` ,`commune` ,`departement` ,`mail`)VALUES (NULL , '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(dicArgum['nomv'], dicArgum['prenomv'], dicArgum['datev'], dicArgum['sexev'], dicArgum['certiv'], dicArgum['idcommunev'], dicArgum['deptv'], dicArgum['mailv']))

        #teste si le dossard n'a pas ete ajouter entre temps et boucle jusqu'a qu'il soit unique
        nDosChance = False
        if objBdd.execute("select `numero` from `dossards` where `numero` = '%s'"%(dicArgum['dossard'])):
            while objBdd.execute("select `numero` from `dossards` where `numero` = '%s'"%(dicArgum['dossard'])):
                dicArgum['dossard'] = str(int(dicArgum['dossard'])+1)
                nDosChance = True

        #Ajoute l'entrée dans la base dossard
        objBdd.execute("INSERT INTO `dossards` (`numero`, `pieton`, `vtt`, `payer`, `etat`, `tmp_pieton`, `tmp_vtt`, `tmp_total`) values ('%s', '%s', '%s', '%s', '0', '00:00:00', '00:00:00', '00:00:00');"%(dicArgum['dossard'], idPartc, idPartv, dicArgum['payer']))

        #Affiche un message de confirmation
        if nDosChance:
            return _Head('''<center><font color="red"><h2>Attention Le numero de dossard a changer <br>Le nouveau numero pour l\'equipe %s %s est le %s</h2></font><br><br>
  
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

            </center>'''%(dicArgum['nomc'], dicArgum['nomv'], dicArgum['dossard']))
        else:
            return _Head('''<center><h2>Le dossard N°%s a bien ete ajouter pour l\'équipe %s %s</h2><br><br>
  
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

            </center>'''%(dicArgum['dossard'], dicArgum['nomc'], dicArgum['nomv']))
