# DataSciencePBL

## 使い方
- python main.py --input_name *csvファイル* --output_name *出力時のファイル名*
---
<br>

## オプション
- `-id, --input_dir` : datasetフォルダ直下にフォルダを指定.
- `-in, --input_name` : 解析したいcsvファイル名(拡張子なし).指定がない場合はエラー.
- `-od, --output_dir` : resultフォルダ直下に作成されるフォルダを指定.
- `-on, --output_name` : 出力するファイル名(拡張子なし).デフォルトは`result_月日時分秒`.
- `-p, --pref` : 解析したい都府を指定(例. osaka，tokyo).デフォルトは`osaka`.
---
<br>

## git clone
```
cd 作業フォルダ
git clone git@github.com:Qohey/DataSciencePBL.git
cd ./DataSciencePBL
```
---
<br>

## git cloneがわからない
- ブラウザで[ここ](https://github.com/Qohey/DataSciencePBL)にアクセス
- 緑色の`Codeボタン`をクリック
- 1番下の`Download ZIP`をクリック
- 解凍して完了
---
<br>

## Pythonの環境構築

### Mac
DataSciencePBLフォルダに移動
```
brew install pyenv
pyenv install 3.8.8
pyenv local 3.8.8
python -m venv .env
```
### Windows
DataSciencePBLフォルダに移動

---
<br>

## 仮想環境の入り方
### Mac
```
# bashの場合
source .env/bin/activate
# fishの場合
source .env/bin/activate.fish
```
詳しくは[こちら](https://qiita.com/m3y/items/45c7be319e401b24fca8)

### Windows
```
source .env/bin/activate
```
---
<br>

## ライブラリ関係のインストール
pipで以下のライブラリをインストール
- numpy
- matplotlib
- pandas
- icecream
---
<br>

## 仮想環境からの抜け方
```
deactivate
```
