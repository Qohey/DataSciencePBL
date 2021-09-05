# coding: UTF-8
import sys
import os
import numpy as np
import pandas as pd
from utils.option import Option
from icecream import ic


def valid_path(opt):
    errs = []
    if opt.input_name == "":
        errs.append("input_nameを指定してください")
    if not os.path.exists(os.path.join(opt.input_dir, opt.input_name)):
        errs.append(os.path.join(opt.input_dir, opt.input_name) + "が見つかりません")
    elif not os.path.join(opt.input_dir, opt.input_name).endswith(".csv"):
        errs.append(os.path.join(opt.input_dir, opt.input_name) + "はcsvファイルではありません")
    if len(errs):
        print("＊＊＊＊エラー＊＊＊＊")
        for err in errs:
            print(err)
        exit()


def main(opt):
    target_data = pd.DataFrame()
    target_data = pd.read_csv(os.path.join(opt.input_dir, opt.input_name))
    print(target_data)


if __name__ == "__main__":
    option = Option().parse()
    valid_path(option)
    main(option)
