import wikipedia as wiki
import spacy 
from flask import Flask, render_template,url_for,request
from spacy import displacy
from flaskext.markdown import Markdown

ner_Obj = spacy.load("en_core_web_sm")

app = Flask(__name__)
Markdown(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getData',methods=["POST"])
def getData():
    if request.method=="POST":
        data = request.form['searchtext']
        try:
            datasearch = wiki.page(str(data)).content
            NerData = ner_Obj(datasearch)
            result = displacy.render(NerData,style='ent')
            return render_template('result.html',rawtext= datasearch,result = result)
        except:
            return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
