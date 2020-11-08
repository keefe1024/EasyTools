# masscan 扫描结果xml格式转xlsx表格脚本

## 0x00 使用说明

### requirement：

```python
pip install bs4
pip install xlsxwriter
```

### 常用的masscan语句：

```bash
masscan 192.168.0.0/16 -p80,443,8080,1433,3306 --banners --rate=100000 -oX scan.xml
```

### python脚本使用说明：

```python
# 默认运行脚本读取scan.xml导出为scan.xlsx
-x:指定xml文件
--xml:指定xml文件
-o:指定输出文件名 -o 1.xlsx
--output:指定输出文件名 -output 1.xlsx
```

```bash
python3 masscan_xml_to_xls.py -x 2.xml -o 2.xlsx
```

![image-20201108142152971](https://github.com/keefe1024/EasyTools/blob/master/masscan_xml_to_xls/image-20201108142152971.png?raw=true)