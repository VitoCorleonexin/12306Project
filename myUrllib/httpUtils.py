import requests
from collections import OrderedDict
from agency.agency_tools import Proxy
import TickerConfig
from config import logger
from time import sleep
import json
import random
import socket

def _set_header_default():
    header_dict = OrderedDict()
    # header_dict["Accept"] = "application/json, text/plain, */*"
    header_dict["Accept-Encoding"] = "gzip, deflate"
    header_dict["User-Agent"] = _set_user_agent()
    header_dict["Content-Type"] = "application/x-www-form-urlencoded;" 
    "charset=UTF-8"
    header_dict["Origin"] = "https://kyfw.12306.cn"
    header_dict["Connection"] = "keep-alive"
    return header_dict


def _set_user_agent():
    # try:
    #     user_agent = UserAgent(verify_ssl=False).random
    #     return user_agent
    # except:
    #     print("请求头设置失败，使用默认请求头")
    #     return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) Apple
    #WebKit/537.36 (KHTML, like Gecko) Chrome/75.0.' + str(
    #         random.randint(5000, 7000)) + '.0 Safari/537.36'
    return "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    " (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"


class HTTPClient(object):

    def __init__(self, is_proxy, cdn_list=None):
        """
        cdn_list 切换不包括查询的cdn，防止查询cdn污染登陆和下单cdn
        """
        self.init_s()
        self._cdn = None
        self.cdn_list = cdn_list
        self._proxies = None
        if is_proxy is 1:
            self.proxy = Proxy()
            self._proxies = self.proxy.setProxy()
             # print(u"设置当前代理ip为 {}, 请注意代理ip是否可用！！！！！请注意
             #代理ip是否可用！！！！！请注意代理ip是否可用！！！！！".
             #format(self._proxies))

    def init_s(self):
        self._s = requests.Session()
        self._s.headers.update(_set_header_default())
        return self
    
    def set_cookies(self, kwargs):
        """
        Setting cookies
        :param kwargs:
        :return :
        
        """
        
        for kwarg in kwargs:
            for k, v in kwarg.items():
                self._s.cookies.set(k, v)

    def get_cookies(self):
        
        """
       get cookies
       :return:
        """
        
        return self._s.cookies.values()

    def del_cookies(self):
        
        """
        delete all cookies
        :return:
        """
        
        self._s.cookies.clear()

    def del_cookies_by_key(self, key):
        
        """
        delete the given key'cookies
        :return:
        """
        
        self._s.cookies.set(key, None)

    def set_headers(self, headers):
        self._s.headers.update(headers)
        return self

    def reset_headers(self):
        self._s.headers.clear()
        self._s.headers.update(_set_header_default())

    def get_headers_host(self):
        return self._s.headers['Host']

    def set_headers_host(self, host):
        self._s.headers.update({'Host': host})
        return self

    def set_headers_user_agent(self):
        self._s.headers.update({"User-Agent": _set_user_agent()})

    def get_headers_user_agent(self):
        return self._s.headers["User-Agent"]

    def get_headers_referer(self):
        return self._s.headers["Referer"]

    def set_headers_referer(self, referer):
        self._s.headers.update({"Referer": referer})
        return self
    
    @property
    def cdn(self):
        return self._cdn
    
    @cdn.setter
    def cdn(self, cdn):
        self._cdn = cdn
    
    
    def send(self, urls, data=None, **kwargs):
        """
        send request to url. if response 200, return response, else 
        return None.
        """
        allow_redirects = False
        is_logger = urls.get('is_logger', False)
        req_url = urls.get('req_url', '')
        re_try = urls.get('re_try', '')
        s_time = urls.get('s_time', 0)
        is_cdn = urls.get('is_cdn', False)
        is_test_cdn = urls.get('is_test_cdn', False)
        error_data = {'code': 99999, 'message': 'reached limits'}
        if data:
            method = 'post'
            self.set_headers({"Content-Length": f"{len(data)}"})
        else:
            method = 'get'
            self.reset_headers()
        if TickerConfig.random_agent is 1:
            self.set_headers_user_agent()
        self.set_headers_referer(urls["Referer"])
        if is_logger:
            logger.log(f'url: {req_url}\n param: {data}\n reqeust type:' 
            '{method}')
        self.set_headers_host(urls['Host'])
        if is_test_cdn:
            url_host = self._cdn
        elif is_cdn:
            if self._cdn:
                url_host = self._cdn
            else:
                url_host = urls['Host']
        else:
            url_host = ulrs['Host']
        
        for i in range(re_try):
            try:
                
                sleep(s_time)
                try:
                    requests.packages.urllib3.disable_warnings()
                except:
                    pass
                response = self._s.request(method=method,
                                           timeout=5,
                                           proxies=self._proxies,
                                           url=http + "://" + url_host
                                            + req_url,
                                           data=data,
                                           allow_redirects=
                                           allow_redirects,
                                           verify=False,
                                           **kwargs)
                if response.status_code == 200 or response.status_code
                 == 302:
                    if urls.get('not_decode', False):
                        return response.content
                    if response.content:
                        if is_logger:
                            logger.log(u'出参 :{0}'.format(response.
                            content.decode()))
                        if urls['is_json']:
                            return json.loads(response.content.decode()
                                              if isinstance(
                                              response.content, bytes)
                                              else response.content)
                        else:
                            retrun response.content.decode('utf-8', 
                            'ignore') if
                            isinstance(response.content, bytes) else
                             response.content
                    else:
                        print(f"{urls['req_url']} return empty, "
                        "interface status code: {response.status_code}")
                        logger.log(f"url: urls['req_url'] "
                        "returns empty")
                        if self.cdn_list:
                            # 如果下单或者登陆出现cdn 302的情况，立马切换cdn
                            url_host = self.cdn_list.pop
                            (random.randint(0, 4))
                        continue
               else:
                   sleep(urls["re_time"])
        
            except(requests.exceptions.Timeout, requests.exceptions.
            ReadTimeout,
            requests.exceptions.ConnectionError):
                pass
            except socket.error:
                pass
        return error_data                
                                            
            
            
        
