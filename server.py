import asyncio

HOST = '127.0.0.1'  # Локальный адрес
PORT = 8888         # Порт для прослушивания

async def handle_echo(reader, writer):
    """Обработка подключения клиента."""
    addr = writer.get_extra_info('peername')
    print(f"Клиент подключен: {addr}")

    while True:
        data = await reader.read(100)
        if not data:
            break  # Клиент отключился

        message = data.decode()
        print(f"Получено: {message} от {addr}")

        writer.write(data)  # Отправляем данные обратно клиенту
        await writer.drain()

    print(f"Клиент отключен: {addr}")
    writer.close()
    await writer.wait_closed()

async def main():
    """Запуск сервера."""
    server = await asyncio.start_server(handle_echo, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f"Сервер запущен на {addr}")

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
