import requests
import ccxt.async_support as ccxt
from settings import env
from global_variables import GLOBAL_VARIABLES


def get_current_price_eth():
    url = GLOBAL_VARIABLES['URL']
    symbol = GLOBAL_VARIABLES['SYMBOL']
    ticker = requests.get( url + '/api/v1/market/orderbook/level1?symbol={0}'.format( symbol ) ).json()
    price = ticker['data']['price']
    return price

async def obtain_exchange():
    
    kucoin = ccxt.kucoinfutures({
        'enableRateLimit': True,
        'apiKey': env('API_KEY_SANDBOX_FUTURE'),
        'secret': env('API_SECRET_SANDBOX_FUTURE'),
        'password': env('PASSPHRASE')
    })
    kucoin.set_sandbox_mode( True );

    return kucoin


async def create_order( exchange, side ):
    
    symbol = GLOBAL_VARIABLES['SYMBOL_PERPETUAL']
    order_type = 'market'
    amount = GLOBAL_VARIABLES['USDT_PER_OPERATION']
    params = {
        'leverage': GLOBAL_VARIABLES['LEVERAGE']
    }
    order = await exchange.create_order( symbol, order_type, side, amount, params=params )
    print(order)

    return [ order['id'], order['amount'] ]

async def close_operation( order_id ):
    
    exchange.cancelOrder(order_id)