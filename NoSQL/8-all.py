def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    :param mongo_collection: pymongo collection object
    :return: list of documents
    """
    documents = mongo_collection.find()
    return list(documents)
