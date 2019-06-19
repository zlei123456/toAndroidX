# toAndroidX

1: 在 gradle.properties 文件中中添加下面的代码：
   android.useAndroidX=true
   android.enableJetifier=true
 
2: 点击 Android Studio 导航条的 Refactor 中的 Migrate to androidx, 即可一键转为 androidX

3: 把 androidx-class-mapping.csv和 toAndroidX.py 拷贝到工程目录下。 执行 toAndroidX.py 文件。（如果不想在功能目录下，可以修改python中的目录）


   
