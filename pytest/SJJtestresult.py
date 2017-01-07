from Updownclass import UpDownNum


def cla_result(position_list, up_score_list, down_score_list, position_old, score_old):
    c = UpDownNum(position_list, up_score_list, down_score_list, position_old, score_old)
    position_new = c.up_num() if c.up_num()[0] != position_old else c.down_num()
    return position_new


first = ['北京', '上海', '武汉', '广州', '成都', '天津', '深圳', '西安', '杭州', '苏州', '重庆', '南京']
second = ['青岛', '沈阳', '合肥', '济南', '郑州', '宁波', '长沙', '东莞', '石家庄', '南昌', '大连', '昆明',
          '南宁', '常州', '无锡', '长春', '海南', '徐州', '厦门', '惠州', '佛山']


# # 正式员工三挡 升级、降级的考核的考核标准
# first_up = [600000, 1000000, 1600000, 2400000]
#
# first_down = [300000, 500000, 800000, 1200000, 2400000]
#
# second_up = [400000, 600000, 1000000, 1600000]
#
# second_down = [200000, 300000, 500000, 800000, 1600000]
#
# third_up = [300000, 500000, 800000, 1200000]
#
# third_down = [100000, 200000, 400000, 600000, 1000000]

position_list1 = ['销售经理','高级销售经理','销售副总监','销售总监','常务副总经理、副总经理、总经理助理']
position_list1 = ['A', 'B', 'C', 'D']
up_score_list1 = [20, 30, 40, 50]
down_score_list1 = [10, 15, 20, 25]

position_old1 = 'B'
score_old1 = 25
# c = UpDownNum(position_list, up_score_list, down_score_list, position_old, score_old)
# print(c.up_num())
print(cla_result(position_list1, up_score_list1, down_score_list1, position_old1, score_old1))


