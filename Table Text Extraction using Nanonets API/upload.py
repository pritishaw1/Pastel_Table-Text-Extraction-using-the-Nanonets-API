from flask import *  
import requests
import jsonify
import json
import os

url = 'https://app.nanonets.com/api/v2/OCR/Model/7d17f0c3-0e82-4107-a1b4-b508795ab9c6/LabelFile/'

app = Flask(__name__)  
app.config["IMAGE_UPLOADS"] = "C:/Users/Priti/Desktop/Flask/"
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)
        data = {'file': open(f.filename, 'rb')}
        response = requests.post(url, auth=requests.auth.HTTPBasicAuth('A_JgAogIx4wG5PHRKEIxW9fIyK8J3h9_', ''), files=data)
        data = response.json()
        data = data['result']
        data = data[0]['prediction']
        data = data[0]['cells']
        list_1 = []
        list_2 = []
        list_3 = []
        list_4 = []
        list_5 = []
        list_6 = []
        for i in range(len(data)):
            if data[i]['col']==1:
                list_1.append(data[i]['text'])
            elif data[i]['col']==2:
                list_2.append(data[i]['text'])
            elif data[i]['col']==3:
                list_3.append(data[i]['text'])
            elif data[i]['col']==4:
                list_4.append(data[i]['text'])
            elif data[i]['col']==5:
                list_5.append(data[i]['text'])
            elif data[i]['col']==6:
                list_6.append(data[i]['text'])
        list = [list_1, list_2, list_3, list_4, list_5, list_6]
        d = json.dumps(list)
        return(d), 200 
  
if __name__ == '__main__':  
    app.run(debug = True)