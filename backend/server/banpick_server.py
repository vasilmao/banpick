from concurrent import futures
from time import sleep
import grpc
import logging

import server.grpc_out.banpick_pb2_grpc as banpick_grpc

from server.pickban_service import BanPickService


class BanPickServer:
    """
    Класс, реализующий сервер, который хостит наш сервис
    """
    def __init__(self, port=5000, host='[::]', max_workers=10):
        self._port = port
        self._host = host
        # Сервер создаётся многопоточным c максимум max_workers потоками,
        # но это не страшно, всей многопоточностью управляет gRPC
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        # Говорим, что наш banpicktingService реализует описанный в Proto сервис чата на этом сервере
        banpick_grpc.add_BanPickServicer_to_server(BanPickService(), self._server)

    def serve(self):
        print('Starting server...')
        self._server.add_insecure_port(f'{self._host}:{self._port}')
        self._server.start()
        print(f'Listening on {self._host}:{self._port}')
        print('Press CTRL+C to stop...')
        try:
            # wait_for_termination ничего не делает (можно заменить на очень большой sleep), просто ждёт
            # пока сервер не остановится, чтобы основной процесс программы не завершался.
            self._server.wait_for_termination()
        except KeyboardInterrupt:
            self._server.stop(None)
            print('Server is stopped')
