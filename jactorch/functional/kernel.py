# -*- coding: utf-8 -*-
# File   : kernel.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 04/02/2018
# 
# This file is part of Jacinle.

"""Useful utilities for kernel-based attention mechanism."""

import torch

from jactorch.functional.linalg import normalize

__all__ = ['inverse_distance', 'cosine_distance', 'dot']


def inverse_distance(f_lookup, f, p=2, eps=1e-8):
    """
    Inverse distance kernel.

    Args:
        f_lookup FloatTensor(NxK): features of the lookup keys
        f FloatTensor(MxK): features of the value keys

    Returns FloatTensor(NxM): the attention mask for each lookup keys.
    """

    n, m, k = f_lookup.size(0), f.size(0), f.size(1)
    f_lookup = f_lookup.view(n, 1, k).expand(n, m, k)
    f = f.view(1, m, k).expand(n, m, k)

    dist = (f_lookup - f).norm(p, dim=2)
    return 1. / dist.clamp(min=eps)


def cosine_distance(f_lookup, f):
    f_lookup = normalize(f_lookup, 2, dim=1)
    f = normalize(f, 2, dim=1)

    return torch.mm(f_lookup, f.t())


def dot(f_lookup, f):
    return torch.mm(f_lookup, f.t())
