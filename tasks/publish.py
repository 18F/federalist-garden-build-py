'''
Publish tasks and helpers
'''
import os

from datetime import datetime

from invoke import task

from publishing.s3publisher import publish_to_s3
from log_utils import get_logger
from .common import SITE_BUILD_DIR_PATH, delta_to_mins_secs


LOGGER = get_logger('PUBLISH')


@task
def publish(ctx, base_url, site_prefix, bucket, cache_control,
            aws_region, dry_run=False):
    '''
    Publish the built site to S3.

    Expects AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to be
    in the environment.
    '''
    LOGGER.info('Publishing to S3')

    access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

    start_time = datetime.now()

    publish_to_s3(
        directory=SITE_BUILD_DIR_PATH,
        base_url=base_url,
        site_prefix=site_prefix,
        bucket=bucket,
        cache_control=cache_control,
        aws_region=aws_region,
        access_key_id=access_key_id,
        secret_access_key=secret_access_key,
        dry_run=dry_run
    )

    delta_string = delta_to_mins_secs(datetime.now() - start_time)
    LOGGER.info(f'Total time to publish: {delta_string}')
