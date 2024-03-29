from flask import Flask, send_file, render_template, request
import os
import bulkMail
app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.csv']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sms')
def sms():
    return render_template('sms.html')

@app.route('/sendmail', methods=['GET', 'POST'])
def handleform():
   if request.method == 'POST':
       csvfile = request.files['csvFile']
       csvfile.save(csvfile.filename)
       smail = request.form.get("sendermail")
       spass = request.form.get("senderpass")
       ssub = request.form.get("sendersub")
       message = request.form.get("emailbody")

       emailSender = bulkMail.sendMail(csvfile.filename, smail, spass, ssub, message)
       return render_template('success.html', val = emailSender)

if __name__ == '__main__':
    app.run(debug= True)