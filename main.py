from flask import Flask,render_template,request
import smtplib
import requests

app = Flask(__name__)
OWN_EMAIL = "spamhereacc111@gmail.com"
OWN_PASSWORD = "spam_account123"


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/contact", methods = ["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_message(data["txtName"],data["txtEmail"],data["txtPhone"],data["txtMsg"])
    return render_template("contact.html")




@app.route("/payment", methods = ["GET", "POST"])
def payment():
    if request.method == "POST":
        data = request.form
        try:
            send_email(data["username"],data["MyName"],data["amount"],data["Address"],data["state"],data["City"],data["cardNumber"])
        except:
            return render_template("payment.html")
        else:
            return render_template("payment.html", msg_sent = True)
    return render_template("payment.html", msg_sent = False)

def send_email(mail,name,amount,Address,state,city,cnum):
    email_message = f"Dear Recipient,\nYour Receipt,\nRecipient MailId : {mail}\nName                : {name}\nAmount             : {amount}\nAddress            : {Address}\nState                 :{state}\nCity                   :{city}\nACC.Number     : {cnum}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL,OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL,to_addrs=mail,msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)

