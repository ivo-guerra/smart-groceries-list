from mongoengine import connect


def get_connection(connection_string, database_name):
    connect(host=connection_string + database_name)
