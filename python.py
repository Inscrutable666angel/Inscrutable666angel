from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'This_is_a_code'

# Function to validate user credentials
def insert_user(email, phone, password):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Code__init__",
        database="users"
    )
    cursor = con.cursor()
    cursor.execute("insert into users (email, phone, password) values (%s, %s, %s)", (email, phone, password))
    con.commit()
    cursor.close()
    con.close()

# Route for the email page
@app.route('/sign_in_email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        session['email']=request.form['email']
        return redirect(url_for('sign_in_phone'))
    return render_template('sign_in_email.html')

# Route for the phone page
@app.route('/sign_in_phone', methods=['GET', 'POST'])
def phone():
    if request.method == 'POST':
        session['phone']=request.form['phone']
        return redirect(url_for('password'))
    return render_template('sign_in_phone.html')

# Route for the password page (might not be necessary since we handle this in /identifier)
@app.route('/password', methods=['POST'])
def password():
    if request.method=='POST':
        password = request.form['password']
        session.get('email')
        session.get('phone')
        if email and phone:
            insert_user(email,phone,password)
            return "User registered successfully!"
        else:
            return "Error: There has been some error... Sorry for the inconvenience!!!"
    return render_template('pass.html')

# Route for the success page
@app.route('/success')
def success():
    return "You have successfully signed in!"

if __name__ == '__main__':
    app.run(debug=True)