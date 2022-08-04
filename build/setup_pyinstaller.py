import os
from shutil import rmtree, copytree

import PyInstaller.__main__

# 获取相关路径
projectName = 'VideoToAudio'
vision = 'v1.0'
curpath = os.path.abspath(os.path.dirname(__file__))
basedir = curpath[:curpath.find(projectName) + len(projectName)]
print('当前路径:', curpath, '项目', basedir)
# 复制资源文件到脚本路径
sourceDir = basedir + '\\icons'
targetDir = curpath + '\\icons'
if not os.path.exists(targetDir):
    os.makedirs(targetDir)
rmtree(targetDir)
copytree(sourceDir, targetDir)
# 执行脚本
PyInstaller.__main__.run([
    '-F',
    f'-n={projectName}_{vision}',
    '--windowed',
    '-i=./icons/audio.ico',
    basedir + '/main.py'
])
