import asyncio
from util import get_current_price_eth, obtain_exchange, create_order, close_operation
from global_variables import GLOBAL_VARIABLES


async def main():
    exchange = await obtain_exchange()
    
    while True:
        initial_price = get_current_price_eth()
        sleep_time = GLOBAL_VARIABLES['SLEEP_TIME']
        print('sleep time', sleep_time)
        await asyncio.sleep( sleep_time )
        current_price = get_current_price_eth()
        print( initial_price, current_price )
        
        if current_price > initial_price:
            [orderId, amount] = await create_order( exchange, 'buy' )
            print( await exchange.fetch_free_balance() )
            print('Waiting for next operation')
            await asyncio.sleep( 60 - sleep_time )
            await close_operation( orderId )
            
        else:
            print('Waiting for next operation')
            await asyncio.sleep( 60 - sleep_time )
            
    
    await exchange.close()


if __name__ == '__main__':
    asyncio.run(main())
    
