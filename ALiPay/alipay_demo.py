#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import traceback

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient

from alipay.aop.api.domain.AlipayTradeCreateModel import AlipayTradeCreateModel
from alipay.aop.api.request.AlipayTradeCreateRequest import AlipayTradeCreateRequest
from alipay.aop.api.response.AlipayTradeCreateResponse import AlipayTradeCreateResponse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')

if __name__ == '__main__':
    # 实例化客户端
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
    alipay_client_config.app_id = '2016102800773902'
    alipay_client_config.app_private_key = open("zz.zzs7.top.txt", "r").read()
    alipay_client_config.alipay_public_key = open("alipayCertPublicKey_RSA2.crt", "r").read().replace("\n", "")
    client = DefaultAlipayClient(alipay_client_config, logger)

    # 构造请求参数对象
    model = AlipayTradeCreateModel()
    model.out_trade_no = "20150320010101001"
    model.total_amount = "88.88"
    model.subject = "Iphone6 16G"
    model.buyer_id = "2088102177846880"
    request = AlipayTradeCreateRequest(biz_model=model)

    # 执行API调用
    try:
        response_content = client.execute(request)
    except Exception as e:
        response_content = None
        print(traceback.format_exc())

    if not response_content:
        print("failed execute")
    else:
        # 解析响应结果
        response = AlipayTradeCreateResponse()
        response.parse_response_content(response_content)
        # 响应成功的业务处理
        if response.is_success():
            # 如果业务成功，可以通过response属性获取需要的值
            print("get response trade_no:" + response.trade_no)
        # 响应失败的业务处理
        else:
            # 如果业务失败，可以从错误码中可以得知错误情况，具体错误码信息可以查看接口文档
            print(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg)

