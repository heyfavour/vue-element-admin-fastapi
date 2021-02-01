# -*- coding:utf-8 -*-
import importlib
from app.api.api_v1.report.gen_excel import gen_template


class Report():
    def __init__(self, code, query_params):
        self.code = code
        self.module_url = "app.api.api_v1.report.report." + code
        self.module = self.import_module(self.module_url).Query(query_params=query_params)

    def import_module(self, module_url):
        return importlib.import_module(module_url)


class BaseQuery():
    def __init__(self, query_params):
        self.query_params = query_params
        self.header = []
        self.file_name = ""
        self.report_config()

    def report_config(self):
        pass

    def get_template(self):
        return gen_template(self.header, self.file_name)

    def instance_data(self):
        return []

    def get_instance(self, db):
        self.db = db
        data = self.instance_data()
        return gen_template(self.header, self.file_name, data)
