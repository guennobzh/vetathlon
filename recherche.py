# -*- coding: utf-8 -*-
from mod_python import apache, Session
from tools import _Head
from datab import _Datab
import re

def index(req, nom=None, prenom=None):
    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"

    #crée l'objet base de donnée
    objBdd = _Datab()

    #regarde si un formulaire a ete poster et traites les informations en retour
    if req.form.has_key('listd'):
        listd = re.findall("'([^']*)'", req.form['listd'])
        retour=''
        
        for dossar in listd:

            #Recupere l'id du pieton et du vététiste
            idP, idV = objBdd.execute("select pieton, vtt from dossards where numero = %s"%(dossar))[0]

            #teste si le pieton a son sertifica
            if req.form.has_key('certifp%s'%(dossar)):
                certifP = 1
            else:
                certifP = 0

            #test si il sagit d'une equipe et si s'ent est une test le sertifica du vététiste
            if idP != idV and req.form.has_key('certifv%s'%(dossar)):
                certifV = 1
            elif idP != idV:
                certifV = 0

            #teste si l'equipe a payer
            if req.form.has_key('payer%s'%(dossar)):
                payer = 1
            else:
                payer = 0

            #Met a jour la fiche du coureur
            objBdd.execute("update participants set certif = %s where id = %s;"%(certifP, idP))

            #Teste si il sagit d'une equipe et si c le cas met a jour la liscence du vetetiste
            if idP != idV :
                objBdd.execute("update participants set certif = %s where id = %s;"%(certifV, idV))

            #Met a jour la fiche du dossard
            objBdd.execute("update dossards set payer = %s where numero = %s;"%(payer, dossar))
            

    #Définie la valeur pas default de nom et prenom 
    nom = prenom = '%'
    
    #met en forme 
    if req.form.has_key('nom'):
        nom = '%'+req.form['nom']+'%'
    if req.form.has_key('prenom'):
        prenom = '%'+req.form['prenom']+'%'

    #Effectue la recherche demander
    resultat = objBdd.execute("select dossards.numero, dossards.vtt - dossards.pieton, concat(partip.nom,' ',partip.prenom),  partip.certif, concat(partiv.nom,' ',partiv.prenom), partiv.certif, dossards.payer from dossards, participants as partip, participants as partiv where partip.id = dossards.pieton and partiv.id = dossards.vtt and ((partip.nom like '%s' and partip.prenom like '%s') or (partiv.nom like '%s' and partiv.prenom like '%s'));"%(nom, prenom, nom, prenom))

    #Crée l'entéte du tableau
    retour = '''<center><FORM METHOD=POST ACTION="recherche">
    <table border="1">
     <tbody><h1>Resultat de le recherche</h1>
      <tr class="tete-tableau">
       <td style="text-align: center; width: 100px;"></td>
       <td colspan="2" style="text-align: center;">Courreur</td>
       <td colspan="2" style="text-align: center;">Vététiste</td>
       <td style="text-align: center; width: 100px;"></td>
      </tr>
      <tr class="tete-tableau">
       <td style="text-align: center; width: 100px;">Dossard</td>
       <td style="text-align: center; width: 200px;">Nom</td>
       <td style="text-align: center; width: 100px;">Certificat</td>
       <td style="text-align: center; width: 200px;">Nom</td>
       <td style="text-align: center; width: 100px;">Certificat</td>
       <td style="text-align: center; width: 100px;">Payer</td>
      </tr>
    '''
    
    #crée une liste vide pour contenire tous les numero de dossards
    listd =[]

    #crée la vatiable pour la couleur des ligne paire
    lclass = 0
    
    #liste tous les resultat et ajoute une ligne pour chacun d'eu
    for infodossard in resultat:
        #Ajoute le numero de dossards a la liste
        listd.append(str(infodossard[0]))


        if infodossard[3]:
            checkCP = 'checked'
        else:
            checkCP = ''

        #Test si le coureurvététiste a son certificat
        if infodossard[5]:
            checkCV = 'checked'
        else:
            checkCV = ''

        #Test si l'teqipe a payer
        if infodossard[6]:
            checkP = 'checked'
        else:
            checkP = ''

        #débinie la class css de la ligne
        if lclass == 0:
            classl = 'l-impaire'
            lclass = 1
        else:
            classl = 'l-paire'
            lclass = 0

        #test si il s'agit d'une equipe
        if infodossard[1] != 0:
            colnom= '''
            <td style="text-align: center;">%s</td>
            <td style="text-align: center;"><INPUT type="checkbox" name="certifp%s" %s></td>
            <td style="text-align: center;">%s</td>
            <td style="text-align: center;"><INPUT type="checkbox" name="certifv%s" %s></td>
            <INPUT type="hidden" value="on" name="solo%s">'''%(infodossard[2], infodossard[0], checkCP, infodossard[4], infodossard[0], checkCV, infodossard[0])
        else:
            colnom= '''
            <td colspan="3" style="text-align: center;">%s</td>
            <td style="text-align: center;"><INPUT type="checkbox" name="certifp%s" %s></td>
            '''%(infodossard[2], infodossard[0], checkCP)


        retour += '''<tr class="%s">
        <td style="text-align: right;"><a href="modifier?dossard=%s">%s<a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</td>
        %s
        <td style="text-align: center;"><INPUT type="checkbox" name="payer%s" %s></td>
        </tr>
        '''%(classl, infodossard[0], infodossard[0], colnom, infodossard[0], checkP)
    retour += '</tbody></table><INPUT type="hidden" value="%s" name="listd"><INPUT type="hidden" value="%s" name="nom"><INPUT type="hidden" value="%s" name="prenom"><INPUT type="submit" value="Envoyer"></FORM>'%(str(listd),  nom.replace('%',''), prenom.replace('%',''))
    
    return _Head(retour)
