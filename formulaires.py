# -*- coding: utf-8 -*

from datab import _Datab

def _formsolo(url, nom='', prenom='', daten='', sexe='', commune='', idcommune=0, dept='', mail='', dossard='', certi='', error='', message='', payer=0, modif=0):
    '''retourne un formulaire de renseignement pour un concurent solo'''
    #Regarde si il sagit d'un homme ou d'une femme et met la fariable checked correspondant
    if str(sexe) == '2':
        checkH = 'checked'
        checkF = ''
    elif str(sexe) == '1':
        checkH = ''
        checkF = 'checked'
    else:
        checkH = ''
        checkF = ''
        
    #Regarde si le certifica est cocher
    if certi == 1 or certi == 'on':
        checkC = 'checked'
    else:
        checkC = ''
        

    #Regarde si payer est a cocher
    if payer == 1 or payer == 'on':
        checkP = 'checked'
    else:
        checkP = ''

    #Regarde si il safit d'une modification auquel cas il faut ajouter un bouton supprime
    if modif:
        supp = '''<input type="button" name="supprimer" value="Supprimer" onclick="self.location.href='del?dossard=%s'">'''%(dossard)
    else:
        supp = ''

    #genere le code pour le titre du formulaire
    if error:
        titre = '<font color="red"><h2>%s</h2></font>'%(error)
    elif message:
        titre = '<h2>%s</h2>'%(message)
    else:
        titre = ''

    #Si le mail est a none assigne lui un string vide
    if not mail :
        mail =''

    return '''<center><FORM METHOD=POST ACTION="%s"><table border=1>

        	%s
	<tr>
		<td align=right>
			Nom : <INPUT type=text name="nom" value="%s">
		</td>
		<td align=right>
			Prénom : <INPUT type=text name="prenom" value="%s">
                </td>
		<td align=right>
	                Date de naissance : <INPUT type=text name="daten" value="%s">
		</td>
		<td align=right>
		        Homme : <INPUT type=radio name="sexe" value="2" %s><br>Femme : <INPUT type=radio name="sexe" value="1" %s>
		</td>
		<td>
	</tr>

	 
	<tr>
		<td align=right>
		        Commune : <INPUT type=text name="commune" value="%s"><br><SELECT name="idcommune">%s</SELECT>
		</td>
		<td align=right>
		        Departement : <INPUT type=text name="dept" value="%s">
		</td>
		<td align=right>
		        Adresse mail : <INPUT type=text name="mail" value="%s">
		</td>
		<td align=right>
		        Certificat ou licence :  <INPUT type=checkbox name="certi" %s>
        </tr>
	</table><br>Payer : <INPUT type=checkbox name="payer" %s><br><INPUT type="hidden" value="%s" name="dossard"><INPUT type="submit" value="Envoyer Solo"></FORM>%s</center>
    
        '''%(url, titre, nom, prenom, daten, checkH, checkF, commune, _villes(idcommune), dept, mail, checkC, checkP, dossard, supp)


def _formequipe(url, nomc='', prenomc='', datenc='', sexec='', communec='', idcommunec=0, deptc='', mailc='', certic='', nomv='', prenomv='', datenv='', sexev='', communev='', idcommunev=0, deptv='', mailv='', certiv='', dossard='', payer=0, error='', message='', modif=0):

    #Regarde si il safit d'une modification auquel cas il faut ajouter un bouton supprime
    if modif:
        supp = '''<input type="button" name="supprimer" value="Supprimer" onclick="self.location.href='del?dossard=%s'">'''%(dossard)
    else:
        supp = ''


    #genere le code pour le titre du formulaire
    if error:
        titre = '<font color="red"><h2>%s</h2></font>'%(error)
    elif message:
        titre = '<h2>%s</h2>'%(message)
    else:
        titre = ''

    #Regarde si le coureur est un homme ou une femme et met la fariable checked correspondant
    if str(sexec) == '2':
        checkPH = 'checked'
        checkPF = ''
    elif str(sexec) == '1':
        checkPH = ''
        checkPF = 'checked'
    else:
        checkPH = ''
        checkPF = ''

    #Regarde si le vtt est un homme ou une femme et met la fariable checked correspondant
    if str(sexev) == '2':
        checkVH = 'checked'
        checkVF = ''
    elif str(sexev) == '1':
        checkVH = ''
        checkVF = 'checked'
    else:
        checkVH = ''
        checkVF = ''

    #Regarde si le certifica du coureur est cocher
    if certic =='on' or certic == 1:
        checkCC = 'checked'
    else:
        checkCC = ''

    #Regarde si le certifica du vvt est cocher
    if certiv =='on' or certiv == 1:
        checkVC = 'checked'
    else:
        checkVC = ''

    #Regarde si payer est a cocher
    if payer == 'on' or payer == 1:
        checkP = 'checked'
    else:
        checkP = ''

    #genere le code pour le titre du formulaire
    if error:
        titre = '<font color="red"><h2>%s</h2></font>'%(error)
    elif message:
        titre = '<h2>%s</h2>'%(message)
    else:
        titre = ''

    #Si le mail est a None assigne lui une string vide
    if not mailc:
        mailc = ''
    if not mailv:
        mailv=''
        
    return '''
        <center>
        %s
	
	<FORM METHOD=POST ACTION="%s"><table border=1>

	<h3>Courreur</h3>

	<tr>
		<td align=right>
			Nom : <INPUT type=text name="nomc" value="%s">
		</td>
		<td align=right>
			Penom : <INPUT type=text name="prenomc" value="%s">
                </td>
		<td align=right>
	                Date de naissance : <INPUT type=text name="datenc" value="%s">
		</td>
		<td align=right>
		        Homme : <INPUT type=radio name="sexec" value="2" %s><br>Femme : <INPUT type=radio name="sexec" value="1" %s>
		</td>
		<td>
	</tr>

	 
	<tr>
		<td align=right>
		        Commune : <INPUT type=text name="communec" value="%s"><br><SELECT name="idcommunec">%s</SELECT>
		</td>
		<td align=right>
		        Departement : <INPUT type=text name="deptc" value="%s">
		</td>
		<td align=right>
		        Adresse mail : <INPUT type=text name="mailc" value="%s">
		</td>
		<td align=right>
		        Certificat ou licence :  <INPUT type=checkbox name="certic" %s>
        </tr>
	</table>

	<h3>Vététiste</h3>

	<table border=1>
	<tr>
		<td align=right>
			Nom : <INPUT type=text name="nomv" value="%s">
		</td>
		<td align=right>
			Penom : <INPUT type=text name="prenomv" value="%s">
                </td>
		<td align=right>
	                Date de naissance : <INPUT type=text name="datenv" value="%s">
		</td>
		<td align=right>
		        Homme : <INPUT type=radio name="sexev" value="2" %s><br>Femme : <INPUT type=radio name="sexev" value="1" %s>
		</td>
		<td>
	</tr>

	 
	<tr>
		<td align=right>
		        Commune : <INPUT type=text name="communev" value="%s"><br><SELECT name="idcommunev">%s</SELECT>
		</td>
		<td align=right>
		        Departement : <INPUT type=text name="deptv" value="%s">
		</td>
		<td align=right>
		        Adresse mail : <INPUT type=text name="mailv" value="%s">
		</td>
		<td align=right>
		        Certificat ou licence :  <INPUT type=checkbox name="certiv" %s>
        </tr>
	</table><br>Payer : <INPUT type=checkbox name="payer" %s><br><INPUT type="hidden" value="%s" name="dossard"><INPUT type="submit" value="Envoyer equipe"></FORM>%s</center>
        '''%(titre, url, nomc, prenomc, datenc, checkPH, checkPF, communev, _villes(idcommunec), deptc, mailc, checkCC, nomv, prenomv, datenv, checkVH, checkVF, communev, _villes(idcommunev), deptv, mailv, checkVC, checkP, dossard, supp)
    
def _villes(select=0):
    '''retourne la liste des villes existantes en html'''

    #recupere la liste de toutes les villes dans la base de donnée
    objBdd = _Datab()
    lstVilles = objBdd.execute("select * from villes order by nom")

    #Crée la rafiable de retour vide
    retour = '<OPTION VALUE="0"></OPTION>'

    #Liste toutes les villes et ajoute une entrée pour chaque
    for ville in lstVilles:
        if int(select)==int(ville[0]):
            retour += '<OPTION VALUE="%s" selected>%s</OPTION>'%(ville[0], ville[1])
        else:
            retour += '<OPTION VALUE="%s">%s</OPTION>'%(ville[0], ville[1])

    return retour
