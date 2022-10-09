from flask import Flask, abort
from markupsafe import escape
from argparse import ArgumentParser
from obj.product_doc import Product
from mongo import mongodb

app = Flask(__name__)


# Test Links
# http://127.0.0.1:5000/product/0024000160113
#


@app.route('/product/<bar_code>')
def show_product(bar_code):
    app.logger.info(f'Starting Product Route for id %s', bar_code)

    q_set = Product.objects(code=bar_code)
    products = [ob for ob in q_set]

    if len(products) > 0:
        product = products[0]
        return f'Product: {escape(product.product_name)} Grade: {escape(product.nutrition_grade_fr)}'
    else:
        app.logger.info(f'No product found with id: %s', bar_code)
        abort(404)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--mongo_address')
    parser.add_argument('--mongo_database')
    args = parser.parse_args()

    # TODO set password!!
    my_db = mongodb.get_connection(args.mongo_address, args.mongo_database)

    app.run(debug=True)
