# 山东大学青岛校区山大V卡通2.0版本电量查询接口

曾经的电量查询脚本[SDUQD-Electricity-Inquiry](https://github.com/SkywalkerWei/SDUQD-Electricity-Inquiry) 停止维护，本人在抓包研究后决定自己写一款新的脚本。

目前可查 `S1 S2 S5 S6 S7 S8 S9 S10 S11 B1 B2 B5 B9 B10 T1 T2 T3`

## 依赖安装

- `pip install -r requirements.txt`
- Python版本为3.12.7

## 使用方法

在config.yaml中填入手机抓包获取的 `Synjones-Auth` 字段信息。

之后在其他 Python 文件中调用 query 函数即可。

## 隐私声明

所有服务均在本地运行，不会保存或上传任何用户数据，可放心使用。可能会在同级目录下生成缓存文件，清理不影响使用。

## 未来计划

- 加入手机抓包教程
- 制作可视化页面
