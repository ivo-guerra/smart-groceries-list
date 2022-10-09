# Start MongoDB after having it installed with brew
mongod --config /opt/homebrew/etc/mongod.conf

# Start product micro-service passing proper arguments
python app/product.py --mongo_address 'mongodb://127.0.0.1:27017/' --mongo_database 'smart-groceries-list'


