# -*- coding:utf8 -*-
# File   : client.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 3/19/17
# 
# This file is part of Jacinle.

import time
import sys
import uuid

from jacinle.comm.cs import ClientPipe


def main():
    client = ClientPipe('client' + uuid.uuid4().hex[:8], conn_info=sys.argv[1:3])
    print('Identity: {}.'.format(client.identity))
    with client.activate():
        in_ = dict(a=1, b=2)
        out = client.query('calc', in_)
        print('Success: input={}, output={}'.format(in_, out))
        time.sleep(1)


if __name__ == '__main__':
    main()
