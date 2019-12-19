'''
@Author: your name
@Date: 2019-12-10 23:17:00
@LastEditTime: 2019-12-17 20:32:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit#
@FilePath: \python\vscode\flask\flask1.py
'''
# 开始flask项目的步骤：
# 1. 安装python环境
# 2. 检验python和pip是否安装好
# 3. 新建项目文件夹
# 4. 安装virtualenv(为什么要虚拟环境)
# 5. 使用pipenv（安装pipenv pip install pipenv) 
#   =>使用pipenv创建一个虚拟环境，这个虚拟环境和项目是绑定的，
#   =>即创建一个新的项目，就要安装一个新的虚拟环境(pipenv install)
'''
E:\study\python\vscode\flask\fisher>pipenv install
Creating a virtualenv for this project…
Pipfile: E:\study\python\vscode\flask\fisher\Pipfile
Using d:\install\anaconda3\python.exe (3.7.4) to create virtualenv…
[  ==] Creating virtual environment...Already using interpreter d:\install\anaconda3\python.exe
Using base prefix 'd:\\install\\anaconda3'
  No LICENSE.txt / LICENSE found in source
New python executable in C:\Users\Lenovo\.virtualenvs\fisher-iWThc5xD\Scripts\python.exe
Installing setuptools, pip, wheel...
done.

Successfully created virtual environment!
Virtualenv location: C:\Users\Lenovo\.virtualenvs\fisher-iWThc5xD
Creating a Pipfile for this project…
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Updated Pipfile.lock (a65489)!
Installing dependencies from Pipfile.lock (a65489)…
  ================================ 0/0 - 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
E:\study\python\vscode\flask\fisher>pip list
Package                            Version
---------------------------------- ----------
absl-py                            0.8.1
alabaster                          0.7.12
anaconda-client                    1.7.2
anaconda-navigator                 1.9.7
anaconda-project                   0.8.3
asn1crypto                         1.0.1
astor                              0.8.0
astroid                            2.3.3
astropy                            3.2.1
atomicwrites                       1.3.0
attrs                              19.2.0
Babel                              2.7.0
backcall                           0.1.0
backports.functools-lru-cache      1.5
backports.os                       0.1.1
backports.shutil-get-terminal-size 1.0.0
backports.tempfile                 1.0
backports.weakref                  1.0.post1
beautifulsoup4                     4.8.0
bitarray                           1.0.1
bkcharts                           0.2
bleach                             3.1.0
bokeh                              1.3.4
boto                               2.49.0
Bottleneck                         1.2.1
certifi                            2019.9.11
cffi                               1.12.3
chardet                            3.0.4
Click                              7.0
cloudpickle                        1.2.2
clyent                             1.2.2
colorama                           0.4.1
comtypes                           1.1.7
conda                              4.7.12
conda-build                        3.18.9
conda-package-handling             1.6.0
conda-verify                       3.4.2
contextlib2                        0.6.0
cryptography                       2.7
cycler                             0.10.0
Cython                             0.29.13
cytoolz                            0.10.0
dask                               2.5.2
decorator                          4.4.0
defusedxml                         0.6.0
dill                               0.3.1.1
distributed                        2.5.2
docutils                           0.15.2
entrypoints                        0.3
et-xmlfile                         1.0.1
fast-histogram                     0.7
fastcache                          1.1.0
filelock                           3.0.12
Flask                              1.1.1
fsspec                             0.5.2
future                             0.17.1
gast                               0.3.2
gevent                             1.4.0
glob2                              0.7
glue-core                          0.15.6
glue-vispy-viewers                 0.12.2
glueviz                            0.15.2
greenlet                           0.4.15
grpcio                             1.25.0
h5py                               2.9.0
HeapDict                           1.0.1
html5lib                           1.0.1
idna                               2.8
imageio                            2.6.0
imagesize                          1.1.0
importlib-metadata                 0.23
ipykernel                          5.1.2
ipython                            7.8.0
ipython-genutils                   0.2.0
ipywidgets                         7.5.1
isort                              4.3.21
itsdangerous                       1.1.0
jdcal                              1.4.1
jedi                               0.15.1
Jinja2                             2.10.3
joblib                             0.13.2
json5                              0.8.5
jsonschema                         3.0.2
jupyter                            1.0.0
jupyter-client                     5.3.3
jupyter-console                    6.0.0
jupyter-core                       4.5.0
jupyterlab                         1.1.4
jupyterlab-server                  1.0.6
Keras-Applications                 1.0.8
Keras-Preprocessing                1.1.0
keyring                            18.0.0
kiwisolver                         1.1.0
lazy-object-proxy                  1.4.3
libarchive-c                       2.8
llvmlite                           0.29.0
locket                             0.2.0
lxml                               4.4.1
Markdown                           3.1.1
MarkupSafe                         1.1.1
matplotlib                         3.1.1
mccabe                             0.6.1
menuinst                           1.4.16
mistune                            0.8.4
mkl-fft                            1.0.14
mkl-random                         1.1.0
mkl-service                        2.3.0
mock                               3.0.5
more-itertools                     7.2.0
mpl-scatter-density                0.6
mpmath                             1.1.0
msgpack                            0.6.1
multipledispatch                   0.6.0
navigator-updater                  0.2.1
nbconvert                          5.6.0
nbformat                           4.4.0
networkx                           2.3
nltk                               3.4.5
nose                               1.3.7
notebook                           6.0.1
numba                              0.45.1
numexpr                            2.7.0
numpy                              1.16.5
numpydoc                           0.9.1
olefile                            0.46
openpyxl                           3.0.0
packaging                          19.2
pandas                             0.25.1
pandocfilters                      1.4.2
parso                              0.5.1
partd                              1.0.0
path.py                            12.0.1
pathlib2                           2.3.5
patsy                              0.5.1
pep8                               1.7.1
pickleshare                        0.7.5
Pillow                             6.2.0
pip                                19.2.3
pipenv                             2018.11.26
pkginfo                            1.5.0.1
plotly                             4.3.0
pluggy                             0.13.0
ply                                3.11
prometheus-client                  0.7.1
prompt-toolkit                     2.0.10
protobuf                           3.10.0
psutil                             5.6.3
py                                 1.8.0
pycodestyle                        2.5.0
pycosat                            0.6.3
pycparser                          2.19
pycrypto                           2.6.1
pycurl                             7.43.0.3
pyflakes                           2.1.1
Pygments                           2.4.2
pylint                             2.4.4
pyodbc                             4.0.27
PyOpenGL                           3.1.1a1
pyOpenSSL                          19.0.0
pyparsing                          2.4.2
pyreadline                         2.1
pyrsistent                         0.15.4
PySocks                            1.7.1
pytest                             5.2.1
pytest-arraydiff                   0.3
pytest-astropy                     0.5.0
pytest-doctestplus                 0.4.0
pytest-openfiles                   0.4.0
pytest-remotedata                  0.3.2
python-dateutil                    2.8.0
pytz                               2019.3
PyWavelets                         1.0.3
pywin32                            223
pywinpty                           0.5.5
PyYAML                             5.1.2
pyzmq                              18.1.0
QtAwesome                          0.6.0
qtconsole                          4.5.5
QtPy                               1.9.0
requests                           2.22.0
retrying                           1.3.3
rope                               0.14.0
ruamel-yaml                        0.15.46
scikit-image                       0.15.0
scikit-learn                       0.21.3
scipy                              1.3.1
seaborn                            0.9.0
Send2Trash                         1.5.0
setuptools                         41.4.0
simplegeneric                      0.8.1
singledispatch                     3.4.0.3
six                                1.13.0
snowballstemmer                    2.0.0
sortedcollections                  1.1.2
sortedcontainers                   2.1.0
soupsieve                          1.9.3
Sphinx                             2.2.0
sphinxcontrib-applehelp            1.0.1
sphinxcontrib-devhelp              1.0.1
sphinxcontrib-htmlhelp             1.0.2
sphinxcontrib-jsmath               1.0.1
sphinxcontrib-qthelp               1.0.2
sphinxcontrib-serializinghtml      1.1.3
sphinxcontrib-websupport           1.1.2
spyder                             3.3.6
spyder-kernels                     0.5.2
SQLAlchemy                         1.3.9
statsmodels                        0.10.1
sympy                              1.4
tables                             3.5.2
tblib                              1.4.0
tensorboard                        1.13.1
tensorflow-estimator               1.13.0
tensorflow-gpu                     1.13.1
termcolor                          1.1.0
terminado                          0.8.2
testpath                           0.4.2
toolz                              0.10.0
tornado                            6.0.3
tqdm                               4.36.1
traitlets                          4.3.3
typed-ast                          1.4.0
unicodecsv                         0.14.1
urllib3                            1.24.2
virtualenv                         16.7.8
virtualenv-clone                   0.5.3
wcwidth                            0.1.7
webencodings                       0.5.1
Werkzeug                           0.16.0
wheel                              0.33.6
widgetsnbextension                 3.5.1
win-inet-pton                      1.1.0
win-unicode-console                0.5
wincertstore                       0.2
wrapt                              1.11.2
xlrd                               1.2.0
XlsxWriter                         1.2.1
xlwings                            0.15.10
xlwt                               1.3.0
zict                               1.0.0
zipp                               0.6.0

E:\study\python\vscode\flask\fisher>pipenv shell
Launching subshell in virtual environment…
Microsoft Windows [版本 10.0.18362.476]
(c) 2019 Microsoft Corporation。保留所有权利。

(fisher-iWThc5xD) E:\study\python\vscode\flask\fisher>pip list
Package    Version
---------- -------
pip        19.3.1
setuptools 41.6.0
wheel      0.33.6

(fisher-iWThc5xD) E:\study\python\vscode\flask\fisher>
'''
# 6. 启动pipenv
# 7. 安装各种包，比如flask
#   ==>pipenv install flask, 安装好后在项目目录输入flask，没有报错也没有提示找不到命令代表安装完成
'''
(fisher-iWThc5xD) E:\study\python\vscode\flask\fisher>pipenv install flask
Installing flask…
Adding flask to Pipfile's [packages]…
Installation Succeeded
Pipfile.lock (662286) out of date, updating to (a65489)…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Success!
Updated Pipfile.lock (662286)!
Installing dependencies from Pipfile.lock (662286)…
  ================================ 6/6 - 00:00:46

(fisher-iWThc5xD) E:\study\python\vscode\flask\fisher>
'''
# 运行flask: pipenv shell 和python fisher.py
'''
E:\study\python\vscode\flask>cd fisher

E:\study\python\vscode\flask\fisher>dir
 驱动器 E 中的卷没有标签。
 卷的序列号是 0BD6-07CA

 E:\study\python\vscode\flask\fisher 的目录

2019/12/15  19:11    <DIR>          .
2019/12/15  19:11    <DIR>          ..
2019/12/15  21:26    <DIR>          .idea
2019/12/15  18:01                12 config.py
2019/12/15  19:11             2,776 fisher.py
2019/12/15  19:05               161 Pipfile
2019/12/11  22:50             4,566 Pipfile.lock
2019/12/15  18:01    <DIR>          __pycache__
               4 个文件          7,515 字节
               4 个目录 843,390,222,336 可用字节

E:\study\python\vscode\flask\fisher>pipenv shell
Launching subshell in virtual environment…
Microsoft Windows [版本 10.0.18363.535]
(c) 2019 Microsoft Corporation。保留所有权利。

(fisher-iWThc5xD) E:\study\python\vscode\flask\fisher>pipenv list
Usage: pipenv [OPTIONS] COMMAND [ARGS]...
Try "pipenv --help" for help.

Error: No such command "list".

Did you mean one of these?
    install

(fisher-iWThc5xD) E:\study\python\vscode\flask\fisher>pip list
Package      Version
------------ -------
Click        7.0
Flask        1.1.1
itsdangerous 1.1.0
Jinja2       2.10.3
MarkupSafe   1.1.1
pip          19.3.1
setuptools   41.6.0
Werkzeug     0.16.0
wheel        0.33.6

(fisher-iWThc5xD) E:\study\python\vscode\flask\fisher>python fisher.py
 * Serving Flask app "fisher" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 198-071-334
 * Running on http://0.0.0.0:81/ (Press CTRL+C to quit)
'''

# pip命令:在github上搜pipenv，建议看官方文档
# exit 退出虚拟环境
# pipenv shell 进入虚拟环境,若没有虚拟环境，则会自动安装虚拟环境
# pipenv install flask 安装flask
# pipenv uninstall flask 卸载flask
# pipenv graph  查看包的依赖

# 选择开发工具的条件
# 是否能够很好支持断点调试
# 自动重启web服务器
# Pycharm满足这个条件
# -javaagent:D:\install\pycharm\PyCharm 2019.3\bin\JetbrainsCrack-2.6.10-release-enc.jar 
# 注册码：
# BIG3CLIK6F-eyJsaWNlbnNlSWQiOiJCSUczQ0xJSzZGIiwibGljZW5zZWVOYW1lIjoibGFuIHl1IiwiYXNzaWduZWVOYW1lIjoiIiwiYXNzaWduZWVFbWFpbCI6IiIsImxpY2Vuc2VSZXN0cmljdGlvbiI6IkZvciBlZHVjYXRpb25hbCB1c2Ugb25seSIsImNoZWNrQ29uY3VycmVudFVzZSI6ZmFsc2UsInByb2R1Y3RzIjpbeyJjb2RlIjoiQUMiLCJwYWlkVXBUbyI6IjIwMTctMTEtMjMifSx7ImNvZGUiOiJETSIsInBhaWRVcFRvIjoiMjAxNy0xMS0yMyJ9LHsiY29kZSI6IklJIiwicGFpZFVwVG8iOiIyMDE3LTExLTIzIn0seyJjb2RlIjoiUlMwIiwicGFpZFVwVG8iOiIyMDE3LTExLTIzIn0seyJjb2RlIjoiV1MiLCJwYWlkVXBUbyI6IjIwMTctMTEtMjMifSx7ImNvZGUiOiJEUE4iLCJwYWlkVXBUbyI6IjIwMTctMTEtMjMifSx7ImNvZGUiOiJSQyIsInBhaWRVcFRvIjoiMjAxNy0xMS0yMyJ9LHsiY29kZSI6IlBTIiwicGFpZFVwVG8iOiIyMDE3LTExLTIzIn0seyJjb2RlIjoiREMiLCJwYWlkVXBUbyI6IjIwMTctMTEtMjMifSx7ImNvZGUiOiJEQiIsInBhaWRVcFRvIjoiMjAxNy0xMS0yMyJ9LHsiY29kZSI6IlJNIiwicGFpZFVwVG8iOiIyMDE3LTExLTIzIn0seyJjb2RlIjoiUEMiLCJwYWlkVXBUbyI6IjIwMTctMTEtMjMifSx7ImNvZGUiOiJDTCIsInBhaWRVcFRvIjoiMjAxNy0xMS0yMyJ9XSwiaGFzaCI6IjQ3NzU1MTcvMCIsImdyYWNlUGVyaW9kRGF5cyI6MCwiYXV0b1Byb2xvbmdhdGVkIjpmYWxzZSwiaXNBdXRvUHJvbG9uZ2F0ZWQiOmZhbHNlfQ==-iygsIMXTVeSyYkUxAqpHmymrgwN5InkOfeRhhPIPa88FO9FRuZosIBTY18tflChACznk3qferT7iMGKm7pumDTR4FbVVlK/3n1ER0eMKu2NcaXb7m10xT6kLW1Xb3LtuZEnuis5pYuEwT1zR7GskeNWdYZ0dAJpNDLFrqPyAPo5s1KLDHKpw+VfVd4uf7RMjOIzuJhAAYAG+amyivQt61I9aYiwpHQvUphvTwi0X0qL/oDJHAQbIv4Qwscyo4aYZJBKutYioZH9rgOP6Yw/sCltpoPWlJtDOcw/iEWYiCVG1pH9AWjCYXZ9AbbEBOWV71IQr5VWrsqFZ7cg7hLEJ3A==-MIIEPjCCAiagAwIBAgIBBTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTE1MTEwMjA4MjE0OFoXDTE4MTEwMTA4MjE0OFowETEPMA0GA1UEAwwGcHJvZDN5MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxcQkq+zdxlR2mmRYBPzGbUNdMN6OaXiXzxIWtMEkrJMO/5oUfQJbLLuMSMK0QHFmaI37WShyxZcfRCidwXjot4zmNBKnlyHodDij/78TmVqFl8nOeD5+07B8VEaIu7c3E1N+e1doC6wht4I4+IEmtsPAdoaj5WCQVQbrI8KeT8M9VcBIWX7fD0fhexfg3ZRt0xqwMcXGNp3DdJHiO0rCdU+Itv7EmtnSVq9jBG1usMSFvMowR25mju2JcPFp1+I4ZI+FqgR8gyG8oiNDyNEoAbsR3lOpI7grUYSvkB/xVy/VoklPCK2h0f0GJxFjnye8NT1PAywoyl7RmiAVRE/EKwIDAQABo4GZMIGWMAkGA1UdEwQCMAAwHQYDVR0OBBYEFGEpG9oZGcfLMGNBkY7SgHiMGgTcMEgGA1UdIwRBMD+AFKOetkhnQhI2Qb1t4Lm0oFKLl/GzoRykGjAYMRYwFAYDVQQDDA1KZXRQcm9
# ubuntu (> 16.4): sudo snap install [pycharm-professional|pycharm-community] --classic
ThisCrackLicenseId-{
"licenseId":"11011",
"licenseeName":"",
"assigneeName":"",
"assigneeEmail":"",
"licenseRestriction":"",
"checkConcurrentUse":false,
"products":[
{"code":"II","paidUpTo":"2099-12-31"},
{"code":"DM","paidUpTo":"2099-12-31"},
{"code":"AC","paidUpTo":"2099-12-31"},
{"code":"RS0","paidUpTo":"2099-12-31"},
{"code":"WS","paidUpTo":"2099-12-31"},
{"code":"DPN","paidUpTo":"2099-12-31"},
{"code":"RC","paidUpTo":"2099-12-31"},
{"code":"PS","paidUpTo":"2099-12-31"},
{"code":"DC","paidUpTo":"2099-12-31"},
{"code":"RM","paidUpTo":"2099-12-31"},
{"code":"CL","paidUpTo":"2099-12-31"},
{"code":"PC","paidUpTo":"2099-12-31"}
],
"hash":"2911276/0",
"gracePeriodDays":7,
"autoProlongated":false}
# Xampp (MySql) 安装MySql

# Navicat（数据库可视化管理工具）