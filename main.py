# coding: UTF-8

import os
import pandas as pd
from utils.option import Option
from datetime import date, datetime
import matplotlib.pyplot as plt
from icecream import ic
import glob
import code

def valid_option(opt):
    """
    オプションの検証
    """
    errors = []
    if date(int(opt.start_year), int(opt.start_month), int(opt.start_day)) > date(int(opt.end_year), int(opt.end_month), int(opt.end_day)):
        errors.append("終了年月日は開始年月日より後にしてください")
    # if opt.meshid == None or len(opt.meshid) <= 0:
    #     errors.append("メッシュIDを1つ以上指定してください")
    if opt.pref == None:
        errors.append("都府を指定してください")
    if 0 < len(errors):
        print("==================Errors==================")
        for err in errors:
            print(err)
        print("==========================================\n")
        exit()

def define_file(opt):
    file = []
    start_date = date(int(opt.start_year), int(opt.start_month), int(opt.start_day))
    end_date = date(int(opt.end_year), int(opt.end_month), int(opt.end_day))
    if date(2019, 4, 1) <= start_date:
        file.append("*2019*1*")
    if date(2019, 10, 1) <= start_date:
        file.append("*2019*2*")
    if date(2020, 4, 1) <= start_date:
        file.append("*2020*1*")
    if date(2020, 10, 1) <= start_date:
        file.append("*2020*2*")

    if end_date <= date(2020, 3, 31):
        file.append("*2019*2*")
    if end_date <= date(2020, 9, 30):
        file.append("*2020*1*")
    if end_date <= date(2021, 3, 30):
        file.append("*2020*2*")

def main(opt):
    target_data = pd.DataFrame()
    tmp = []
    # define_file(opt)
    for data in sorted(glob.glob(os.path.join(opt.input_dir, "*.csv"))):
        print(data)
        tmp.append(pd.read_csv(data).query(f"{opt.start_hour} <= hour & hour <= {opt.end_hour}")
                                    )
    target_data = pd.concat(tmp)
    start_date = date(int(opt.start_year), int(opt.start_month), int(opt.start_day))
    end_date = date(int(opt.end_year), int(opt.end_month), int(opt.end_day))
    # target_data['year'] = target_data['year'].astype(str)
    # target_data['month'] = target_data['month'].astype(str)
    # target_data['month'] = target_data['month'].str.zfill(2)
    # target_data['day'] = target_data['day'].astype(str)
    # target_data['day'] = target_data['day'].str.zfill(2)
    # target_data['date'] = target_data['year']+target_data['month']+target_data['day']
    # target_data['date'] = pd.to_datetime(target_data['date'], format="%Y%m%d")

    # tmp = target_data.groupby('date').mean()
    # if opt.start_hour == opt.end_hour:
    #     plt.plot(target_data['date'],target_data['population'])
    #     # plt.xlabel("日付")
    #     # plt.ylabel("人流量")
    # elif start_date == end_date:
    #     plt.plot(target_data['hour'], target_data['population'])
    #     # plt.xlabel("時間")
    #     # plt.ylabel("人流量の平均")
    # else:
    #     plt.plot(tmp.index, tmp['population'])
    #     # plt.xlabel("日付")
    #     # plt.ylabel("人流量の平均")
    # plt.show()
    code.InteractiveConsole(locals=locals()).interact()

if __name__ == "__main__":
    option = Option().parse()
    valid_option(option)
    # init(option)
    main(option)
    # code.InteractiveConsole(locals=locals()).interact()
