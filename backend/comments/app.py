#This api its to the comments

from flask import Flask, jsonify, request
app = Flask(__name__)

comments = [
    {
        'id': 1,
        'comment': 'My comment is: jooj',
        'author': 'Charles Dantas'
    },
    {
        'id': 2,
        'comment': 'livro baum',
        'author': 'jooj'
    },
]
@app.route('/comments',methods=['POST'])
def include_new_comment():
    new_comment = request.get_json()
    comments.append(new_comment)
    return jsonify(comments)

@app.route('/comments', methods=['GET'])
def get_comments():
    return jsonify(comments)


@app.route('/comment/<int:id>', methods=['GET'])
def get_comments_by_id(id):
    for comment in comments:
        if comment.get('id') == id:
            return jsonify(comment)
        

@app.route('/comments/<int:id>', methods=['PUT'])
def edit_comment_by_id(id):
    comment_alter = request.get_json()
    for indice, comment in enumerate(comments):
        if comment.get('id') == id:
            comments[indice].update(comment_alter)
            return jsonify(comments[indice])   
        
@app.route('/comments/<int:id>',methods=['DELETE'])
def delete_comment(id):
    for indice, comment in enumerate(comments):
        if comment.get('id') == id:
            del comments[indice]

    return jsonify(comments) 


app.run(debug=True)