https://github.com/jpswing/Lo-runner.git

在Judger_Test/Judger_Test文件目录下打开cmd

docker image build -t judger:1.0 .

之后

docker run -it judger:1.0

### SSHFS
[tutorial](https://www.linode.com/docs/networking/ssh/using-sshfs-on-linux/)

dev:
```
sshfs root@172.17.0.1:/root/soj/shared_data/problems problems
```