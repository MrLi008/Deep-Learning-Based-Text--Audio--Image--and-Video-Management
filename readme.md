# 基于深度学习的文案语音图片视频管理分析-视频矩阵系统

### 配置信息

  database: vm790_bcfe8a202787453d

  default port:9100

### 部署启动步骤

1. 激活python环境
2. 项目根目录下执行:
   3. 建库,建表,初始化administrator管理员密码,默认123456
   4. 启动项目,可用 123456 123456登入系统

# code

    check.bat
    init_project.bat
    start_project.bat

### 代码结构

 a_simulink_unit/generate_detect.py # 这个是算法处理部分

 appcenter/admin.py # 后台管理

 appcenter/models.py # 数据库表和字段定义

 config_busi/views.py # 前端增删改查

 config_visual/views.py # 大屏 你这个没有。

 sys_user/views.py  # 这里是登陆注册的

 templates/config_busi/auto_detect.html # 这个是图像合成的界面

 templates/login.html # 前端登录

 templates/register.html# 前端注册

 templates/index_v1.html # 前端 主页

# Spark

spark:3.0.2

python==3.8.18
pip==23.3.1
py4j==0.10.9
pyspark==3.0.2
setuptools==68.0.0
wheel==0.41.2




### 默认数据集在a_simulink_unit\data文件夹.

算法类的数据集同上,需要上传视频和图片的同上


法律声明
若接收此份代码，即表示您已同意以下条款。若不同意以下条
款，请停止使用本软件。
本文档版权所有《952934650@qq.com》。保留任何未在
本文档中明示授予的权利。文档中涉及《952934650@qq.com》的专有
信息。未经《952934650@qq.com》事先书面许可，任何单位和个人不
得复制、传递、分发、使用和泄漏该文档以及该文档包
含的任何图片、表格、数据及其他信息。
在未经《952934650@qq.com》或第三方权利人事先书面同意的情况
下，阅读本文档并不表示以默示、不可反言或其他方式
授予阅读者任何使用本文档中出现的任何标记的权利。
本产品符合有关环境保护和人身安全方面的设计要求，
产品的存放、使用和弃置应遵照产品手册、相关合同或
相关国法律、法规的要求进行。
本文档按“现状”和“仅此状态”提供。本文档中的信息随着
《952934650@qq.com》产品和技术的进步将不断更新，《952934650@qq.com》不再
通知此类信息的更新。