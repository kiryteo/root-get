# root-get

ROOT's package manager prototype

### Prerequisites
```
python
cmake (Version 3.8 and above)
```

### Initial setup
Required - root build files directory, if not present already, do an out of source build for root

(if root is present in '/home/username/root' then inside '/home/username' do the following)
```
$mkdir rootbuild
$cd rootbuild
$cmake -DCMAKE_CXX_STANDARD=14 -Dbuiltin_clang=on ../root
$make
```
Fork and Clone the repository 
```
$git clone https://github.com/oshadura/root-get
```
Create a directory where you would like to install new packages using root-get
(inside '/home/username' directory or any other path)
```
$mkdir installdir
```
Inside the root-get directory, set environment variables
```
$cd root-get
$export ROOTSOURCES="/path/to/root/source/directory"
$export ROOT_PKG_PATH="/path/where/to/install/new/packages"
(/home/username/installdir if you have followed above method)
$export ROOTSYS="/path/to/rootbuild/directory"
```

### Installing

To install a new module with root-get :
```
./bin/root_get.py -i 'modulename'
```

e.g. Installing XMLIO with root-get :
```
./bin/root_get.py -i XMLIO
```

## Contributing

Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

## License

## Acknowledgments

