export CHECKER_DIR=testlib/bin
export LOG_DIR=logs

mkdir -p $LOG_DIR
mkdir -p problems

groupadd fuse
usermod -a -G fuse root

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir --upgrade pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

git clone https://github.com/jpswing/Lo-runner.git
cd Lo-runner
python setup.py install
cd ..

rm -rf Lo-runner

git clone https://github.com/MikeMirzayanov/testlib.git
cd testlib

mkdir bin
for checker in checkers/*.cpp
do
  filename=$(basename -- "$checker")
  extension="${filename##*.}"
  filename="${filename%.*}"
  g++ -I ./ $checker -o bin/$filename -O2 --std=c++14
done
cd ..

apt-get update
apt-get install -y pypy3 default-jdk sshfs
rm -rf /var/lib/apt/lists/*
