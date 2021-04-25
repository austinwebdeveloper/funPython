admin_record = []
json_results = {'Result': {'ErrorCode': '0', 'ErrorDescription': {}, 'HydraErrorReturnCode': '0'},
 'Data': 
 {'NewDataSet': 
 {'Table': [{'DataID': '8', 'UserID': '100064', 'CreateDate': '2021-04-23T15:50:14.29-05:00', 'GTDataValue': 'D63F38F9-98BC-44B7-8B06-7352FB1FE380:100064', 'ShortName': 'SubscriberNumber'},
            {'DataID': '8', 'UserID': '100040', 'CreateDate': '2021-04-23T16:07:38.23-05:00', 'GTDataValue': 'D63F38F9-98BC-44B7-8B06-7352FB1FE380:100040', 'ShortName': 'SubscriberNumber'}]}}}
print(json_results)
result_table = json_results['Data']['NewDataSet']['Table']
if result_table:
    for record in result_table:
        if record['GTDataValue']:
            value = record['GTDataValue']
            print("value", value)
            admin_record.append(value)
        else:
            print(record)
print("admin_record", admin_record)