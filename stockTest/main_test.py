import pandas as pd
import pandas_datareader
import datetime
import matplotlib.pylab as plt
from matplotlib.pylab import style
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


style.use('ggplot')     # 设置图片显示的主题样式

# 解决matplotlib显示中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def main_run():
    """
        主函数
    """
    # 1. 准备数据
    # 指定股票分析开始日期
    start_date = datetime.datetime(2007, 1, 1)
    # 指定股票分析截止日期
    end_date = datetime.datetime(2017, 3, 1)
    # 股票代码
    stock_code = '600519.SS'    # 沪市贵州茅台

    stock_df = pandas_datareader.data.DataReader(
                        stock_code, 'yahoo', start_date, end_date
                )
    # 预览数据
    print(stock_df.head())
    print('--------------------------------------------------1-------------------------------------------------------')

    # 2. 可视化数据
    plt.plot(stock_df['Close'])
    plt.title('股票每日收盘价')
    plt.show()

    # 按周重采样
    stock_s = stock_df['Close'].resample('W-MON').mean()
    stock_train = stock_s['2014':'2016']
    plt.plot(stock_train)
    plt.title('股票周收盘价均值')
    plt.show()

    acf = plot_acf(stock_train, lags=20)
    plt.title('股票指数的 ACF')
    acf.show()

    pacf = plot_pacf(stock_train, lags=20)
    plt.title('股票指数的 PACF')
    pacf.show()

    print('--------------------------------------------------2-------------------------------------------------------')

    stock_diff = stock_train.diff()
    diff = stock_diff.dropna()
    print(diff.head())
    print(diff.dtypes)
    print('--------------------------------------------------3-------------------------------------------------------')
    plt.figure()
    plt.plot(diff)
    plt.title('一阶差分')
    plt.show()

    acf_diff = plot_acf(diff, lags=20)
    plt.title('一阶差分的 ACF')
    acf_diff.show()

    pacf_diff = plot_pacf(diff, lags=20)
    plt.title('一阶差分的 PACF')
    pacf_diff.show()

    print('--------------------------------------------------4-------------------------------------------------------')

    model = ARIMA(stock_train, order=(1, 1, 1), freq='W-MON')
    arima_result = model.fit()
    print(arima_result.summary())

    print('--------------------------------------------------5-------------------------------------------------------')

    pred_vals = arima_result.predict('20170102', '20170301', dynamic=True, typ='levels')
    print(pred_vals)

    print('--------------------------------------------------6-------------------------------------------------------')

    stock_forcast = pd.concat([stock_s, pred_vals], axis=1, keys=['original', 'predicted'])

    plt.figure()
    plt.plot(stock_forcast)
    plt.title('真实值vs预测值')
    # plt.savefig('./stock_pred.png', format='png')
    plt.show()

if __name__ == '__main__':
    main_run()










