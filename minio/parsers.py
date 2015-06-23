from xml.etree import ElementTree

__author__ = 'minio'


def parse_list_buckets(data):
    print 'xml', data
    root = ElementTree.fromstring(data)
    bucket_list = []
    for buckets in root.findall('{http://doc.s3.amazonaws.com/2006-03-01}Buckets'):
        for bucket in buckets:
            name = None
            creation_date = None
            print 'bucket', bucket
            for attribute in bucket:
                if attribute.tag == '{http://doc.s3.amazonaws.com/2006-03-01}Name':
                    name = attribute.text
                if attribute.tag == '{http://doc.s3.amazonaws.com/2006-03-01}CreationDate':
                    creation_date = attribute.text
            bucket_list.append(Bucket(name, creation_date))
    print 'bucket_list', bucket_list
    return bucket_list


class Bucket(object):
    def __init__(self, name, created):
        self.name = name
        self.creation_date = created