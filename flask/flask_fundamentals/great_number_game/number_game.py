from flask import Flask, render_template, request, redirect, session 
import random 	            # import the random module

app = Flask(__name__)
app.secret_key = 'my_super_secret_key'

@app.route('/')
def index():
    if 'randomguess' not in session:
        print("randomguess not in session")
        print("@"*20)
        session['randomguess']=random.randint(1, 100)
        session['counter'] = 5
    if session['counter'] <= 0:
        session['counter'] = 5
        print(int(session['counter']))
    if 'displaymsg' not in session:
        print("displaymsg not in session")
        session['displaymsg']="startpage"
        print(session['displaymsg'])
    #session['counter']+=1
    return render_template("index.html", jinja_num=session['randomguess'], jinja_dispmsg=session['displaymsg'], jinja_counter=session['counter'])

@app.route('/guess', methods=["POST"])
def guess():
    print("+="*20)
    print("guessing...")
    session['counter'] = session['counter']  - 1
    print("#@"*20)
    print(session['counter'])
    if int(session['counter'])  <= 0:
        return redirect('/gameover')
    # I added in in client side validation for key presses. This will catch pasted text.
    try:
        int(request.form['myguess'])
    except:
        print("string detected")
        return redirect('/')
    if int(request.form['myguess']) > session['randomguess']:
        session['displaymsg']="toohigh"
    elif int(request.form['myguess']) < session['randomguess']:
        session['displaymsg']="toolow"
    elif int(request.form['myguess']) == session['randomguess']:
        session['displaymsg']="correct"
    else:
        session['displaymsg']="unknown"
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    print("in reset")
    [print(key) for key in list(session.keys())]
    session['randomguess']=int(random.randint(1, 100))
    print(session['randomguess'])
    session['displaymsg']="startpage"
    #session.clear() #needed for sensei bonus
    session['counter']=0
    return redirect('/')

@app.route('/gameover')
def gameover():
    print("in game over")
    [print(key) for key in list(session.keys())]
    session['randomguess']=int(random.randint(1, 100))
    print(session['randomguess'])
    session['displaymsg']="gameover"
    #session.clear() #needed for sensei bonus
    session['counter']=5
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
