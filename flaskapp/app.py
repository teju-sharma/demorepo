from flask import Flask,render_template
from flask import request,redirect,url_for
import os
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('Reg.html')
@app.route('/register', methods=['GET', 'POST']) 
def register():
 if request.method == 'POST': 
    name = request.form['name'] 
    email = request.form['email']
    password = request.form['password']
    # Store the user data in a database or file
    return render_template('Success.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


