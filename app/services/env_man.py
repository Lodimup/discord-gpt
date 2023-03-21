"""
Makes sure environment variables are set and valid.
"""
import os

L_ENVS = [
    'OPENAI_API_KEY',
    'GUILD_ID',
    'DEFAULT_SYSTEM_MESSAGE',
    'PREPEND_USERNAME',
]


def check_envs() -> None:
    """
    Check if environment variables are set.
    """
    env_not_set = [env for env in L_ENVS if env not in os.environ]
    if env_not_set:
        raise ValueError(f'Environment variables not set: {env_not_set}')


def make_envs() -> dict:
    """
    Generate a dictionary of environment variables.
    """
    check_envs()
    ret = {}

    for env in L_ENVS:
        ret[env] = os.getenv(env)

    return ret


ENVS = make_envs()
