export CHECKER_DIR=testlib/bin
export LOG_DIR=logs

mkdir -p $LOG_DIR
mkdir -p problems

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

git clone https://github.com/jpswing/Lo-runner.git
cd Lo-runner
python setup.py install
cd ..

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

apt install pypy3
apt install default-jdk
apt install sshfs
