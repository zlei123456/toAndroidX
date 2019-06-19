# by lei
# coding: utf-8

import os
import time

 # 需要修改的目录。**************8  (need to change dir)
 # 需要自己写 nodeModules 目录   (nodeModules direction)
nodeModulesDir = './node_modules/'
# 需要自己写android目录   (android direction)
androidDir = './android/'
# *************

filePath = "./androidx-class-mapping.csv"
readFile = open(filePath, "r")
buf = readFile.read()
readFile.close()

toMap = {}
arr1 = buf.split('\n')
for v in arr1:
    print(v)
    arr2 = v.split(',')
    if (len(arr2) >= 2) :
        supportClass = arr2[0]
        androidXClass = arr2[1]
        toMap[supportClass] = androidXClass

print(toMap)
# toMap = {'android.support.v4.content.FileProvider': 'androidx.core.content.FileProvider'}


for k in toMap:
    print(k)
    os.system('grep -rl \'' + k + '\' --include "*.java" ' + nodeModulesDir + ' | xargs sed -i "" "s/' + k + '/' + toMap[k] + '/g"')
    os.system('grep -rl \'' + k + '\' --include "*.xml" ' + nodeModulesDir + ' | xargs sed -i "" "s/' + k + '/' + toMap[k] + '/g"')

for k in toMap:
    os.system('grep -rl \'' + k + '\' --include "*.java" ' + androidDir + ' | xargs sed -i "" "s/' + k + '/' + toMap[k] + '/g"')
print('over')