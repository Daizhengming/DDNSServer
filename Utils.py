from AcsClient import AcsClientString
from urllib.request import urlopen
import json
from aliyunsdkalidns.request.v20150109 import DescribeDomainRecordsRequest, UpdateDomainRecordRequest

class Utils:

    def get_netIP():
        return json.load(urlopen('https://api.ipify.org/?format=json'))['ip']

    def get_records(domain):
        request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
        request.set_DomainName(domain)
        request.set_accept_format('json')
        result = AcsClientString.get_instance().do_action(request)
        result = json.JSONDecoder().decode(str(result, encoding='utf8'))
        return result

    def update_dns(RR, Type, Value, RecordId, TTL):
        request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
        request.set_RR(RR)
        request.set_Type(Type)
        request.set_Value(Value)
        request.set_RecordId(RecordId)
        request.set_TTL(TTL)
        request.set_accept_format('json')
        result = AcsClientString.get_instance().do_action(request)
        return result