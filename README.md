# BBS
a bulletin board site  

项目介绍：  

   1. 前端外观：使用了`bbs.deepin.org`的外观设计。  
   2. 后端功能：用户模型：子类化AbstractBaseUser。使用中间模型链接多个外键，再到用户到多对多键。论坛模型：分为4个层次，Category，Forum，Topic，Post。对以类方法实现的模型属性使用@property装饰器，以免写入数据库。对特别消耗内存对计算使用@cached_property。论坛模型改进：后期会将每个模型的类方法整合到模型管理器中。并对可以由现有数据库中对字段可以容易计算出来模型类属性改为类方法。对模型对重复查询改为使用QuerySets进行惰性计算，减少内存开销。视图：函数视图，未使用通用类视图。信号：在用户创建时使用，以获得最新的用户实例对象。站内用户间消息和相关订阅提醒：使用支持服务端推送特性的第三方应用`django-websocket-redis`来解决客户端和不能够与服务器双向通信的问题。
   3. Django版本：Django 1.8。

************
http://www.django-china.ml/
