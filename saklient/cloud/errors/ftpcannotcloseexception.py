# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException
import saklient

# module saklient.cloud.errors.ftpcannotcloseexception

class FtpCannotCloseException(HttpConflictException):
    ## 要求された操作を行えません。FTP共有によりアップロードされたファイルを操作できません。ファイル名等をご確認ください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(FtpCannotCloseException, self).__init__(status, code, "要求された操作を行えません。FTP共有によりアップロードされたファイルを操作できません。ファイル名等をご確認ください。" if message is None or message == "" else message)
    
