caffe on Ubuntu 16.04 (without anaconda)
for python3.5

1. 
sudo apt-get install libprotobuf-dev libleveldb-dev libopencv-dev libsnappy-dev
sudo apt-get install libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install python3-dev
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev

sudo apt-get -y install libopenblas-dev
sudo apt-get install libfaac-dev

2. 
git clone https://github.com/BVLC/caffe

cd caffe



```
apt-get install python3-numpy

find /usr -iname "*hdf5.h*"   # find out where is hdf5.h

find /usr -name arrayobject.h  # find arrayobject.h for python 

/usr/lib/python3/dist-packages/numpy/core/include/numpy/arrayobject.h
```

cp Makefile.config.example Makefile.config
vim Makefile.config
```
a. Uncomment (No space in the beginning): 
    CPU_ONLY := 1

b. Uncomment:
    USE_PKG_CONFIG := 1
    
c. Modify 
# Whatever else you find you need goes here.
before INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include 
after INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/  
:wq

d. Modify PYTHON_LIBRARIES for python3  
/usr/lib/python3/dist-packages/numpy/core/include/numpy

e. Uncomment:
python2 directory
#before boost_python3 
#after boost_python-py35
```




3. vim Makefile
```
before LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5
after LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_serial_hl hdf5_serial
```

4. 
cd ~/caffe/python
sudo pip3 install -r requirements.txt

cd /usr/lib/x86_64-linux-gnu
sudo ln -s libboost_python-py35.so libboost_python3.so
```
location:
/usr/lib/x86_64-linux-gnu/libboost_python-py35.so
```


5. 
sudo make -j

6. 
sudo make pycaffe


7.
sudo make test
sudo make runtest


8. 
vim .bashrc
```
# Caffe Root
#export CAFFE_ROOT=/home/<username>/caffe/
#export PYTHONPATH=/home/<username>/caffe/distribute/python:$PYTHONPATH
export PYTHONPATH=/home/<username>/caffe/python:$PYTHONPATH
```

9. 
pip3 install python-dateutil --upgrade

Reference:
http://blog.csdn.net/m0_37477175/article/details/78151283
https://gist.github.com/arundasan91/b432cb011d1c45b65222d0fac5f9232c
http://caffe.berkeleyvision.org/install_apt.html
https://github.com/erlerobot/gym-gazebo/issues/90
