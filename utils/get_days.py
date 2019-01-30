#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date, datetime


def get_days(dt):
    now = date.today()
    delta = datetime.strptime(dt[:10], '%Y-%m-%d').date() - now

    return delta.days


if __name__ == '__main__':
    print(get_days('2019-02-11T00:00:00.000+08:00'))
