#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
import pymongo


def log_stats():
    """Returns some stats about Nginx logs stored in MongoDB"""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.logs
    logs = db.nginx

    print("{} logs".format(logs.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(
            method, logs.count_documents({"method": method})))
    print("{} status check".format(logs.count_documents(
        {"method": "GET", "path": "/status"})))


if __name__ == "__main__":
    log_stats()
