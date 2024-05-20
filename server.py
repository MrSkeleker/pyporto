from flask import Flask, render_template, request, redirect
import csv
import os
app = Flask(__name__)

database_filename = 'database.csv'

if not os.path.exists(database_filename):
    # Create the file if it doesn't exist
    with open(database_filename, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the headers to the CSV file
        writer.writerow(['email', 'subject', 'message'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def route(page_name):
    return render_template(f'{page_name}.html')


def save_contact(data):
    with open(database_filename, mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']

        writer_writer = csv.writer(
            database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            save_contact(data)
            return redirect('/thankyou')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
