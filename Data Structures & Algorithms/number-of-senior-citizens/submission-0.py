class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for detail in details:
            for i in range(len(detail)):
                age = str(detail[11]) + str(detail[12])
                if  int(age) > 60:
                    c += 1
                    break

        return c