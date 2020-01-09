import requests

def download(id):
    i=1
    while i<=200:
        target = 'http://output.nsfc.gov.cn/report/61/'+str(id)+'_'+str(i)+'.png'
        print(i)
        req = requests.get(url=target, timeout=100)
        img = req.content
        dir = '../自然基金结项项目下载文件夹/' + str(id) + '_' + str(i) + '.png'
        with open(dir, 'wb') as f:
            f.write(img)
        i += 1

if __name__ == '__main__':
    id = input("请输入需要下载的项目编号: ")
    download(id)
