# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_Html = request.form.get('button_Html')
    button_proyect = request.form.get('button_proyect')
    return render_template('index.html', button_python=button_python
                           ,button_discord = button_discord
                           ,button_Html = button_Html
                           ,button_proyect = button_proyect)

@app.route('/respuestas', methods=['POST'])
def Sub_form():
    email = request.form["email"]
    text = request.form["text"]
    with open ("result.txt", "a",encoding="utf-8") as f:
        f.write(email+"    "+text+"\n")


    return render_template("result.html",
                           email = email,
                           text =text)

if __name__ == "__main__":
    app.run(debug=True)
