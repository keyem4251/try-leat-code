#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # matrixを作成
        matrix = [[] for i in range(numRows)]

        # matrixのindexを行を0で設定
        row_i = 0

        # 文字を設定する行の
        reverse_col_i = numRows - 1
        
        # 設定した文字数
        c_count = 0

        # 文字列分ループしてrowsに詰める
        while c_count < len(s):
            # 行を進める
            if reverse_col_i == 0 or reverse_col_i == (numRows - 1):
                matrix[row_i].append(s[c_count])
                c_count += 1
            elif row_i == reverse_col_i:
                matrix[row_i].append(s[c_count])
                c_count += 1
            else:
                matrix[row_i].append("")

            row_i += 1
            
            if row_i == numRows:
                row_i = 0
                
                if reverse_col_i == 1:
                    reverse_col_i = numRows - 1
                else:
                    reverse_col_i -= 1
        
        result = ""
        for row in matrix:
            for col in row:
                if col:
                    result += col

        return result

# @lc code=end

