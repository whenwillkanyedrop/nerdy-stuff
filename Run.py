import os
import urllib.request


if __name__== "__main__":
    print("downloadin dataset :3")
    zip_url  = "http://www.openslr.org/resources/45/ST-AEDS-20180100_1-OS.tgz"
    urllib.request.urlretrieve(zip_url, 'SLR45.tgz')

    print("organzing stuff")
    os.system('python3 Code/DataManager.py')

    print("trainin the .gmm stuffs")
    os.system('python3 Code/ModelsTrainer.py')

    print("identiffyig gender stuff")
    os.system('python3 Code/GenderIdentifier.py')
