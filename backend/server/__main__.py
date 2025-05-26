from server.banpick_server import BanPickServer
from server.db.db_all import connect_and_init_db
import os
import time

# Строка [::] означает, что мы разрешаем подключение с любого хоста (любого IP и Hostname).
# Можно явно написать localhost или 127.0.0.1, тогда будет работать только на одном компьютере.
# os.system("./compile_proto.sh")
# time.sleep(100000)
server = BanPickServer(5000, '[::]')
connect_and_init_db()
server.serve()
