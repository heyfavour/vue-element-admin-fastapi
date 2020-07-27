# -*- coding:utf-8 -*-

import importlib


class Report():
    def __init__(self, code,):
        self.code = code
        self.module_url = "app.api.api_v1.report.report." + code
        self.module = self.import_module(self.module_url).Query()

    def import_module(self, module_url):
        return importlib.import_module(module_url)




