#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # matrixを作成
        matrix = [[] for i in range(numRows)]

        # matrixのindexを行と列を0で設定
        row_i = 0
        col_i = 0

        is_desc = True

        # 文字列分ループしてrowsに詰める
        for c in s:
            matrix[row_i][col_i].append(c)
            
            # 行を1つ進める
            if is_desc:
                row_i += 1
            else:
                row_i -= 1
                col_i += 1

            if row_i == numRows:
                is_desc = False
                col_i += 1
                row_i -= 1

            if row_i == 0:
                is_desc = True
            

# @lc code=end

