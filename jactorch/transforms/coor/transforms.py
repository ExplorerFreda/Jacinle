# -*- coding: utf-8 -*-
# File   : transforms.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 03/03/2018
# 
# This file is part of Jacinle.

import random

import torch
import torchvision.transforms as transforms

from . import functional as F

__all__ = ["Compose", "Lambda", "ToTensor", "NormalizeCoor", "Normalize", "Resize", "CenterCrop", "Pad",
           "RandomCrop", "RandomHorizontalFlip", "RandomVerticalFlip", "RandomResizedCrop",
           "LinearTransformation", "ColorJitter", "RandomRotation", "Grayscale", "RandomGrayscale"]


class Compose(transforms.Compose):
    def __call__(self, img, coor):
        for t in self.transforms:
            img, coor = t(img, coor)
        return img, coor


class Lambda(transforms.Lambda):
    def __call__(self, img, coor):
        return self.lambd(img, coor)


class ToTensor(transforms.ToTensor):
    def __call__(self, img, coor):
        img, coor = F.refresh_valid(img, coor)
        return super().__call__(img), torch.from_numpy(coor)


class NormalizeCoor(object):
    def __call__(self, img, coor):
        return F.normalize_coor(img, coor)


class Normalize(transforms.Normalize):
    def __call__(self, img, coor):
        return super().__call__(img), coor


class Resize(transforms.Resize):
    # Assuming coordinates are 0/1-normalized.
    def __call__(self, img, coor):
        return super().__call__(img), coor


class CenterCrop(transforms.CenterCrop):
    def __call__(self, img, coor):
        return F.center_crop(img, coor, self.size)


class Pad(transforms.Pad):
    def __call__(self, img, coor):
        return F.pad(img, coor, self.padding, self.fill)


class RandomCrop(transforms.RandomCrop):
    def __call__(self, img, coor):
        if self.padding > 0:
            img = F.pad(img, coor, self.padding)
        i, j, h, w = self.get_params(img, self.size)
        return F.crop(img, coor, i, j, h, w)


class RandomHorizontalFlip(transforms.RandomHorizontalFlip):
    def __call__(self, img, coor):
        if random.random() < 0.5:
            return F.hflip(img, coor)
        return img, coor


class RandomVerticalFlip(transforms.RandomVerticalFlip):
    def __call__(self, img, coor):
        if random.random() < 0.5:
            return F.vflip(img, coor)
        return img, coor


class RandomResizedCrop(transforms.RandomResizedCrop):
    def __call__(self, img, coor):
        i, j, h, w = self.get_params(img, self.scale, self.ratio)
        return F.resized_crop(img, coor, i, j, h, w, self.size, self.interpolation)


class Grayscale(transforms.Grayscale):
    def __call__(self, img, coor):
        return super().__call__(img), coor


class RandomGrayscale(transforms.RandomGrayscale):
    def __call__(self, img, coor):
        return super().__call__(img), coor


class LinearTransformation(transforms.LinearTransformation):
    def __call__(self, tensor, coor):
        return super().__call__(tensor), coor


class ColorJitter(transforms.ColorJitter):
    def __call__(self, img, coor):
        return super().__call__(img), coor


class RandomRotation(transforms.RandomRotation):
    def __call__(self, img, coor):
        assert self.degrees[0] == self.degrees[1] == 0
        angle = self.get_params(self.degrees)
        return F.rotate(img, coor, angle, self.resample, self.expand, self.center)
