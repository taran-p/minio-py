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
from random import randint
from datetime import datetime, timedelta

from progress import Progress
from minio import Minio
from minio.commonconfig import GOVERNANCE, Tags
from minio.retention import Retention
from minio.sse import SseCustomerKey, SseKMS, SseS3

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
    
    #Create random my-bucket
    bucket_name = "my-bucket"+str(randint(10000,99999))
    client.make_bucket(bucket_name,"us-east-1", object_lock=True)
    print(bucket_name)

    # Upload data.
    result = client.fput_object(
        bucket_name, "my-object1", "examples/my-filename",
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ),
    )

    # Upload data with content-type.
    result = client.fput_object(
        bucket_name, "my-object2", "examples/my-filename",
        content_type="application/csv",
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ),
    )

    # Upload data with metadata.
    result = client.fput_object(
        bucket_name, "my-object3", "examples/my-filename",
        metadata={"My-Project": "one"},
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ),
    )

    # Upload data with customer key type of server-side encryption.
    result = client.fput_object(
        bucket_name, "my-object4", "examples/my-filename",
        sse=SseCustomerKey(b"32byteslongsecretkeymustprovided"),
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ),
    )

    # Upload data with KMS type of server-side encryption.
    result = client.fput_object(
        bucket_name, "my-object5", "examples/my-filename",
        sse=SseKMS("KMS-KEY-ID", {"Key1": "Value1", "Key2": "Value2"}),
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ),
    )

    # Upload data with S3 type of server-side encryption.
    result = client.fput_object(
        bucket_name, "my-object6", "examples/my-filename",
        sse=SseS3(),
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ),
    )

    # Upload data with tags, retention and legal-hold.
    date = datetime.utcnow().replace(
        hour=0, minute=0, second=0, microsecond=0,
    ) + timedelta(days=30)
    tags = Tags(for_object=True)
    tags["User"] = "jsmith"
    result = client.fput_object(
        bucket_name, "my-object7", "examples/my-filename",
        tags=tags,
        retention=Retention(GOVERNANCE, date),
        legal_hold=True,
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ),
    )

    # Upload data with progress bar.
    result = client.fput_object(
        bucket_name, "my-object8", "examples/my-filename",
        progress=Progress(),
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ),
    )
    
if __name__ == '__main__':
    main()
