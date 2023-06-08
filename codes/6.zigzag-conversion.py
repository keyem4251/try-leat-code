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

        # 下りか、上りか
        is_desc = True

        # 文字列分ループしてrowsに詰める
        for c in s:            
            # 行を進める
            if is_desc:
                # 下りはそのまま文字列入れる
                matrix[row_i].append(c)
                row_i += 1
            else:
                # 上りは
                matrix[row_i].append("")
                row_i -= 1

            if row_i == numRows:
                is_desc = False
                row_i -= 1

            if row_i == 0:
                is_desc = True

        result = ""
        for row in matrix:
            for col in row:
                if col:
                    result.append(col)

        return result

# @lc code=end

