import unittest
from Updownclass import UpDownNum


class Testupdown(unittest.TestCase):
    def setUp(self):
        self.position_list1 = ['A', 'B', 'C', 'D']
        self.up_score_list1 = [20, 30, 40, float('inf')]
        self.down_score_list1 = [10, 15, 20, 25]
        # self.position_old1 = 'B'
        # self.score_old1 = 25

    def test_up_num(self):
        self.upnumA1 = UpDownNum(self.position_list1,self.up_score_list1,self.down_score_list1,'A',25).up_num()
        self.upnumA2 = UpDownNum(self.position_list1,self.up_score_list1,self.down_score_list1,'A',30).up_num()
        self.upnumA3 = UpDownNum(self.position_list1,self.up_score_list1,self.down_score_list1,'A',45).up_num()
        self.assertEqual(self.upnumA1[0],'B','A升一级成功')
        self.assertEqual(self.upnumA2[0],'C','A升二级成功')
        self.assertEqual(self.upnumA3[0],'D','A升三级成功')

    def test_down_num(self):
        self.downnumD1 = UpDownNum(self.position_list1,self.up_score_list1,self.down_score_list1,'D',30).down_num()
        self.downnumD2 = UpDownNum(self.position_list1,self.up_score_list1,self.down_score_list1,'D',18).down_num()
        self.downnumD3 = UpDownNum(self.position_list1,self.up_score_list1,self.down_score_list1,'D',13).down_num()
        with self.subTest(name='降一级'):
            self.assertEqual(self.downnumD1[0],'C','D降一级成功')
        # if self.downnumD2[0]:
        with self.subTest(i=2):
            self.assertEqual(self.downnumD2[0],'B','D降二级成功')
        # if self.downnumD3[0]:
        with self.subTest(i=3):
            self.assertEqual(self.downnumD3[0],'A','D降三级成功')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()






