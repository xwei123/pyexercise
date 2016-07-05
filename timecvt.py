#!/usr/bin/env python
# _*_ coding: utf-8_*_

# 这句话是引入模块
# import datetime

# 从模块中引入类
from datetime import datetime, timedelta, date



# --------- output -----------------


def main():
    # import time
    # 从公元元年开始计数的天数
    day = 39495.6289236111
    print type(day)
    n = 1
    print type(n)
    # -------- input -------------------
    # excel 里的公元元年
    # cmd + / 就是生成注释行
    # 这一句是为了构造一个公元元年的日期对象
    epoch = datetime(1899, 12, 30)
    print epoch
    print type(epoch)
    # 构造一个能相加的时间差
    # delta = timedelta(39495.6289236111, 0, 0, 0, 0, 8, 0)
    # 命名参数写法
    delta = timedelta(days=39495.6289236111, hours=8)
    print type(delta)
    # delta = datetime.timedelta(days=day, hours=8)
    print delta
    # 日期相加就是结果，国际时间
    result = epoch + delta
    # 拿到日期对象
    resultdate = result.date()
    print resultdate
    print type(resultdate)
    # 这是日期字符串
    datestr = result.date().isoformat()
    print datestr
    print type

    # -------- process -----------------
    print result

    today = datetime.now()
    print today

    # print date.today()


if __name__ == '__main__':
    main()
