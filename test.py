# -*- coding: utf-8 -*
from mod_python import apache, Session

def index(req):
     return '''<html>
     <FORM METHOD=GET ACTION="test/test">
     Nom : <INPUT type=text name="nomc">
     <INPUT type="hidden" value="%s" name="dossard"><INPUT type="submit" value="Envoyer equipe">


     </html>'''

def test(req):
    if not req.form :
         return 'a rien'
    req.session = Session.Session(req)
    req.session['argum'] = req.form
    req.session.save() 
    return '''<html><a href="/vetathlon/test/test2">suite</a></html>'''

def test2(req):
    req.session = Session.Session(req) 
    return req.session['argum']
 
