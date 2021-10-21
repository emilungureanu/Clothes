from flask import Flask, url_for, redirect, render_template, request, session, flash, send_from_directory
import sqlite3 #pachetele instalate

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "miau" #parola extrem de grea

#redirect pe home
@app.route("/")
def default():
    return redirect(url_for("home"))

@app.route("/home")
def home():
            return render_template("index.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    global email_input, password_input
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        conn = sqlite3.connect("login.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users")

       
        email_input = request.form["email_input"]
        password_input = request.form["password_input"]


        se_afla_in_baza_de_date = False
        for lista_informatie in c.fetchall():
            if email_input == lista_informatie[0] and password_input == lista_informatie[1]:
                se_afla_in_baza_de_date = True 
        
        if se_afla_in_baza_de_date == True:
            session["email_input"] = email_input
            session["password_input"] = password_input

            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))
        




if __name__ == "__main__":
    app.run(debug=True)
