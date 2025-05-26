import server.grpc_out.banpick_pb2 as banpick_proto

from server.db.db_all import get_tournament_collection
from google.protobuf.json_format import Parse, ParseDict, MessageToDict, MessageToJson

import json


def CreateTournament():
    tour_collection = get_tournament_collection()
    # tour_id = (tour_collection.estimated_document_count()) + 1
    max_element = tour_collection.find_one(sort=[("tournamentId", -1)])
    tour_id = 1
    if (max_element is not None):
        tour_id = max_element["tournamentId"] + 1
    prsn = banpick_proto.Person(personId=1, personName="keklol")
    new_tournament = banpick_proto.Tournament(
        tournamentId = tour_id,
        name = "New Tournament",
        people=[prsn]
    )
    tour_collection = get_tournament_collection()
    tour_collection.insert_one(MessageToDict(new_tournament))
    return tour_id

def GetTournament(tournament_id: int):
    tour_collection = get_tournament_collection()
    result = tour_collection.find_one({"tournamentId":tournament_id}, {'_id': False})
    x = Parse(json.dumps(result), banpick_proto.Tournament(), ignore_unknown_fields=False)
    return x

def UpdateTournament(new_t: banpick_proto.Tournament):
    tour_collection = get_tournament_collection()
    tour_collection.replace_one({"tournamentId": new_t.tournamentId}, MessageToDict(new_t))
    return new_t.tournamentId
