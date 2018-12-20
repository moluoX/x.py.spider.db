from pymongo import MongoClient


def get_client():
    return MongoClient('10.1.40.166', 27017)


def get_lagou():
    return get_client().lagou


def get_zdm():
    return get_client().zdm
