from aliyunsdkcore.client import AcsClient

class AcsClientString():

    __client = None
    __AccessKeyId = 'xxx'
    __AccessKeySecret = 'xxx'

    @classmethod
    def get_instance(self):

        if self.__client is None:
            self.__client = AcsClient(self.__AccessKeyId, self.__AccessKeySecret, 'cn-hangzhou')

        return self.__client