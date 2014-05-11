# -*- coding: utf-8 -*-
from mod_python import apache, Session
from tools import _Head
def index(req):
    '''menue principale de l\'application'''

    #Définie le type mine
    req.content_type = "text/html;charset=UTF-8"

    return _Head('''<center><h2>Inscription des concurents</h2><table border=0>
    
    <tr>
        <td>
            <input type="button" name="adda" value="Ajouter un senior" onclick="self.location.href='inscription'">
        </td>
        <td>
            <input type="button" name="addj" value="Ajouter un jeune" onclick="self.location.href='inscription?jeune=on'">
        </td>
    </tr>
    </table>
    <br><br>
    <h2>Modifier un dossard</h2>

    <FORM METHOD=GET ACTION="modifier">Dossard : <INPUT type=text name="dossard"><INPUT type="submit" value="Modifier"></Form>
    <br><br>
    
    <h2>Rechercher un dossard</h2>
    <FORM METHOD=POST ACTION="recherche">
    &nbsp&nbsp&nbsp&nbsp Nom : <INPUT type=text name="nom"><br>
    Prenom : <INPUT type=text name="prenom"><br>
    <INPUT type="submit" value="Rechercher"></Form>
    

    <h2>Pointer les temps</h2>
    <input type="button" name="addj" value="Pointer" onclick="self.location.href='pointage'">

    <br><br>
    <h2>Attributions des coupes</h2>
    <input type="button" name="coupes" value="Attribution coupes" onclick="self.location.href='coupes'">

    <br><br>
    <h2>Afficher des statistiques</h2>
    <table style="text-align: left;" border="0" cellpadding="2"
    <tr>
        <td><input type="button" name="equipes" value="Equipes" onclick="self.location.href='stats/equipes'">
        </td
        <td><input type="button" name="lesplus" value="Les plus ..." onclick="self.location.href='stats/lesplus'">
        </td
        <td><input type="button" name="origine" value="Origine" onclick="self.location.href='stats/origine'">
        </td
        <td><input type="button" name="chiffres" value="Les chiffres" onclick="self.location.href='stats/chiffres'">
        </td
        <td><input type="button" name="etat" value="Abandon/absents" onclick="self.location.href='stats/etat'">
        </td
    </tr>
    </table>
    
    <br><br>
    <h2>Afficher les resultat</h2>

    <input type="button" name="seniorsg" value="Classement Général Séniors" onclick="self.location.href='resultat?categorie=seniorsg'">
    <input type="button" name="juniorsg" value="Classement Général Juniors" onclick="self.location.href='resultat?categorie=juniorsg'">
    <br><br>
    <table style="text-align: left;" border="0" cellpadding="2"
    cellspacing="2">
    <tbody>
    <tr>
        <td style="text-align:center; vertical-align: top; width: 100px">Equipes
        </td>
        <td style="vertical-align: top; border:0px; width: 85px">
        </td>
        <td style="text-align:center; vertical-align: top; width: 100px">Individuels
        </td>
        <td style="vertical-align: top; border:0px; width: 85px">
        </td>
        <td style="text-align:center; vertical-align: top; width: 100px">Pietons
        </td>
        <td style="vertical-align: top; border:0px; width: 85px">
        </td>
        <td style="text-align:center; vertical-align: top; width: 100px">Vtt
        </td>
    </tr>
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorse" value="Séniors" onclick="self.location.href='resultat?categorie=seniorse'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorsi" value="Séniors" onclick="self.location.href='resultat?categorie=seniorsi'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorsp" value="Séniors" onclick="self.location.href='resultat?categorie=seniorsp'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorsv" value="Séniors" onclick="self.location.href='resultat?categorie=seniorsv'">
        </td>
    </tr>
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="masculinese" value="Masculines" onclick="self.location.href='resultat?categorie=masculinese'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorshi" value="Séniors Hommes" onclick="self.location.href='resultat?categorie=seniorshi'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorshp" value="Séniors Hommes" onclick="self.location.href='resultat?categorie=seniorshp'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorshv" value="Séniors Hommes" onclick="self.location.href='resultat?categorie=seniorshv'">
        </td>
    </tr>
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="femininese" value="Féminines" onclick="self.location.href='resultat?categorie=femininese'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorsfi" value="Sénior Femmes" onclick="self.location.href='resultat?categorie=seniorsfi'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorsfp" value="Sénior Femmes" onclick="self.location.href='resultat?categorie=seniorsfp'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="seniorsfe" value="Sénior Femmes" onclick="self.location.href='resultat?categorie=seniorsfv'">
        </td>
    </tr>

   <tr>
        <td style="text-align:center; vertical-align: top;">----------
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">----------
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">----------
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">----------
        </td>
    </tr>

    
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorsv" value="Juniors" onclick="self.location.href='resultat?categorie=juniorse'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorsi" value="Juniors" onclick="self.location.href='resultat?categorie=juniorsi'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorsp" value="Juniors" onclick="self.location.href='resultat?categorie=juniorsp'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorsv" value="Juniors" onclick="self.location.href='resultat?categorie=juniorsv'">
        </td>
    </tr>
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="masculinesje" value="Masculines" onclick="self.location.href='resultat?categorie=masculinesje'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorshi" value="Juniors Hommes" onclick="self.location.href='resultat?categorie=juniorshi'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorshp" value="Juniors Hommes" onclick="self.location.href='resultat?categorie=juniorshp'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorshv" value="Juniors Hommes" onclick="self.location.href='resultat?categorie=juniorshv'">
        </td>
    </tr>
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="femininesje" value="Féminines" onclick="self.location.href='resultat?categorie=femininesje'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorsfi" value="Juniors Femmes" onclick="self.location.href='resultat?categorie=juniorsfi'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorsfp" value="Juniors Femmes" onclick="self.location.href='resultat?categorie=juniorsfp'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="juniorsfv" value="Juniors Femmes" onclick="self.location.href='resultat?categorie=juniorsfv'">
        </td>
    </tr>

   <tr>
        <td style="text-align:center; vertical-align: top;">----------
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
    </tr>
    
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="mixtess" value="Mixtes séniors" onclick="self.location.href='resultat?categorie=mixtess'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
    </tr>
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="mistesj" value="Mixtes junior" onclick="self.location.href='resultat?categorie=mistesj'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
    </tr>
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="sj" value="Sénior/Junior" onclick="self.location.href='resultat?categorie=sj'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
    </tr>
    <tr>
        <td style="text-align:center; vertical-align: top;"><input style="width:130px" type="button" name="js" value="Junior/Sénior" onclick="self.location.href='resultat?categorie=js'">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
        <td style="vertical-align: top; border:0px;">
        </td>
        <td style="text-align:center; vertical-align: top;">
        </td>
    </tr>
    </tbody>
    </table>

    </center>
    ''')
