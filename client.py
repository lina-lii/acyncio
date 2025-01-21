import asyncio

HOST = '127.0.0.1'  # Локальный адрес сервера
PORT = 8888         # Порт сервера

async def tcp_echo_client():
    """Асинхронный клиент."""
    reader, writer = await asyncio.open_connection(HOST, PORT)
    print(f"Подключено к серверу {HOST}:{PORT}")

    while True:
        message = input("Введите сообщение (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            print("Закрытие соединения...")
            writer.close()
            await writer.wait_closed()
            break

        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(100)
        print(f"Ответ от сервера: {data.decode()}")

if __name__ == '__main__':
    asyncio.run(tcp_echo_client())
