from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/encrypt/post", methods = ['POST'])
def encryptstr():
    #Ins and Outs
    message = request.form['message']
    newstring = str()
    ascii_letter_value = int()
    one_letter = str()
    new_ascii_value = int()
    #Loop to find index of message
    for i in range(0, len(message)):
        one_letter = message[i]
        ascii_letter_value = ord(one_letter)
        #If letters are z or Z
        if ascii_letter_value == 122:
            new_ascii_value = 97
        elif ascii_letter_value == 90:
            new_ascii_value = 65
        #All other letters
        else:
            new_ascii_value = ascii_letter_value + 1
        #Create Decrypted message
        newstring = newstring + chr(new_ascii_value)
    return render_template("back.html", result=newstring)

@app.route("/decrypt/post", methods = ['POST'])
def decryptstr():
    #Ins and Outs
    message = request.form['message2']
    newstring = str()
    ascii_letter_value = int()
    one_letter = str()
    new_ascii_value = int()
    #Loop to find index of message
    for i in range(0, len(message)):
        one_letter = message[i]
        ascii_letter_value = ord(one_letter)
        #If letters are A or a
        if ascii_letter_value == 97:
            new_ascii_value = 122
        elif ascii_letter_value == 65:
            new_ascii_value = 90
        #All other letters
        else:
            new_ascii_value = ascii_letter_value - 1
        #Create Encrypted message
        newstring = newstring + chr(new_ascii_value)
    return render_template("back.html", result=newstring)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
