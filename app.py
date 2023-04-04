from flask import Flask, request, render_template 
import pickle

app = Flask(__name__,template_folder='templates',static_folder='static')
model = pickle.load(open('./mlTraining/university.pkl','rb'))

@app.route('/',methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/predictionForm',methods=['GET'])
def predictionForm():
    return render_template('form.html')



@app.route('/result',methods=['POST'])
def result():
    

    # userData = [337,118,4,4.5,4.5,9.65,1]  # This values have chance
    # userData = [220,50,2,1,3,8,0]  # This values don't have chance

    min = [290.0, 92.0, 1.0, 1.0, 1.0, 6.8, 0.0]
    max = [340.0, 120.0, 5.0, 5.0, 5.0, 9.92, 1.0]

    k = [float(x) for x in request.form.values()]
    p = []

    for i in range(7):
        l = (k[i]-min[i]) / (max[i]-min[i])
        p.append(l)

    prediction = model.predict([p])
    # print(prediction)

    output = prediction[0] 

    if(output == False):
        return render_template('result.html', prediction_text="You don't have a chance")
    else:
        return render_template('result.html',prediction_text="You have a chance")


