<div align="center">
  <img src="https://cdn.worldvectorlogo.com/logos/django.svg" width="56" alt="django logo">
</div>

# 目录结构

- [环境配置]()
- [项目结构]()
- [创建项目]()
- [创建应用]()
- [参考]()

## 环境配置

- **Python**: macOS 自带 Python3 环境，windows 需要单独安装[最新版本](https://www.python.org/downloads/)
- **数据库**：该项目使用 django 默认自带的 SQLite 数据库

## 项目结构

## 创建项目

- 第一步：创建项目名

  ``` sh
  $ mkdir <PROJECT_NAME>
  ```

- 第二步：安装本地虚拟环境

  > 当然你也可以安装全局虚拟环境

  ``` sh
  $ cd <PROJECT_NAME>
  $ python3 -m venv venv
  ```

- 第三步：激活本地虚拟环境

  ``` sh
  $ source venv/bin/activate
  ```

- 第四步：安装 Django

  ``` sh
  $ pip install django
  ```

- 第五步：创建项目

  ``` sh
  $ django-admin startproject <PROJECT_NAME> .
  ```

- 第六步：创建超级管理员账号

  ``` sh
  $ python manage.py createsuperuser
  ```

  至此，我们一个基础的项目结构和本地虚拟环境就正常建立起来了。

## 创建应用

在 Django 中，每一个应用都是一个 Python 包，并且遵循着相同的约定。Django 自带一个工具，可以帮你生成应用的基础目录结构，这样你就能专心写代码，而不是创建目录了。关于项目与应用的区别，大家可参考[官网](https://docs.djangoproject.com/zh-hans/4.2/intro/tutorial01/#creating-the-polls-app)介绍

- 第一步：创建 apps 目录

> 这个看自己喜好，个人习惯把所有的 app 归类到 apps 目录之下

``` sh
$ mkdir apps
```

- 第二步：创建一个应用

``` sh
$ mkdir apps/<APP_NAME>
$ python manage.py startapp <APP_NAME> <APP_DIRECTORY>
```

## 参考

- [Django 官网](https://www.djangoproject.com/)
- [Python Tutorial](https://www.pythontutorial.net/)
