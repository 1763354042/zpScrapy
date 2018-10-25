import json


def get_keyWord(i):
    with open('keyWord.json','r',encoding='utf-8') as json_result:
        keyWord = json.load(json_result)["keyWord"][i]
        return keyWord

def get_keyWord_len():
    with open('keyWord.json','r',encoding='utf-8') as f:
        keyWordLen = json.load(f)["keyWord"]
        return len(keyWordLen)

