from protos.user_pb2 import (
    UserCheckRequest
)

from protos.status_pb2 import (
    StatusResponse
)

import protos.user_pb2_grpc

class UserService(user_pb2_grpc.UserServicer):
    def Check(self, request, context):
        if request.username != "manoelhc":
            return StatusResponse(result=1)
        
        return StatusResponse(result=0)

