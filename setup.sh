set -ex

export CHECKER_DIR=checker_bin
export LOG_DIR=logs

mkdir -p $LOG_DIR
mkdir -p problems
mkdir -p $CHECKER_DIR

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir --upgrade pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

git clone https://github.com/jpswing/Lo-runner.git
cd Lo-runner
python setup.py install
cd ..

rm -rf Lo-runner

git clone https://github.com/MikeMirzayanov/testlib.git

for checker in testlib/checkers/*.cpp
do
  filename=$(basename -- "$checker")
  extension="${filename##*.}"
  filename="${filename%.*}"
  g++ -I testlib/ $checker -o $CHECKER_DIR/$filename -O2 --std=c++14
done

cp testlib/testlib.h $CHECKER_DIR
rm -rf testlib
