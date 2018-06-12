# coding:utf-8
import numpy as np
import pandas as pd
import os, sys
import codecs


def merge_data(data_src, data_dst_file):
    """
    合并数据
    :param data_src:  数据源文件夹
    :param data_dst_file:  保存数据文件
    :return:
    """
    dfs_api = None;
    for file_name in os.listdir(data_src):
        scv_file_dir = os.path.join(data_src, file_name);
        for scv_name in os.listdir(scv_file_dir):
            try:
                scv_file = os.path.join(scv_file_dir, scv_name)
                df = pd.read_csv(scv_file)
                df_api = df[df.type == 'AQI'];
                if dfs_api is None:
                    dfs_api = df_api
                else:
                    dfs_api = pd.concat([dfs_api, df_api])
                print len(dfs_api)
            except Exception as e:
                print scv_file
                print e
    dfs_api.to_csv(data_dst_file, index=False, header=True)


def load_data():
    train_df=None;
    train_df = pd.DataFrame(columns=['year', 'month', 'day', 'hour', 'area', 'label'])
    fr = codecs.open('C:\Users\Administrator\PycharmProjects\knn-exp/train_data/beijing_api.csv')
    fr.next();
    areas = [''] * 36
    df_list = []
    pre_label=[0.0]*36;
    for line in fr:
        line = line.strip();
        # date,hour,type,东四,天坛,官园,万寿西宫,奥体中心,农展馆,万柳,北部新区,植物园,丰台花园,云岗,古城,房山,大兴,亦庄,通州,顺义,昌平,门头沟,平谷,怀柔,密云,延庆,定陵,八达岭,密云水库,东高村,永乐店,榆垡,琉璃河,前门,永定门内,西直门北,南三环,东四环
        date, hour, type, areas[1], areas[2], areas[3], areas[4], areas[5], areas[6], areas[7], areas[8], \
        areas[9], areas[10], areas[11], areas[12], areas[13], areas[14], areas[15], areas[16], areas[17], areas[18], \
        areas[19], \
        areas[20], areas[21], areas[22], areas[23], areas[24], areas[25], areas[26], areas[27], areas[28], areas[29], \
        areas[30], areas[31], \
        areas[32], areas[33], areas[34], areas[35] = line.split(',')
        month = int(date[4:6])
        day = int(date[6:8])
        hour = int(hour)
        for ind, area in enumerate(areas[1:], start=1):
            if ind>1:
                df = pd.DataFrame(columns=[ 'month', 'day', 'hour', 'area','pre_label', 'label'],
                                  data=[[month, day, hour, ind,pre_label[ind], float(-1.0 if area in ['', None] else area)]])
                df_list.append(df)
            pre_label[ind] = float(-1.0 if area in ['', None] else area)
    train_df = pd.concat(df_list)
    train_df.to_csv("C:\Users\Administrator\PycharmProjects\knn-exp/train_data/beijing_train.csv", index=False,
                        header=True)


if __name__ == '__main__':
    # merge_data("C:\Users\Administrator\PycharmProjects\knn-exp\data",
    #            "C:\Users\Administrator\PycharmProjects\knn-exp/train_data/beijing_api.csv")
    load_data()
