#!/usr/bin/env python3
import boto3

dynamodb_client = boto3.client('dynamodb')

#====================================================================================


def get_all_items(table_name, last_key=None, accumulator=[]):

    scan_results = {}
    if last_key:
        scan_results = dynamodb_client.scan(TableName=table_name,
                                            ExclusiveStartKey=last_key)
    else:
        scan_results = dynamodb_client.scan(TableName=table_name)
    segment = scan_results.get("Items", [])
    accumulator = accumulator + segment

    new_last_key = scan_results.get("LastEvaluatedKey")
    if new_last_key:
        return get_all_items(table_name=table_name,
                             last_key=new_last_key,
                             accumulator=accumulator)
    else:
        return accumulator


#====================================================================================


def count_all_items(table_name, last_key=None, counter=0):

    scan_results = {}
    if last_key:
        scan_results = dynamodb_client.scan(TableName=table_name,
                                            ExclusiveStartKey=last_key)
    else:
        scan_results = dynamodb_client.scan(TableName=table_name)
    segment_count = scan_results.get("Count", 0)
    last_key = scan_results.get("LastEvaluatedKey")
    new_count = counter + segment_count

    # print(counter, segment_count, last_key)
    if last_key:
        return count_all_items(table_name,
                               last_key=last_key,
                               counter=new_count)
    else:
        return new_count


#====================================================================================


def count_all_items_alt(table_name, last_key=None, counter=0):

    scan_results = {}
    if last_key:
        scan_results = dynamodb_client.scan(TableName=table_name,
                                            ExclusiveStartKey=last_key)
    else:
        scan_results = dynamodb_client.scan(TableName=table_name)
    segment_count = len(scan_results.get("Items"))
    last_key = scan_results.get("LastEvaluatedKey")
    # print(counter, segment_count, last_key)
    new_count = counter + segment_count

    if last_key:
        return count_all_items(table_name,
                               last_key=last_key,
                               counter=new_count)
    else:
        return new_count


#====================================================================================


def create_table(table_name,
                       hash_key="hash_key",
                       range_key="range_key",
                       read_capacity_units=5,
                       write_capacity_units=5):
    return dynamodb_client.create_table(TableName=table_name,
                                        KeySchema=[
                                            {
                                                'AttributeName': hash_key,
                                                'KeyType': 'HASH'
                                            },
                                            {
                                                'AttributeName': range_key,
                                                'KeyType': 'RANGE'
                                            },
                                        ],
                                        AttributeDefinitions=[
                                            {
                                                'AttributeName': hash_key,
                                                'AttributeType': 'S'
                                            },
                                            {
                                                'AttributeName': range_key,
                                                'AttributeType': 'S'
                                            },
                                        ],
                                        ProvisionedThroughput={
                                            'ReadCapacityUnits':
                                            read_capacity_units,
                                            'WriteCapacityUnits':
                                            write_capacity_units
                                        })


#====================================================================================

