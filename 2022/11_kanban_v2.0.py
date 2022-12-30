import time
import  os

# 字符点阵
dict = {

'a' : [[0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'b' : [[1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0]],
'c' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
'd' : [[1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0]],
'e' : [[1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]],
'f' : [[1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]],
'g' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0]],
'h' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'i' : [[0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0]],
'j' : [[0, 0, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0],
     [1, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0]],
'k' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0]],
'l' : [[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]],
'm' : [[1, 0, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'n' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'o' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
'p' : [[1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]],
'q' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0],
     [1, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0]],
'r' : [[1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0]],
's' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
't' : [[1, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]],
'u' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
'v' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0]],
'w': [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0],
     [1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 1, 0]],
'x' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'y' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]],
'z' : [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]],
' ': [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
'.' : [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]],
'?' : [[0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
}

abc = input('input words :')

# 列表重新排序成输出格式, 是整个句子的点阵
str_list = [dict.get(alpha) for alpha in abc]



# print(str_list)
'''
ab=
[
[[0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]], 
[[1, 1,1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0]]

]
'''





def get_in_out_char(str_list,in_out_position):
          # 进出屏幕边缘的 字符
     # in_out_char = []
     # in_out_char.append(str_list[in_out_position] )  
     in_out_char = [str_list[in_out_position]]
     # print('here2', in_out_char)
     return in_out_char

def sliced_char_l_half(in_out_char, width):
     l_half_char =[[]]
     for height in range(0,7):
          tmp = in_out_char[0][height][:width] # in_out_char  进来的是包含一个字符的列表， 所以索引第[0]个
          l_half_char[0].append(tmp)
     return l_half_char

def sliced_char_r_half(in_out_char, width):
     r_half_char =[[]]
     for height in range(0,7):
          tmp = in_out_char[0][height][width:]
          r_half_char[0].append(tmp)
     return r_half_char     

def before_in_char(str_list, start, in_out_position):

     before_char = str_list[start:in_out_position]

     return before_char






in_out_position = 0 # 进入屏幕的字符,指针初始为0
def get_screen_list(str_list,screen_width, in_out_position):
     empty_list = [dict.get(' ') for i in range(0,screen_width + 1)]
     for in_out_position in range(0,len(str_list)): # 指针遍历字符串点阵
          for width in range(1,7): #每个字遍历循环切片6次
               str_prt =[]
               if in_out_position < screen_width and in_out_position == 0: # 第一个字符进入画面
                    
                    empty_head = sliced_char_r_half([empty_list[in_out_position]], width)
                    empty_body = before_in_char(empty_list,in_out_position + 1, len(empty_list)-1)
                    # empty_end = sliced_char_l_half([empty_list[-1]], width)

                    tmp = get_in_out_char(str_list,in_out_position)           #进入画面的字符
                    # char_head = sliced_char_l_half(tmp, width)

                    char_end = sliced_char_l_half(tmp, width)             # 进入画面的字符的左半部的列表
                    str_prt = empty_head + empty_body  + char_end

                    # print('ioposi==0 str_prt:',str_prt)
                    prtstars(str_prt)


               elif in_out_position < screen_width and in_out_position >= 1: #进入画面的字符 >= 1个,且小于屏幕宽度时, 已进入字符+进入字符左半部

                    empty_head = sliced_char_r_half([empty_list[in_out_position]], width)
                    empty_body = before_in_char(empty_list,in_out_position + 1, len(empty_list)-1)

                    char_body = before_in_char(str_list,0, in_out_position) # 已经进入的整字字符
                    tmp = get_in_out_char(str_list,in_out_position)             # 正在进入的字符
                    char_end = sliced_char_l_half(tmp, width)               # 正在进入的字符的左半部
                    str_prt = empty_head + empty_body + char_body + char_end

                    # print('ioposi==0 str_prt:',str_prt)
                    prtstars(str_prt)


               elif in_out_position >= screen_width and in_out_position < len(str_list)-1:                             #进入画面的字符数大于屏幕宽度,需要同时切片屏幕左侧和右侧字符
                    head_tmp = get_in_out_char(str_list,in_out_position-screen_width)    #左侧出画面的字符
                    char_head = sliced_char_r_half(head_tmp, width)                  #左侧出画面字符的 右半部
                    char_body = before_in_char(str_list, in_out_position - screen_width + 1,in_out_position) # 中间字符
                    end_tmp = get_in_out_char(str_list,in_out_position)                 # 右侧进入画面的字符
                    char_end = sliced_char_l_half(end_tmp, width)                   # 右侧进入画面的字符的左半部
                    if width < 6:
                         str_prt= char_head + char_body + char_end
                    elif width == 6:
                         str_prt= char_body + char_end
                    prtstars(str_prt)




          # print('after for width',width)



'''
str_prt = [[[0], [0], [0], [0], [0], [0], [0]], 
[[0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1,1, 1, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]], 
[[0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1,0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]], 
[[0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]], 
[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]]]
'''





def prtstars(str_prt):
     print('\n\n')
     time.sleep(0.05)
     if os.name == 'nt':
          os.system('cls')
     elif os.name =='posix':
          os.system('clear')

     for height in range(len(str_prt[0])):   # 按行遍历
          for i in range(0,len(str_prt)):              #遍历 str_prt 列表中的item 
               for width in range(0,len(str_prt[i][height])):  #按列遍历
                    if str_prt[i][height][width]  == 1:
                         print("* ", end = "")
                    if str_prt[i][height][width] == 0:
                         print("  ", end = "")
          print()   # 每打印一行换行




while True:
     # 参数： 字符串 ， 屏幕宽度， 
     get_screen_list(str_list,4,in_out_position)  #



