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
from datetime import datetime, timedelta

from minio import Minio
from minio.datatypes import PostPolicy

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
    url = os.environ.get("MINIO_ADDRESS")+'/'
    if client == None:
        client = client_from_play()
        url = 'https://play.min.io/'

    # Create random my-bucket
    bucket_name = "my-bucket"+str(randint(10000,99999))
    client.make_bucket(bucket_name)
    print(bucket_name)
    
    policy = PostPolicy(
        bucket_name, datetime.utcnow() + timedelta(days=10),
    )
    policy.add_starts_with_condition("key", "my/object/prefix/")
    policy.add_content_length_range_condition(1*1024*1024, 10*1024*1024)

    form_data = client.presigned_post_policy(policy)

    curl_cmd = (
        "curl -X POST "+
        url +
        bucket_name + " "
        "{0} -F file=@<FILE>"
    ).format(
        " ".join(["-F {0}={1}".format(k, v) for k, v in form_data.items()]),
    )
    print(curl_cmd)
    
if __name__ == '__main__':
    main()


