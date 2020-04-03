from Utils import Utils


if __name__ == "__main__":

     print('{:10} | {:^11} | {:^11} |'.format('DNS IP LOG', 'OLD-IP', 'NOW-IP'))
     fmt = '{:10} | {:^11} | {:^11} |'

     record_info = Utils.get_records("minglearning.info")
     local_ip = Utils.get_netIP()

     if record_info['DomainRecords']['Record']:

          dns_ip = record_info['DomainRecords']['Record'][0]['Value']
          RR = record_info['DomainRecords']['Record'][0]['RR']
          Type = record_info['DomainRecords']['Record'][0]['Type']
          RecordId = record_info['DomainRecords']['Record'][0]['RecordId']
          TTL = record_info['DomainRecords']['Record'][0]['TTL']
          if local_ip != dns_ip:
               Value = local_ip
               result = Utils.update_dns(RR, Type, Value, RecordId, TTL)
               print(fmt.format('Change', dns_ip, local_ip))
          else:
               print(fmt.format('Same', dns_ip, local_ip))
     else:
          print("ERROR: DNS Not initialization!!!")