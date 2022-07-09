# 目前有两种安装方式

- 从action下载wheel ```pip install xxx.whl```

之后吧那个找不到的so文件放进/usr/lib

- pip install pycurl-antitls==7.45.3rc1

之后把so放进/usr/lib

挪so文件其实可以自动完成
```
# 如果有多个虚拟环境，刚才哪个python安装的curl，就用哪个python执行这个
import sys
import os

base = os.path.join(sys.prefix, "lib", "libcurl-impersonate-chrome.so")

with open(base, "rb") as inp, open("/usr/lib/libcurl-impersonate-chrome.so.4","wb") as out:
    data = inp.read()
    out.write(data)
```
因此，安装后执行上面的就行了

### 综上，你的so文件得在/usr/lib找得到 不能一键安装是[py的限制](https://docs.python.org/3/distutils/setupscript.html#installing-additional-files)