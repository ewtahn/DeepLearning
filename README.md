
[TOC]
# DeepLearning学习步骤
## 环境搭建
### 网络环境
用ss翻墙
先安装ss。

通过PPA源安装，仅支持`Ubuntu`14.04或更高版本。

[shadowsocks](https://github.com/shadowsocks/shadowsocks-qt5/wiki/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97)

```
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```




### 软件环境
利用`Anaconda`管理`python`的科学包。不过网速有限，暂时安装了`miniconda`，安装哪个版本无所谓，注意配置环境变量。
`conda`一个特点是可以管理多个独立的环境，这样python2，3可以放在不同的环境里。

下载安装`miniconda`
```
$ conda create -n py36 python=3.6 ##创立环境
$ source activate py36            ##激活环境
$ conda list                      ##查看该环境下的包
$ conda install numpy pandas matplotlib##安装numpy包等
$ conda install jupyter notebook      ##安装jupyter notebook
$ conda env export > environment.yaml ##保存环境配置到文件(如果需要)
$ conda env create -f environment.yaml##根据文件来创建环境(如果需要)
```

如果需要
```
$ source deactivate py36          ##离开环境
$ conda env list                  ##查看一共有几个环境
$ conda env remove -n py36        ##删除某环境(如果需要)
```
