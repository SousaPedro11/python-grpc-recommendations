FROM python:3.10-alpine

RUN mkdir -p /service/marketplace

COPY marketplace/requirements.txt .

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

COPY protobufs/ service/protobufs
COPY marketplace/ /service/marketplace/

WORKDIR /service/marketplace

RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
     --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 5000

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
