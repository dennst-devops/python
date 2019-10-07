# Dennis S
# Dojo Survey
from flask import Flask, render_template, request, redirect  # added request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
# add these later:  , ice, chkbox
def process():
    print("*"*40)
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    loc_from_form = request.form['location']
    lang_from_form = request.form['language']
    comment_from_form = request.form['message']
    ice_from_form = request.form['ice']
    #checkboxes don't work...
    # veh_from_form  = request.form['Car']
    # veh_from_form  += request.form['Boat']
    return redirect(f'/result/{name_from_form}/{loc_from_form}/{lang_from_form}/{ice_from_form}/{comment_from_form}')

@app.route('/result/<route_name>/<route_loc>/<route_lang>/<route_ice>/<route_comment>')
def result(route_name, route_loc, route_lang, route_ice, route_comment):
    print("+"*40)
    print("Got results Info")
    return render_template("show.html", jinja_name=route_name, jinja_loc=route_loc, jinja_lang=route_lang, jinja_ice=route_ice, jinja_comment=route_comment)

if __name__ == "__main__":
    app.run(debug=True)
