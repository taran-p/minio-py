# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage,
# (C) 2020 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from minio import Minio
from minio.commonconfig import ComposeSource, Tags
from minio.sse import SseS3
import os
import io
from random import randint

def client_from_env()->Minio:
    url = os.environ.get("MINIO_ADDRESS")
    user = os.environ.get("MINIO_ACCESS_KEY")
    pw = os.environ.get("MINIO_SECRET_KEY")
    sec_var = os.environ.get("MINIO_SECURE",'off')
    if sec_var == 'on':
        sec = True
    else:
        sec = False

    if url or user or pw:
        client = Minio(
            url,
            access_key=user,
            secret_key=pw,
            secure=sec
        )
        return client
    else:
        return None

def client_from_play()->Minio:
    client = Minio(
        'play.min.io',
        access_key='Q3AM3UQ867SPQQA43P2F',
        secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG'
    )
    return client

def main():
    client = client_from_env()
    if client == None:
        client = client_from_play()
    
    # Create random my-buckets
    bucket_name_1 = "my-source-bucket"+str(randint(10000,99999))
    client.make_bucket(bucket_name_1)
    bucket_name_2 = "my-bucket"+str(randint(10000,99999))
    client.make_bucket(bucket_name_2)
    print(bucket_name_2)

    # Create my-object
    client.put_object(bucket_name_1, "my-object-pt1", io.BytesIO(b"hello"), 5,) #Objects must be bigger than 5MB
    client.put_object(bucket_name_1, "my-object-pt2", io.BytesIO(b"hi"), 2,)
    client.put_object(bucket_name_1, "my-object-pt3", io.BytesIO(b"goodbye"), 7,)

    sources = [
        ComposeSource(bucket_name_1, "my-object-pt1"),
        ComposeSource(bucket_name_1, "my-object-pt2"),
        ComposeSource(bucket_name_1, "my-object-pt3"),
    ]

    # Create my-bucket/my-object by combining source object
    # list.
    result = client.compose_object(bucket_name_2, "my-object1", sources)
    print(result.object_name, result.version_id)

    # Create my-bucket/my-object with user metadata by combining
    # source object list.
    result = client.compose_object(
        bucket_name_2,
        "my-object2",
        sources,
        metadata={"test_meta_key": "test_meta_value"},
    )
    print(result.object_name, result.version_id)

    # Create my-bucket/my-object with user metadata and
    # server-side encryption by combining source object list.
    client.compose_object(bucket_name_2, "my-object3", sources, sse=SseS3())
    print(result.object_name, result.version_id)

    
if __name__ == '__main__':
    main()
