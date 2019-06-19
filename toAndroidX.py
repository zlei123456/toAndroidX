# by lei
# coding: utf-8

import os
import time

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

nodeModulesDir = '../../db_story_center_p1/node_modules/'
for k in toMap:
    print(k)
    os.system('grep -rl \'' + k + '\' --include "*.java" ' + nodeModulesDir + ' | xargs sed -i "" "s/' + k + '/' + toMap[k] + '/g"')
    os.system('grep -rl \'' + k + '\' --include "*.xml" ' + nodeModulesDir + ' | xargs sed -i "" "s/' + k + '/' + toMap[k] + '/g"')

androidDir = '../../db_story_center_p1/android/'
for k in toMap:
    os.system('grep -rl \'' + k + '\' --include "*.java" ' + androidDir + ' | xargs sed -i "" "s/' + k + '/' + toMap[k] + '/g"')
print('aaa')