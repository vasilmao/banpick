from queue import Queue
from time import sleep

import grpc

import server.grpc_out.banpick_pb2 as banpick_proto
import server.grpc_out.banpick_pb2_grpc as banpick_grpc

import server.db.db_tournament as dblib
import logging


class BanPickService(banpick_grpc.BanPickServicer):
    """
    Класс, который реализует описанный в Proto файле сервис
    """

    MESSAGE_STREAM_INTERVAL: 0.1

    def __init__(self):
        # История всех сообщений
        self._history = []
        self._is_working = True

    def CreateTournament(self, request, context: grpc.ServicerContext):
        logging.error("PEPETS")
        new_id = dblib.CreateTournament()
        # request to db, returns id
        print(new_id)
        return banpick_proto.TourId(tour_id=new_id)
    
    def GetTournament(self, request: banpick_proto.TourId, context: grpc.ServicerContext):
        # request to db
        res = dblib.GetTournament(request.tour_id)
        return res
    
    def EditTournament(self, edited: banpick_proto.Tournament, context: grpc.ServicerContext):
        # change in db
        old_id = dblib.UpdateTournament(edited)
        return banpick_proto.TourId(tour_id = old_id)
