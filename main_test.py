# -*- coding: utf-8 -*-

"""
    作者:     Kevin Shi
    版本:     1.0
    日期:     2017/02/19
    项目名称：科技工作者心理健康数据分析 (Mental Health in Tech Survey)
"""
import csv

# 数据集路径
data_path = './survey.csv'


def run_main():
    mental_health_set = {'Yes'}  # 心理健康问题要找到的值

    result_dict = {}
    # result_dict_final = {}

    with open(data_path, 'r', newline='') as csvfile:
        # 加载数据
        rows = csv.reader(csvfile)
        for i, row in enumerate(rows):
            if i == 0:
                # 跳过第一行表头数据
                continue

            if i % 50 == 0:
                print('正在处理第{}行数据...'.format(i))
            # 性别数据
            age_val = row[1]
            country_val = row[3]
            mental_health_val = row[18]

            # sum([1, 2, 3])

            # 去掉可能存在的空格
            age_val = age_val.replace(' ', '')
            mental_health_val = mental_health_val.replace(' ', '')

            # 判断“国家”是否已经存在
            if country_val not in result_dict:
                # 如果不存在，初始化数据
                # result_dict[country_val] = []
                result_dict[country_val] = [0, 0, 0]  # 第一个参数存储符合条件的年龄总和， 第二个参数存储有多少条记录

            # 有心理问题, 要过滤不合常理的数据，如Zimbabwe 年龄999999 392行
            if mental_health_val in mental_health_set and (len(age_val) <= 3):
                # 列出所有符合条件的年龄列表
                # result_dict[country_val].append(age_val)

                # 第一个参数存储符合条件的年龄总和， 第二个参数存储有多少条记录
                result_dict[country_val][0] += int(age_val)
                result_dict[country_val][1] += 1

            else:
                # 噪声数据，不做处理
                pass

    # 将结果写入文件
    with open('mental_country1.csv', 'w', newline='', encoding='utf-16') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        # 写入表头
        # csvwriter.writerow(['国家', '存在心理问题的年龄列表'])
        csvwriter.writerow(['国家', '存在心理问题的平均年龄'])

        # 写入统计结果
        for k, v in list(result_dict.items()):

            # if len(result_dict[k]) == 0:
            #     csvwriter.writerow([k, 0])
            # else:
            #     csvwriter.writerow([k, v])
            # csvwriter.writerow([k, v])

            if int(v[0]) == 0:
                v[2] = 0
            else:
                v[2] = round(int(v[0]) / int(v[1]), 2)
            csvwriter.writerow([k, v[2]])


if __name__ == '__main__':
    run_main()
