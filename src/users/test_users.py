import unittest
import grpc

from protos.user_pb2_grpc import UserStub
from protos.user_pb2 import UserCheckRequest
from protos.status_pb2 import ResultStatus

channel = grpc.insecure_channel("localhost:50051")
client = UserStub(channel)

class TestUserCheck(unittest.TestCase):
    def test_available_user(self):
        status = client.Check(UserCheckRequest(username="man"))
        self.assertEqual(ResultStatus.NOT_EXIST, status.result)
    def test_existing_user(self):
        status = client.Check(UserCheckRequest(username="manoelhc"))
        self.assertEqual(ResultStatus.OK, status.result)

if __name__ == '__main__':
    unittest.main()