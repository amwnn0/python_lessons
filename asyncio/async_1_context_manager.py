import asyncio

async def get_conn(host, port):
    class Conn:
        async def put_data(self):
            print('Data transferring...')
            await asyncio.sleep(1)
            print('Data transferred')

        async def get_data(self):
            print('Getting data...')
            await asyncio.sleep(1)
            print('Got data')

        async def close(self):
            print('Closing connection...')
            await asyncio.sleep(1)
            print('Connection closed')

    print('Connecting to %s:%d' % (host, port))
    await asyncio.sleep(1)
    print('Connected')
    return Conn()


class Connection:
    # этот конструктор будет выполнен в заголовке with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # этот метод будет неявно выполнен при входе в with
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    # этот метод будет неявно выполнен при выходе из with
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()

async def main():
    async with Connection('localhost', 9001) as conn:
        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_data())

        await send_task
        await receive_task


asyncio.run(main())