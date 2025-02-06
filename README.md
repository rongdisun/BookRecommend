## 基于Django框架实现的推书推荐系统

### 1、项目简介

**本项目分为用户模块、图书模块、资讯模块、论坛模块。**

用于基于Django自带的用户功能，并对其进行拓展，很好的实现了基于角色的用户权限控制；图书模块为本系统的核心功能，本模块是实现了图书借阅功能、图书收藏功能、图书图表分析 、推书推荐、图书评分等功能，在图书推荐部分根据协同过滤算法计算出推荐指数；资讯模块主要包含文章分类、文章内容、文章标签，同时支持搜索功能；论坛模块类似于百度贴吧，大家可以开放式的发布帖子，跟帖等，并且实现了关注功能。本项目同时使用了富文本编辑器。

### 2、环境配置

- python==3.10.0
- django==4.2.6
- bootstrap==5.2.3

项目中还使用到了一些其他的django比较好用的插件，在这里就不一一列举了。

### 3、功能展示

#### **首页：实现了图书的分页、图书组合式搜索（根据图书分类、图书书名的关键字组合搜索）**

![image-20250206214512573](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206214512573.png)

#### **图书借阅记录**

![image-20250206215829556](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206215829556.png)

![image-20250206215902079](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206215902079.png)

![image-20250206215933809](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206215933809.png)

#### **图书详情页**

![image-20250206220057850](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206220057850.png)

#### **图书评论部分**

![image-20250206220157268](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206220157268.png)

#### 图书推荐部分

![image-20250206220416760](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206220416760.png)

#### 图表分析

![image-20250206220504210](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206220504210.png)

![image-20250206220522390](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206220522390.png)

#### 最新资讯

![image-20250206221049938](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206221049938.png)

![image-20250206221117480](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206221117480.png)

#### 论坛模块

![image-20250206221206302](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206221206302.png)

![image-20250206221316041](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206221316041.png)

#### 用户模块

![image-20250206221600626](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206221600626.png)

![image-20250206221621041](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206221621041.png)

![image-20250206221633954](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206221633954.png)

#### 后台管理页面

![image-20250206221717936](https://raw.githubusercontent.com/rongdisun/learn/main/image-20250206221717936.png)

#### 4、获取源码方式

![二维码](https://raw.githubusercontent.com/rongdisun/learn/main/%E4%BA%8C%E7%BB%B4%E7%A0%81.jpg)

