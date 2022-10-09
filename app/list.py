import json
from argparse import ArgumentParser

from bson import json_util
from flask import Flask, abort, jsonify
from flask import request
from markupsafe import escape
from mongoengine import connect
from pymongo.errors import ServerSelectionTimeoutError

from obj.list_doc import ListDoc
from obj.list_item import ListItem
from mongo import mongodb

app = Flask(__name__)


@app.route('/list_add/<user_id>', methods=['PUT'])
def add_list(user_id):
    app.logger.info(f'Starting List Route for user %s', user_id)

    # Form data
    data = request.form
    list_id = data.get("list_id")
    item_list = []

    for key in data:
        if 'list_item' in key:
            list_item = ListItem(item_name=data.get(key), item_id=key)
            item_list.append(list_item)

    # Creating Document
    document = ListDoc(user_id=user_id, list_id=list_id, item_list=item_list)

    app.logger.info(f'Inserting list: %s for user: %s', list_id, user_id)

    try:
        document.save()
    except ServerSelectionTimeoutError:
        abort(408)

    app.logger.info(f'Inserted list: %s for user: %s', list_id, user_id)

    return document


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--mongo_address')
    parser.add_argument('--mongo_database')
    args = parser.parse_args()

    # TODO set password!!
    my_db = mongodb.get_connection(args.mongo_address, args.mongo_database)
    app.run(debug=True)
