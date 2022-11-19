#This api its to the emails

from flask import Flask, jsonify, request
app = Flask(__name__)

emails = [
    {
        'id': 1,
        'email': 'My email is: jooj',
        'author': 'Charles Dantas'
    },
    {
        'id': 2,
        'email': 'livro baum toma aqui meu email e me cobre',
        'author': 'jooj'
    },
]
@app.route('/emails',methods=['POST'])
def include_new_email():
    new_email = request.get_json()
    emails.append(new_email)
    return jsonify(emails)

@app.route('/emails', methods=['GET'])
def get_emails():
    return jsonify(emails)


@app.route('/email/<int:id>', methods=['GET'])
def get_emails_by_id(id):
    for email in emails:
        if email.get('id') == id:
            return jsonify(email)
        

@app.route('/emails/<int:id>', methods=['PUT'])
def edit_email_by_id(id):
    email_alter = request.get_json()
    for indice, email in enumerate(emails):
        if email.get('id') == id:
            emails[indice].update(email_alter)
            return jsonify(emails[indice])   
        
@app.route('/emails/<int:id>',methods=['DELETE'])
def delete_email(id):
    for indice, email in enumerate(emails):
        if email.get('id') == id:
            del emails[indice]

    return jsonify(emails) 


app.run(debug=True)