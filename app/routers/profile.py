from flask import Blueprint, request

import skin_system

bp = Blueprint('profile', __name__)

@bp.route('/profile/<username>')
@skin_system.token_required(0)
def func(username):
    username = skin_system.DB.what_redirect_of(username, 'ely')

    url = f"http://skinsystem.ely.by/profile/{username['ely']}"

    unsigned = request.args.get('unsigned', default='true', type=str)

    url = f"{url}?unsigned={unsigned}"

    return skin_system.resolve(url)