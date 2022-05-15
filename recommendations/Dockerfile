FROM python:alpine3.10

RUN mkdir /service

COPY protobufs/ service/protobufs
COPY recommendations/ /service/recommendations/

WORKDIR /service/recommendations

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
    --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 50051

ENTRYPOINT [ "python", "recommendations.py" ]
