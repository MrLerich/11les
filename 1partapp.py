from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def page_main():
    '''
    Страничка Лабрадудля
    :return:
    '''
    return render_template("1part.html")


app.run(debug=True)
