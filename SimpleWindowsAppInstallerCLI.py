import os
import sys
import requests

def current_path():
    print("Current working directory:")
    print(os.getcwd())



cwd = os.getcwd()

current_path()

os.chdir('../../../Downloads')
cwd = os.getcwd()

current_path()

defaultDownload_URL="https://go.microsoft.com/fwlink/?linkid=2187327&Lmsrc=groupChatMarketingPageWeb&Cmpid=directDownloadWin64&clcid=0x409&culture=en-us&country=us"
download_URL= ""
print("input download URL:")
download_URL= input()
if(len(download_URL)==0):
    download_URL = defaultDownload_URL

r=requests.get(download_URL,allow_redirects=True)

open('installer_file.exe','wb').write(r.content)





