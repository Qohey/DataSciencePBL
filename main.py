# coding: UTF-8

import sys
import os
import numpy as np
import pandas as pd
from utils.option import Option
from icecream import ic

def init(opt):
    """
    出力用のディレクトリやファイル作成，その他諸々の初期化
    """
    output_file = os.path.join(opt.output_dir, opt.output_name) + ".csv" # */*.csvの形
    if not os.path.exists(opt.output_dir):
        os.makedirs(opt.output_dir)
    if not os.path.isfile(output_file):
        with open(output_file, "w", encoding="UTF-8") as f:
            f.write("")
    else: #ファイルが重複したときは上書き確認
        print(output_file + "はすでに存在しています。\n上書きしますか？Y/n")
        if input() == "Y":
            with open(output_file, "w", encoding="UTF-8") as f:
                f.write("")
        else:
            exit()

def valid_path(opt):
    """
    オプションで指定されたpathの検証
    """
    errors = []
    input_file = os.path.join(opt.input_dir, opt.input_name) # */*.csvの形
    if opt.input_name == "":
        errors.append("input_nameを指定してください")
    elif not os.path.isfile(input_file):
        errors.append(input_file + "が見つかりません")
    if opt.output_name == "":
        errors.append("output_nameを指定してください")
    if 0 < len(errors):
        print("==================Errors==================")
        for err in errors:
            print(err)
        print("==========================================\n")
        exit()


def main(opt):
    target_data = pd.DataFrame()
    target_data = pd.read_csv(os.path.join(opt.input_dir, opt.input_name))
    print(target_data.describe())


if __name__ == "__main__":
    option = Option().parse()
    valid_path(option)
    init(option)
    main(option)
