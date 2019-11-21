

def product_two_largest_num(nums):

    '''
    :input [1, 2, 3]
    :return 最大两个数的乘积
    :example:
        input [1, 2, 3] ---> 2 * 3
    '''

    if len(nums) < 2:
        raise Exception('nums length error')

    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if i == 1:
            return nums[len(nums) - 1], nums[len(nums) - 2]

a = [1, 2, 3, 10, 11, 12]
print(product_two_largest_num(a))

# def test():
#     nums_test1 = [1, 2, 3]      # 输出为6
#     nums_test2 = [3, 2, 1]      # 输出为6
#     nums_test3 = [1, 1, 1]      # 输出为1
#     nums_test4 = [0, 0, 0]      # 输出为0
#
#     assert 6 == product_two_largest_num(nums_test1)
#     assert 6 == product_two_largest_num(nums_test2)
#     assert 1 == product_two_largest_num(nums_test3)
#     assert 0 == product_two_largest_num(nums_test4)
#
#     print('----- 测试通过 ------')
#
#
# # test()




class RGB:

    def __init__(self, R=0, G=0, B=0):
        '''

        :param R:
        :param G:
        :param B:
        '''
        if R < 0 or R > 255 or G < 0 or G > 255 or B < 0 or B > 255:
            raise Exception('out of color range')

        self.R = R
        self.G = G
        self.B = B

    def __repr__(self):
        return 'RGB({},{},{})'.format(self.R, self.G, self.B)

class Plain(object):

    #   默认画布大小　10 * 10
    def __init__(self, width=10, height=10):
        '''

        :param width:
        :param height:
        '''
        self.width = width
        self.height = height

        self.base = []

        # 根据 with, height 将初始画布变为二维数组
        for i in range(height):
            self.base.append([None])
            for j in range(width):
                self.base[i].append(None)

    #   输入 width height, 和对应的r g b 参数
    def draw(self, width, height, r, g, b):
        '''

        :param width:
        :param height:
        :param r:
        :param g:
        :param b:
        :return:
        '''
        if width > self.width or height > self.height:
            raise Exception('out of range')

        rgb = RGB(r, g, b)

        #   将输入的width， height 画在 self.base上
        for i in range(len(self.base)):
            if i < height:
                for j in range(len(self.base[i])):
                    if j < width:
                        self.base[i][j] = rgb

    def PrintImg(self):
        '''

        :return:
        '''
        for i in self.base:
            print(i)

    def SaveImage(self, filename):
        '''

        :param filename:
        :return:
        '''
        with open(filename, 'w') as f:
            f.write(str(self.base))


pla = Plain()
pla.draw(2, 3, 255, 1, 1)
pla.PrintImg()
pla.SaveImage('test.txt')
