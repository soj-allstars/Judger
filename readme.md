# soj-judger
### Run redis
```
docker run -itd -p 127.0.0.1:6379:6379 --name soj-redis --network soj-net redis
```
### Build image and run container
Build image

```
docker image build -t judger:1.0 .
```
Run container
```
docker run -d --name soj-judger --network soj-net judger:1.0
```
