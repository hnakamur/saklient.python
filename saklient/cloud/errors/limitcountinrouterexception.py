# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException
import saklient

# module saklient.cloud.errors.limitcountinrouterexception

class LimitCountInRouterException(HttpConflictException):
    ## 要求を受け付けできません。ルータあたりのリソース数上限により、リソースの割り当てに失敗しました。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(LimitCountInRouterException, self).__init__(status, code, "要求を受け付けできません。ルータあたりのリソース数上限により、リソースの割り当てに失敗しました。" if message is None or message == "" else message)
    
