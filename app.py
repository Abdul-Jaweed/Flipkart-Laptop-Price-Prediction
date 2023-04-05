from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model and data
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', pipe)

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    if request.method == 'GET':
         return render_template('home.html')
    # Retrieve values from form
    else:
        if request.method == 'POST':
            company = request.form['Brand Name']
            Os = request.form['OS']
            ramtype = request.form['Ram Type']
            ram = request.form['RAM']
            processor = request.form['Processor']
            gpu = request.form['GPU']
            warr = request.form['Warranty']
            screensize = request.form['ScreenSize']
            disktype = request.form['Disk Type']
            disksize = request.form['DISK SIZE']
        
        # Make prediction
            query = np.array([[company, Os, ramtype, ram, processor, gpu, warr, screensize, disktype, disksize]])
            prediction = int(pipe.predict(query)[0])
            
            return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
