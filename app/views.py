
from flask import request, redirect, render_template, g

from app import app


@app.route('/')
def main():
    return "hell world"


@app.route('/hello')
def shit():
    return "hello"


@app.route('/i/<id>')
def test1(id):
    return render_template('_layout.html', something=id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=18080, debug=True)
