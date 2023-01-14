# img2vec

## build proto

```shell
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. img2vec/api/v1/*.proto
```
