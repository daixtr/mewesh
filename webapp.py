import sys
import os
import random
from flask import *
from functools import wraps
import time
from datetime import timedelta
import re

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(seconds = 60*5)

@app.errorhandler(404)
def page_not_found(error):
    print "ERROR 404: " + str(error)
    return redirect(url_for('home'))

@app.errorhandler(500)
def page_not_found(error):
    print "ERROR 500"
    return redirect(url_for('home'))

@app.route('/takealook')
def takealook():
    print "*** here ***"     
    D = {}
    path = '/home/daixtr/mewesh/static/sessions/'
    sessio = list(sorted(os.listdir(path)))
    for f in sessio:
        print f
    sessions = reversed(sessio)
    print sessions
    return render_template('takealook.html',sessions=sessions,public = 0)

@app.route('/',methods=['GET','POST'])
def home():
    session.permanent = True
    if request.method == 'POST':
        userident = request.form['username']
        userpass = request.form['password']
			
    L = request.args.getlist('session')
    if len(L) > 0:
        sessionfile = L[0]

        print "QUERYSTRING %s" % sessionfile
        f = "/home/daixtr/mewesh/static/sessions/" + sessionfile
        if os.path.exists(f): 
            return render_template('replay.html',sess = sessionfile,wid = getdim(f),public = 0)
        else:
            return render_template('missing.html',sess = sessionfile)
    else:
        return render_template('index.html',showlogin = False)

# a better getdim that reads into the js tty file rather than basing it 
# from logbook meta file
def getdim(f):
    with open(f,'r') as myfile:
        data = myfile.read()
    m = re.search('setCols",0,[0-9]+',data)
    extract = m.group(0)
    w1 = int(extract.split(',')[-1])
    ww = (w1 + w1%2) * 8
    dim = str(ww) + "px"
    return dim

@app.route('/replay/<sessionfile>')
def replay(sessionfile):
    path = '/home/daixtr/mewesh/static/sessions/'
    f = path + sessionfile
    if os.path.exists(f): 
        return render_template('replay.html',sess = sessionfile,wid = getdim(f),public =1 )
    else:
        return render_template('missing.html',sess = sessionfile)
        #return redirect(url_for('home'))

if __name__ == '__main__':
    port = 8000 
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            app.run(debug=False,host='0.0.0.0',port=port)
            #app.run(debug=True,port=port)
        except:
            print "invalid port parameter"
    else:
        app.run(debug=False,host='0.0.0.0',port=port)
        #app.run(debug=True,port=port)
