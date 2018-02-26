#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cli.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Ernesto Ruy Sanchez <ernesto@tmake.mx>

from preggy import expect

from cli import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
