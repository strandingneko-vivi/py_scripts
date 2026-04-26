import os
import random


def md5change(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for _ in dirs:      # 此处预留，以避免以后有其他需求
            continue
        for file in files:
            with open(file, 'a') as f:
                if file != 'md5changer.py':
                    f.write(str(random.random()))
                    print('{:<60}'.format(file), '{:>>5}'.format(''), 'md5 value has been changed.')


if __name__ == '__main__':
    path = r'E:\1.下载\迅雷下载\[XKsub][Hyouka][01-23][CHS_JAP][1080p][BDrip]'
    md5change(path)
    print('修改完成')
