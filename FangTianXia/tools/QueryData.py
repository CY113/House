# coding=utf-8

from tools import DBHelper


class QueryData(object):
    def __init__(self):
        self.db_helper = DBHelper.DBHelper()

    def get_new_house_url(self):
        query_sql = "SELECT detail_url FROM new_house"
        return self.db_helper.query_task(query_sql)

    def get_esf_house_url(self):
        query_sql = "SELECT detail_url FROM esf_house"
        return self.db_helper.query_task(query_sql)

    def get_rent_house_url(self):
        query_sql = "SELECT detail_url FROM rent_house"
        return self.db_helper.query_task(query_sql)


if __name__ == '__main__':
    url_list = QueryData().get_esf_house_url()
    print(url_list)
