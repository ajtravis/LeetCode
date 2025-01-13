class Solution(object):
    def minDeletionSize(self, rows):
        
        count = 0
        for index in range(len(rows[0])):
            previous = rows[0][index]
            for row in rows[1:]:
                letter = row[index]
                if letter < previous:
                    count += 1
                    break
                previous = letter

        return count