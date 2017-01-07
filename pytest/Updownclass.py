# 升降级考核类UpDownNum,up_num:返回当前职级和升级数，up_down:d返回当前职级和降级数
# add commit 

class UpDownNum:
    def __init__(self, pos_list, up_list, down_list, position, score):
        self.score = score
        self.position = position
        self.pos_list = pos_list
        self.up_list = up_list
        self.down_list = down_list

    def up_num(self):
        up = 0
        try:
            index = self.pos_list.index(self.position)
        except ValueError:
            print('The position is not exist!')
        else:
            for level in range(index, len(self.pos_list)):
                if self.score >= self.up_list[level]:
                    up += 1
                else:
                    pass
            # 升级后新的索引
            index_new = index + up
            # 索引超出position的长度时按最高职位算
            up_position_new = self.pos_list[index_new] if index_new <= len(self.pos_list)-1 else self.pos_list[len(self.pos_list)-1]
            return up_position_new, up

    def down_num(self):
        down = 0
        try:
            index = self.pos_list.index(self.position)
        except ValueError:
            print('The position is not exist!')
        else:
            for level in range(index, -1, -1):
                if self.score < self.down_list[level]:
                    down += 1
                else:
                    pass
            index_new = index - down
            #  索引比0小时按淘汰算
            down_position_new = '淘汰' if index_new < 0 else self.pos_list[index_new]
            return down_position_new, down


