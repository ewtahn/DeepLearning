
[TOC]
# DeepLearning学习步骤
## 环境搭建
利用`Anaconda`管理`python`的科学包。不过网速有限，暂时安装了`miniconda`，安装哪个版本无所谓，注意配置环境变量。
`conda`一个特点是可以管理多个独立的环境，这样python2，3可以放在不同的环境里。
```
$ conda create -n py36 python=3.6 ##创立环境
$ source activate py36            ##激活环境
$ conda list                      ##查看该环境下的包
$ conda install numpy             ##安装numpy包
$ source deactivate py36          ##离开环境
$ conda env list                  ##查看一共有几个环境
$ conda env remove -n py36        ##删除某环境(如果需要)
```
