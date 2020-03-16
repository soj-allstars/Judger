# soj-judger
### Run redis
```
docker run -itd -p 127.0.0.1:6379:6379 --name soj-redis --network soj-net redis
```
### How to build image and run container
在Judger_Test/Judger_Test文件目录下打开cmd

```
docker image build -t judger:1.0 .
```
之后
```
docker run --privileged=true -d --name soj-judger --network soj-net judger:1.0
```
### Set up SSHFS
[tutorial](https://www.linode.com/docs/networking/ssh/using-sshfs-on-linux/)

Enter the container:
```
docker exec -it soj-judger /bin/bash
```

Then:
```
sshfs root@172.17.0.1:/path/to/soj/backend/shared_data/problems problems
```
Change 172.17.0.1 to the hostname of soj backend.
