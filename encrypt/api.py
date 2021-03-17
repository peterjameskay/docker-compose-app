from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/encrypt")
def message_func():
    return render_template("form1.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)