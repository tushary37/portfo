from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_text(data)
        write_to_csv(data)
        return redirect('/thanku.html')
    else:
        return 'Something went wrong'

def write_to_text(data):
    with open('datafile.txt','a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"{email},{subject},{message}")

def write_to_csv(data):
    with open('data.csv',newline='',mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        msg='\n'
        csv_writer= csv.writer(database2,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #csv_writer.writeheader()
        csv_writer.writerow([email,subject,message])




