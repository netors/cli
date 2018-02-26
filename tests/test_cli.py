#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cli.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Ernesto Ruy Sanchez <ernesto@tmake.mx>

from preggy import expect

from cli.cli import main
from tests.base import TestCase


class MainTestCase(TestCase):
    def test_prints_cli(self):
        main()
