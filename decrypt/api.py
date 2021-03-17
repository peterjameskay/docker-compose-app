from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/decrypt")
def message_func2():
    return render_template("form2.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)