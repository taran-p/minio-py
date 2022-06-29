import bucket_exists
import compose_object
import copy_object
import delete_bucket_encryption
import delete_bucket_lifecycle
import delete_bucket_policy
import delete_bucket_tags
import delete_object_lock_config
import delete_object_tags
import disable_object_legal_hold
import enable_object_legal_hold
import fget_object
import fput_object
import get_bucket_encryption
import get_bucket_lifecycle
import get_bucket_tags
import get_bucket_versioning
import get_object_lock_config
import get_object_tags
import get_object
import is_object_legal_hold_enabled
import list_buckets
import list_objects
import make_bucket
import presigned_get_object
import presigned_post_policy
import presigned_put_object
import put_object
import remove_bucket
import remove_object
import remove_objects
import select_object_content
import set_bucket_encryption
import set_bucket_lifecycle
import set_bucket_policy
import set_bucket_tags
import set_bucket_versioning
import set_object_lock_config
import set_object_retention
import set_object_tags
import stat_object


def main():
    bucket_exists.main()
    compose_object.main()
    copy_object.main()
    delete_bucket_encryption.main()
    delete_bucket_lifecycle.main()
    delete_bucket_policy.main()
    delete_bucket_tags.main()
    delete_object_lock_config.main()
    delete_object_tags.main()
    disable_object_legal_hold.main()
    enable_object_legal_hold.main()
    fget_object.main() # sse-c commented out
    fput_object.main() # sse-c, sse-kms commented out
    get_bucket_encryption.main()
    get_bucket_lifecycle.main()
    get_bucket_tags.main()
    get_bucket_versioning.main()
    get_object_lock_config.main()
    get_object_tags.main()
    get_object.main() # sse-c commented out
    is_object_legal_hold_enabled.main()
    list_buckets.main()
    list_objects.main()
    make_bucket.main()
    presigned_get_object.main()
    presigned_post_policy.main()
    presigned_put_object.main()
    put_object.main() # sse-c, sse-kms commented out
    remove_bucket.main()
    remove_object.main()
    remove_objects.main()
    select_object_content.main()
    set_bucket_encryption.main()
    set_bucket_lifecycle.main()
    set_bucket_policy.main() # transition commented out
    set_bucket_tags.main()
    set_bucket_versioning.main()
    set_object_lock_config.main()
    set_object_retention.main()
    set_object_tags.main()
    stat_object.main() # sse-c commented out

if __name__ == '__main__':
    main()