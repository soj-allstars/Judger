mkdir logs

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

git clone https://github.com/dojiong/Lo-runner.git
cd Lo-runner
python setup.py install

cd ..
git clone https://github.com/MikeMirzayanov/testlib.git
cd testlib

for checker in `ls checkers/*.cpp`
do
  g++ $checker -o bin/"${FILE%%.*}" -O2 --std=c++11
done
