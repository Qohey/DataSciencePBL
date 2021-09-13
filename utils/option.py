# coding: UTF-8

import os
import argparse
from pprint import pprint

class Option():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.opt = None

    def _initial(self):
        # ===============================================================
        #                     I/O options
        # ===============================================================
        self.parser.add_argument("-id", "--input_dir", type=str, default="", help="解析するデータのフォルダ(dataset直下のフォルダ)")
        self.parser.add_argument("-in", "--input_name", type=str, default="", help="解析するデータのファイル名")
        self.parser.add_argument("-od", "--output_dir", type=str, default="", help="result直下に出力するフォルダ")
        self.parser.add_argument("-on", "--output_name", type=str, default="result", help="解析結果の出力ファイル名(拡張子なし)")

        # ===============================================================
        #                     Analysis options
        # ===============================================================
        self.parser.add_argument("-p", "--pref", type=str, default="osaka", help="解析する都府の指定")

    def _print(self):
        print("\n==================Options=================")
        pprint(vars(self.opt), indent=4)
        print("==========================================\n")

    def parse(self):
        self._initial()
        self.opt = self.parser.parse_args()
        self._print()
        self.opt.input_dir = os.path.join("dataset", self.opt.input_dir) # dataset直下の前提
        self.opt.output_dir = os.path.join("result", self.opt.output_dir) # result直下の前提
        if self.opt.input_name != "": # 指定があれば*.csvの形に変更
            self.opt.input_name = self.opt.input_name + ".csv"
        return self.opt
