# coding: UTF-8

import os
import argparse
from pprint import pprint
from datetime import date, datetime
import re

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


        # ===============================================================
        #                     Analysis options
        # ===============================================================
        self.parser.add_argument("-sd", "--start_date", type=str, default="2019/4/1", help="解析開始年月日")
        self.parser.add_argument("-ed", "--end_date", type=str, default="2021/3/31" ,help="解析終了年月日")
        self.parser.add_argument("-sh", "--start_hour", type=int, default=0, help="解析開始時刻")
        self.parser.add_argument("-eh", "--end_hour", type=int, default=23, help="解析終了時刻")
        self.parser.add_argument("-mi", "--meshid", nargs="*",type=int, help="解析するメッシュID")
        self.parser.add_argument("-p", "--pref", type=str, default="osaka", help="解析する都府の指定")

    def _print(self):
        print("\n==================Options=================")
        pprint(vars(self.opt), indent=4)
        print("==========================================\n")

    def parse(self):
        self._initial()
        self.opt = self.parser.parse_args()
        self.opt.start_year, self.opt.start_month, self.opt.start_day = re.split('[/\-_]', self.opt.start_date)
        self.opt.end_year, self.opt.end_month, self.opt.end_day = re.split('[/\-_]', self.opt.end_date)
        self.opt.pref = self.opt.pref.lower() # 小文字に変換
        self.opt.input_dir = os.path.join("dataset", self.opt.pref) # dataset直下の前提
        self.opt.output_dir = os.path.join("result", self.opt.output_dir) # result直下の前提
        self._print()
        return self.opt
