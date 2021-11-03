from flask import *  
import requests
import jsonify
import json
import os
import csv

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
        column_name = []
        row_1 = []
        row_2 = []
        row_3 = []
        row_4 = []
        row_5 = []
        row_6 = []
        row_7 = []
        row_8 = []
        row_9 = []
        row_10 = []
        row_11 = []
        row_12 = []
        row_13 = []
        for i in range(len(data)):
            if data[i]['row']==1:
                column_name.append(data[i]['text'])
            elif data[i]['row']==2:
                row_1.append(data[i]['text'])
            elif data[i]['row']==3:
                row_2.append(data[i]['text'])
            elif data[i]['row']==4:
                row_3.append(data[i]['text'])
            elif data[i]['row']==5:
                row_4.append(data[i]['text'])
            elif data[i]['row']==6:
                row_5.append(data[i]['text'])
            elif data[i]['row']==7:
                row_6.append(data[i]['text'])
            elif data[i]['row']==8:
                row_7.append(data[i]['text'])
            elif data[i]['row']==9:
                row_8.append(data[i]['text'])
            elif data[i]['row']==10:
                row_9.append(data[i]['text'])
            elif data[i]['row']==11:
                row_10.append(data[i]['text'])
            elif data[i]['row']==12:
                row_11.append(data[i]['text'])
            elif data[i]['row']==13:
                row_12.append(data[i]['text'])
            elif data[i]['row']==14:
                row_13.append(data[i]['text'])
        total_rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11, row_12, row_13]
        filename_csv = "table_"+f.filename+".csv"
        with open(filename_csv, 'w', encoding='utf-8') as f:
            write = csv.writer(f)
            write.writerow(column_name)
            write.writerows(total_rows)
        d = json.dumps(total_rows)
        return(d), 200 
  
if __name__ == '__main__':  
    app.run(debug = True)