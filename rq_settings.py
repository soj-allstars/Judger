import os
# all available settings can be found in https://github.com/rq/rq/blob/master/rq/cli/helpers.py

# REDIS_URL = 'redis://soj-redis:6379/0'

# You can also specify the Redis DB to use
REDIS_HOST = os.environ.get('REDIS_HOST', 'soj-redis')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_DB = 0
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')

# Queues to listen on
# QUEUES = ['default', 'check'] # specified in Dockerfile

# If you're using Sentry to collect your runtime exceptions, you can use this
# to configure RQ for it in a single step
# The 'sync+' prefix is required for raven: https://github.com/nvie/rq/issues/350#issuecomment-43592410
# SENTRY_DSN = 'sync+http://public:secret@example.com/1'

# If you want custom worker name
# NAME = 'worker-1024'
