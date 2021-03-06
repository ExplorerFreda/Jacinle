# -*- coding: utf-8 -*-
# File   : custom_optimizer.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 27/02/2018
#
# This file is part of Jacinle.

__all__ = ['CustomizedOptimizer']


class CustomizedOptimizer(object):
    @property
    def state(self):
        raise NotImplementedError()

    @property
    def param_groups(self):
        raise NotImplementedError()

    def state_dict(self):
        raise NotImplementedError()

    def load_state_dict(self, state_dict):
        raise NotImplementedError()

    def zero_grad(self):
        raise NotImplementedError()

    def step(self, closure=None):
        raise NotImplementedError()
