from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'my_super_secret_key' # set a secret key for security purposes
# our index route will handle rendering our form
# >>> import base64
# >>> base64.urlsafe_b64decode('eyJjb3VudGVyIjoxfQ===')
# b'{"counter":1}'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter']=0
    session['counter'] += 1
    return render_template("index.html", counter=session['counter'])

@app.route('/add2')
def add2():
    session['counter']+=1
    return redirect('/')

@app.route('/reset')
def reset():
    print("in reset")
    session['counter']=0
    session.pop("counter")
    session.clear() #needed for sensei bonus
    return redirect('/')

@app.route('/addmore', methods=["POST"])
def addmore():
    print("in addmore")
    print(request.form)
    # I added in in client side validation for key presses. This will catch pasted text.
    try:
        print("+="*20)
        int(request.form['addme'])
        print(request.form['addme'])
    except:
        print("string detected")
        return redirect('/reset')
    session['counter']+=int(request.form['addme'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
