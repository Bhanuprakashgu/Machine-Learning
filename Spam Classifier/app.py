from flask import Flask,render_template,request
import pickle

app = Flask(__name__)


model = pickle.load(open("spam_classifier.pkl","rb"))

@app.route('/', methods=["GET","POST"])
def main_function():
    if request.method == "POST":
        text = request.form
        # print(text)
        emails = text['email']
        print(emails)
        
        list_email = [emails]
        # print(list_email)
        output = model.predict(list_email)[0]
        print(output)


        return render_template("show.html", prediction = output)
    
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)