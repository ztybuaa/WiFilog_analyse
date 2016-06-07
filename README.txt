基于:numpy
----------数据预处理----------
1. data_clean:数据清洗，字段粗提取
2. field_extract:字段精细提取
3. data_summarize:数据整合
----------广场分析----------
4. plaza_count:计算广场每天的平均点击次数、停留时间和设备数
5. plaza_count_sum:plaza_count汇总（设备数计算不准，没有去重）
6. plaza_feature:计算广场的设备比例方差、平均点击时间、点击时间方差、平均点击间隔、点击间隔信息熵、主要品牌数
7. plaza_feature_sum:plaza_feature汇总
8. plaza_device:计算各广场的各品牌设备数量
9. plaza_interval_time:统计广场的点击间隔频率
10. plaza_adclick:广场广告点击汇总
----------用户分析----------
11. user_sort:按用户整理所有数据
12. user_detail:根据cmac查询详细访问记录
----------时间分析----------
13. checkin_timeline:各时间段登录人数（第一次点击）
14. day_hour_analyse:分星期分时间段统计
15. day_hour_analyse_sum:day_hour_analyse汇总
----------设备分析----------
16. device_sort:计算品牌的设备数量、点击时间、各类广告点击数
17. iphone_sort:分析苹果各版本设备的点击情况
----------网址分析----------
18. url_analyse:url提取
19. url_keyword:url汇总
20. redirect_analyse:redirect提取
21. redirect_keyword:redirect汇总
----------数据可视化----------
22. data_visualization_pre:可视化数据准备，按广场统计