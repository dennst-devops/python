# Dennis S
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# localhost:5000/ - have it say "Hello World!"
@app.route('/')
def hello_world():
    return 'Hello World!'

# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def hello_dojo():
    return 'Dojo!'

# Create one url pattern and function that can handle the following examples:
@app.route('/say/<name>')
def say(name):
    return "Hi, " + str.capitalize(name) +"!"

#Create one url pattern and function that can handle the following examples
#ninja bonus: int:howmany
@app.route('/repeat/<int:howmany>/<whattosay>')
def repeat(howmany, whattosay):
    int(howmany)
    return (whattosay)*(int(howmany))

#sensei bonus:
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
