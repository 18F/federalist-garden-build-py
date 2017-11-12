'''
Common variables, tasks, and functions
'''

import shutil

from os import path
from datetime import timedelta  # noqa pylint: disable=W0611

from invoke import task
from dotenv import load_dotenv as _load_dotenv

from log_utils import get_logger

REPO_BASE_URL = 'github.com'
WORKING_DIR = path.join(path.sep, 'tmp')

CLONE_DIR = 'site_repo'
CLONE_DIR_PATH = path.join(WORKING_DIR, CLONE_DIR)

SITE_BUILD_DIR = '_site'

BASE_DIR = path.dirname(path.dirname(__file__))
DOTENV_PATH = path.join(BASE_DIR, '.env')

SITE_BUILD_DIR_PATH = path.join(CLONE_DIR_PATH, SITE_BUILD_DIR)

LOGGER = get_logger('COMMON')


def load_dotenv():
    '''Loads environment from a .env file'''
    if path.exists(DOTENV_PATH):
        LOGGER.info('Loading environment from .env file')
        _load_dotenv(DOTENV_PATH)


def delta_to_mins_secs(delta):
    '''
    Converts a timedelta to a string of minutes and seconds.

    >>> td = timedelta(seconds=55)
    >>> delta_to_mins_secs(td)
    '55s'

    >>> td = timedelta(seconds=124)
    >>> delta_to_mins_secs(td)
    '2m 4s'
    '''
    secs = int(delta.total_seconds())
    if secs > 60:
        mins = int(secs // 60)
        secs = int(secs % 60)
        return f'{mins}m {secs}s'
    # else
    return f'{secs}s'


@task
def clean(ctx, which=None):
    '''Deletes the specified directory'''
    which = which or CLONE_DIR_PATH
    LOGGER.info(f'Cleaning {which}')
    shutil.rmtree(which, ignore_errors=True)
