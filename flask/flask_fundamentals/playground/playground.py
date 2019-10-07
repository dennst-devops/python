# Dennis S
# playground
from flask import Flask, render_template
app = Flask(__name__) 

# When a user visits http://localhost:5000/play, have it render three beautiful
# looking blue boxes. Please use a template to render this.
@app.route('/play')
def play():
    return render_template("index.html", color="aqua", times=3)

# When a user visits localhost:5000/play/(x),
# have it display the beautiful looking blue boxes x times. 
@app.route('/play/<int:mytimes>')
def multiplay(mytimes):
    return render_template("index.html", color="aqua", times=mytimes)

# When a user visits localhost:5000/play/(x)/(color), have it display beautiful
# looking boxes x times, but this time where the boxes appear in (color)
@app.route('/play/<int:mytimes>/<mycolor>')
def colorplay(mytimes, mycolor):
    return render_template("index.html", times=mytimes, color=mycolor)

if __name__=="__main__":
    app.run(debug=True)
