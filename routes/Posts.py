import os
import time as t
from datetime import datetime

from flask import request, jsonify, Blueprint, url_for

postBlueprint = Blueprint('postBlueprint', __name__)

posts = []


@postBlueprint.route('/post')
def create_post():
    file = request.files['postImage']
    file_name = str(request.form.get('user_id')) + "sdfdsfdsffsd" + ".jpg"

    file.save(os.path.join(postBlueprint.root_path, "static/post_images/", file_name))
    postUrl = url_for('static', filename="static/post_images/" + file_name)

    posts.append({
        'caption': request.form.get('caption'),
        'image': postUrl,
    })
    return jsonify({'status': 200, 'message': "Post Created", 'postImageUrl': postUrl})
