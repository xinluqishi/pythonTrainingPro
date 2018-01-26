import math


def judge_abc(password_str):
    for i in password_str:
        if i.isnumeric():
            print("true")
    print("false")


def main():

    """
       python入门视频练习
    """

    total_week = 52
    money_per_week = float(input('请输入每周存入的金额：'))
    increase_money = float(input('请输入每周存入的金额：'))
    saving = 0

    money_list = []

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        print('第{}周，存入{}元，账户余额{}元'.format(i + 1, money_per_week, saving))

        money_per_week += increase_money

if __name__ == '__main__':
    # main()
    judge_abc('abc1233')
