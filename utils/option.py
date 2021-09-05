# coding: UTF-8
import argparse

class Option():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.opt = None

    def _initial(self):
        self.parser.add_argument("--input_dir", type=str, default="dataset/", help="解析するデータのフォルダ")
        self.parser.add_argument("--input_name", type=str, default="", help="解析するデータのファイル名")
        self.parser.add_argument("--output_dir", type=str, default="result", help="解析結果の出力フォルダ")
        self.parser.add_argument("--output_name", type=str, default="result", help="解析結果の出力ファイル名(拡張子なし)")

    def parse(self):
        self._initial()
        self.opt = self.parser.parse_args()
        return self.opt
