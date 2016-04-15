import requests
from datetime import datetime
import re


def wallGet(pars):
    request = requests.get('https://api.vk.com/method/wall.get?',params=pars)
    jsonList = request.json()["response"]
    while(True):
        print("DA")
        try:
            for i in range(1, pars['count']):
                print("DAAA?")
                text = jsonList[i].get('text')
                time = datetime.fromtimestamp(jsonList[i].get('date'))                    
                #print(text,time)
                with open('posts.txt', 'a', encoding='utf-8') as f:
                    f.write("============" + str(time.year) + ":" + str(time.month) + ":"+str(time.day)+"========\n")
                    f.write(text.replace('<br>','\n')+'\n')
        except Exception as e:
            print(e)
            return
        finally:
            pars['offset'] += 100
            jsonList = requests.get('https://api.vk.com/method/wall.get?',params=pars).json()['response']
    print(pars['offset'])
    return
          
def main():
    owner = input("Page:?")
    Id = re.findall(r'\/([A-z]+)$',owner)
    if Id:
        pars = {'domain':Id, 'offset': 0, 'count' : 100, 'filter' : 'owner'}
    else:
        pars = {'owner_id':re.findall(r'\/id(\d+)$',owner), 'offset': 0, 'count' : 100, 'filter' : 'owner'}
    wallGet(pars)




if __name__ == '__main__':
    main()
