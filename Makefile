# Proto helpers
proto-users:
	python -m grpc_tools.protoc -I protobufs --python_out=src/users/protos --grpc_python_out=src/users/protos protobufs/user.proto protobufs/status.proto

# Build section
build-base:
	docker build -t jaguar_base -f Containerfile .

build-user:
	docker build -t jaguar_users -f src/users/Containerfile src/users

# Run section
run-users: build-user
	docker container stop jaguar_users || true
	docker container rm jaguar_users || true
	docker run -p 50051:50051 --name jaguar_users jaguar_users
	
