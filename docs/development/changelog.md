## Version 0.2.5 (2022-08-12)

### 特性与改进
+ 更新并锚定polars模块的版本为0.14.0。

## Version 0.2.4 (2022-08-03)

### Bug修复
+ 解决原始csv文件的读取错误。

## Version 0.2.3 (2022-07-30)

### 特性与改进
+  利用polars替代pandas进行区域信息的读取和查询，速度起飞（详细结果可见[基准测试](./benchmark.md)部分）。
+  重构了Addr类，以及以之为基础的各个函数。一般情况下在查询时可以通过输入`level`参数进一步加快查询速度，并在很大程度上解决区域名简称重复的问题。

### Bug修复
+  修复了一些bug，比如同名简称区域查询的错误反馈。