# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage,
# (C) 2015 MinIO, Inc.
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

import os
import io
from random import randint

from minio import Minio
from minio.sse import SseCustomerKey

def client_from_env()->Minio:
    url = os.environ.get("MINIO_ADDRESS")
    user = os.environ.get("MINIO_ACCESS_KEY")
    pw = os.environ.get("MINIO_SECRET_KEY")
    sec_var = os.environ.get("MINIO_SECURE",'on')
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
    
    #Create random my-bucket
    bucket_name = "my-bucket"+str(randint(10000,99999))
    client.make_bucket(bucket_name)
    print(bucket_name)

    #Create my-object
    r = client.put_object(bucket_name, "my-object", io.BytesIO(b"hello"), 5,)
    client.put_object(bucket_name, "my-object", io.BytesIO(b"Lorem ipsum dolor sit amet orci aliquam."), 40,)
    ver = r.version_id

    # Get data of an object.
    try:
        response = client.get_object(bucket_name, "my-object")
        # Read data from response.
    finally:
        response.close()
        response.release_conn()

    # Get data of an object of version-ID.
    try:
        response = client.get_object(
            bucket_name, "my-object",
            version_id = ver,
        )
        # Read data from response.
    finally:
        response.close()
        response.release_conn()

    # Get data of an object from offset and length.
    try:
        response = client.get_object(
            bucket_name, "my-object", offset=10, length=15,
        )
        # Read data from response.
    finally:
        response.close()
        response.release_conn()

    # # Get data of an SSE-C encrypted object.
    # try:
    #     response = client.get_object(
    #         bucket_name, "my-object",
    #         ssec=SseCustomerKey(b"32byteslongsecretkeymustprovided"),
    #     )
    #     # Read data from response.
    # finally:
    #     response.close()
    #     response.release_conn()
    
if __name__ == '__main__':
    main()
