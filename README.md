# VisualAnalytics_Back
可视分析(服务端)，数据可视化课程项目。

![Anaconda](https://img.shields.io/badge/Anaconda-4.6.12-brightgreen.svg)
![MySQL](https://img.shields.io/badge/MySQL-5.7.21-blue.svg)

## 前端项目地址
[VisualAnalytics_Front](https://github.com/LauZyHou/VisualAnalytics_Front)

## 配置

在用户家目录下的`.condarc`文件中确保保存了清TUNA源：
```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
custom_channels:
  conda-forge: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

创建Python虚拟环境：
```
conda env create -f env.yaml
```

在PyCharm中将`apps`目录mark为蓝色(Sources Root)。

## 使用虚拟环境

```
conda init
# 进入
activate DRF
# 退出
deactivate
```