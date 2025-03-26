from flask import Flask, redirect, url_for, render_template, request,jsonify
import os
from index import d_dtcn
import pandas as pd
from ResponseFetcher import handle_file_and_get_response
import json
import time


secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'csv', 'xlsx'} 

# Defining the home page of our site


@app.route("/", methods=['GET', 'POST'])
def home():
    print(request.method,"home")
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
            return render_template("test1.html")
    else:
        # pass # unknown
        return render_template("index.html")

# Directory to store uploaded files


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Function to process CSV file
def process_csv(file_path):
    try:
        df = pd.read_csv(file_path)  # Read CSV file using pandas
        print(df.to_string() )
        txt_file = os.path.join(app.config['UPLOAD_FOLDER'], 'output_txt.txt')
        df.to_csv(txt_file, sep='\t', index=False)
        txt=process_txt(txt_file)
        return txt  # Convert dataframe to string
    except Exception as e:
        return f"Error processing CSV file: {str(e)}"

# Function to process TXT file
def process_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except UnicodeDecodeError:
        # Fallback encoding if utf-8 fails
        with open(file_path, 'r', encoding='ISO-8859-1') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading text file: {str(e)}"

# Function to process XLSX file
def process_xlsx(file_path):
    try:
        # Read Excel file using pandas
        df = pd.read_excel(file_path, engine='openpyxl')  # Make sure 'openpyxl' is installed
        return df.to_string()  # Convert dataframe to string
    except Exception as e:
        return f"Error processing XLSX file: {str(e)}"



@app.route("/send", methods=["POST"])
def handle_data():
    if 'file' in request.files:
        # Handle file upload
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            # Process the file based on its extension
            file_extension = filename.rsplit('.', 1)[1].lower()
            if file_extension == 'csv':
                file_content = process_csv(filename)
            elif file_extension == 'txt':
                file_content = process_txt(filename)
            elif file_extension == 'xlsx':
                file_content = process_xlsx(filename)
            else:
                return jsonify({"error": "Unsupported file type."}), 400

            # Send file content to OpenAI
            print(file_content)
            response=handle_file_and_get_response(file_content)
            json_data = json.dumps(response)
            return json_data
        else:
            return jsonify({"error": "Invalid file type. Only TXT, CSV, and XLSX are allowed."}), 400

    elif 'text' in request.form:
        # Handle text input
        text = request.form['text']
        
        # Send text to OpenAI
        response=handle_file_and_get_response(text)
        json_data = json.dumps(response)
        return json_data
 
    else:
        return jsonify({"error": "No file or text provided"}), 400

@app.route("/loading")
def loading_page():
    return render_template("loading.html")

@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method,"start")
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            d_dtcn()

            return render_template("test1.html")
    else:
        # pass # unknown
        return render_template("test1.html")


@app.route('/contact', methods=['GET', 'POST'])
def cool_form():
    print(request.method,"contact")
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('contact.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    DL = output["Drivinglicsence"]
    #func(name)

    return render_template("driver_registration_form.html", name=name, Drivinglicsence=DL)

@app.route('/driver_registration_form', methods=['POST', 'GET'])
def showfunc():
    print(request.method)
    return render_template("driver_registration_form.html")



if __name__ == "__main__":
    app.run()
    
