class HTTPClient(object):

    def __init__(self, is_proxy, cdn_list=None):
        """
        cdn_list 切换不包括查询的cdn，防止查询cdn污染登陆和下单cdn
        """
        self.initS()
        self.cdn_list = cdn_list
