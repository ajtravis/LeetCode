class Solution:
    def calPoints(self, operations: List[str]) -> int:
        i = 0
        record = []
        def helper(x, record):
            if x == "+":
               record.append((record[-1] + record[-2]))
            elif x == "D":
                record.append(2 * record[-1])
            elif x == "C":
                record = record[:-1]
            else:
                record.append (int(x))
            return record

        while i < len(operations):
            record = helper(operations[i], record)
            i+=1
        return sum(record)