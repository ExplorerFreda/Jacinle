# -*- coding: utf-8 -*-
# File   : plot.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 19/01/2018
# 
# This file is part of Jacinle.

import io as _io
import numpy as np

from jacinle.image.backend import cv2, opencv_only

__all__ = ['plot2img']


@opencv_only
def plot2img(plt):
    """Convert a pyplot instance to image"""

    buf = _io.BytesIO()
    plt.axis('off')
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    rawbuf = np.frombuffer(buf.getvalue(), dtype='uint8')
    im = cv2.imdecode(rawbuf, cv2.IMREAD_COLOR)
    buf.close()
    return im
