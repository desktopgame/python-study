# python-study
python勉強用
````
C:\Work\python-study>python --version
Python 3.7.6

C:\Work\python-study>pip --version
pip 19.2.3 from c:\python37\lib\site-packages\pip (python 3.7)
````

## 新しいプロジェクトの追加
````
cd python-study
python -m venv project-name
; プロジェクト作る
code project-name
; .vscode/launch.json
; project-name.code-workspace
; を作成して、pythonPathを Scripts/python に設定する
````

## このプロジェクトをクローンする
このプロジェクトにはサブディレクトリそれぞれにpythonプロジェクトが格納されており、  
そのそれぞれが`python -m venv`によって作成されています。  
これをクローン側でセットアップする方法について。  
例として`httpTest`をセットアップする。

````
hub clone desktopgame/python-study
cd httpTest
python -m venv .
; Windowsなら
; Scripts¥activate
; Macなら
; . bin/activate
pip install -r requirements.txt

deactivate
````