import redis
import uuid

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True, charset="utf-8")


def CreateImage(path):
    last = client.get("last")
    id = None
    if last == None:
        id = 0
        client.set('last', 0)
    else:
        oldID = last
        id = int(oldID) + 1
        client.set('last', id)
        
    imageKey = f'P/{id}'
    client.set(imageKey, path)

    return id

def SetPoints(id, point):
    pointIndex = f'I/{id}'
    result = client.set(pointIndex, point)
    return int(result)

def GetPath(id):
    pathIndex = f'P/{id}'
    result = client.get(pathIndex)
    return result

def GetPoints(id):
    pointIndex = f'I/{id}'
    result = client.get(pointIndex)
    return int(result)
