
# Ports for your workers
STRATUM_HOST = "0.0.0.0"
STRATUM_PORT = 5555

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = '42JzYcuSB8tUThjTEc7a89bbYWtZXa7EwhPWcfUV1WTYEPYDMNACSjNJZPaRimBh1GcxPKxeG9Na5GAc7xygPUNXEFSpLhS'
# Only if you mine direct to the exchange
PAYMENT_ID = ''

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = True
MONITORING_EMAIL = 'mail@example.com'

# Main pool
POOL_HOST = 'pool.minexmr.com'
POOL_PORT = 7777

# Failover pool
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'pool.minexmr.com'
POOL_PORT_FAILOVER = 7777

# ERROR, INFO, DEBUG
LOGLEVEL = 'INFO'
DEBUG = False
LOGFILE = "logfile.log"
