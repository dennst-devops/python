# Dennis S
# checkerboard
from flask import Flask, render_template
app = Flask(__name__) 

color1="red"
color2="black"
# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def default():
    return render_template("index.html", row=int(8), col=int(8), mycolor1=color1, mycolor2=color2)

# http://localhost:5000/4 - should display 8 by 4 checkerboard
# it may be nice to check for a 0 and display a message if it does
@app.route('/<int:row>')
def rowchoice(row):
    return render_template("index.html", row=int(row), col=int(8), mycolor1=color1, mycolor2=color2)

# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  
# For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  
# Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)
@app.route('/<int:row>/<int:col>')
def multiplay(row, col):
    return render_template("index.html", row=int(row), col=int(col), mycolor1=color1, mycolor2=color2)

# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  
# For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  
# Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)
@app.route('/<int:row>/<int:col>/<color1>/<color2>')
def multiplaycolor(row, col, color1, color2):
    return render_template("index.html", row=int(row), col=int(col), mycolor1=color1, mycolor2=color2)
    # should probably check to see if the colors are the same and return a message or alert if they are
    
if __name__=="__main__":
    app.run(debug=True)
