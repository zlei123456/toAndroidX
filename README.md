# toAndroidX

CN
1: 在 gradle.properties 文件中中添加下面的代码：
   android.useAndroidX=true
   android.enableJetifier=true
 
2: 点击 Android Studio 导航条的 Refactor 中的 Migrate to androidx, 即可一键转为 androidX

3: 把 androidx-class-mapping.csv和 toAndroidX.py 拷贝到工程目录下。 执行 toAndroidX.py 文件。（如果不想在功能目录下，可以修改python中的目录）


EN
1: add code to gradle.properties:
   android.useAndroidX=true
   android.enableJetifier=true 

2: in  Android Studio   Refactor->Migrate to androidx 

3: copy  androidx-class-mapping.csv and toAndroidX.py to project root direction, then run toAndroidX.py (if you donot copy to root direction, you can change something in toAndroidX.py)


    "react": "16.8.3",
    "react-native": "^0.59.4",
    and more...
