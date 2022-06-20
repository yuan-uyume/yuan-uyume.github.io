import requests
import os
import json
import re
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import threading

notFields = ['sid' , 'status', 'image', 'like']

def copyNotFields(des, src):
    for field in notFields:
        if field in src:
            des[field] = src[field]

def getJson(path):
    with open(path, encoding="utf-8") as file:
        data = file.read()
        return json.loads(data)

def getNeedUpdate(json, finish):
    return list(filter(lambda d: 'sid' in d and (finish or 'title' not in d or 'isFinish' not in d or d['isFinish'] == 0), json))

def getOldData(json, finish):
    return list(filter(lambda d: not ('sid' in d and (finish or 'title' not in d or 'isFinish' not in d or d['isFinish'] == 0)), json))

def uploadImg(url):
    file = requests.get(url+'@138w_175h.webp', timeout=10).content
    link = uploadSM(file)
    return link if link else url

def uploadSM(file):
    try:
        result = requests.post('https://sm.ms/api/v2/upload', headers= {
            'Authorization': 'qIXhqY2kUjAmLMzfvNyfd4FORwkeYhp2'
        }, files= {
            'smfile': file
        }, timeout=15)
        data = result.json()
    except Exception:
        return None
    finally:
        return data['data']['url'] if data['success'] else data['images']

def getInfoFromBL(obj):
    result = requests.get('https://api.bilibili.com/pgc/view/web/season?season_id=' + obj['sid']).json()['result']
    info = {
        'mid': result['media_id'],
        'title': result['title'],
        'type': result['type'],
        'areas': result['areas'],
        'cover': result['cover'],
        'evaluate': result['evaluate'],
        'new_ep': result['new_ep'],
        'publish': result['publish'],
        'share_url': result['share_url'],
        'seasons': result['seasons']
    }
    copyNotFields(info, obj)
    # 获取番剧标签
    result = requests.get("https://www.bilibili.com/bangumi/media/md" + str(info['mid'])).text
    tags = re.search('<span class="media-tags" style="opacity:0;">(<span class="media-tag">.*</span>)*</span></div>', result)
    if tags:
        tags = tags.group(1)
    tags = tags.replace(' class="media-tag"', '')
    info['andTwo'] = tags
    return info

def getOutData(data):
    season = list(filter(lambda d: str(d['season_id']) == data['sid'], data['seasons']))
    if season:
        season = season[0]
    out = {
        'title': data['title'],
        'state': (data['new_ep']['desc'] +', 最新集数' + data['new_ep']['title']) if data['publish']['is_finish'] == 0 else data['new_ep']['desc'],
        'badge': season['badge_info'],
        'isFinish': data['publish']['is_finish'],
        'release': data['publish']['pub_time'],
        'isNew': 'is-new' if data['new_ep']['is_new'] == 1 else '',
        'andOne': "<span>" + ('番剧' if data['type'] == 1 else ('电影' if data['type'] == 2 else '未知')) +"</span><i></i><span>"+ data['areas'][0]['name'] +"</span>",
        'andTwo': data['andTwo'],
        'url': data['share_url'],
        'info': data['evaluate'],
    }
    copyNotFields(out, data)
    if 'image' not in out:
        image = uploadImg(data['cover'])
        if image:
            out['image'] = image
    return out


def parseObj(obj):
    info = getInfoFromBL(obj)
    out = getOutData(info)
    return out

def getOutFileJSON(path, finish):
    jsonn = getJson(path)
    need = getNeedUpdate(jsonn,finish)
    if need and len(need) > 0:
        old = getOldData(jsonn, finish)
        size = 6 if len(need) > 6 else len(need)
        pool = ThreadPoolExecutor(max_workers=size)
        allTask = [ ]
        for obj in need:
            task = pool.submit(parseObj, obj)
            allTask.append(task)
        wait(allTask, return_when=ALL_COMPLETED)
        outData = [task.result() for task in allTask]
        pool.shutdown()
        if outData and len(outData) > 0:
            return json.dumps(outData + old, ensure_ascii=False, indent=2)
        else:
            return json.dumps(jsonn, ensure_ascii=False, indent=2)
    else:
        return json.dumps(jsonn, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    outFile = getOutFileJSON('animes.json', True)
    print(outFile)
    with open('animes.json', 'w', encoding="utf-8") as file:
        file.write(outFile)