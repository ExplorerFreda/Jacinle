# -*- coding: utf-8 -*-
# File   : travis.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 04/02/2018
# 
# This file is part of Jacinle.

import os.path as osp
import glob
import subprocess

from jacinle.logging import get_logger

logger = get_logger(__file__)


def auto_travis(filename, required_files=None, use_glob=True):
    if required_files is None:
        required_files = ['**.so']

    dirname = osp.dirname(filename)

    compiled = True
    for fname in required_files:
        fname = osp.join(dirname, fname)
        if not osp.exists(fname):
            if not use_glob or len(glob.glob(fname, recursive=True)) == 0:
                compiled = False

    if compiled:
        logger.critical('Loading c extension from: "{}".'.format(dirname))
    else:
        logger.critical('Compiling c extension at: "{}".'.format(dirname))
        subprocess.check_call(['./travis.sh'], cwd=dirname)
