class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        # x는 person1의 위치
        # y는 person2의 위치
        # z는 person3의 위치. 움직이지 않음
        # person1,2는 3을 향해 같은 속도로 움직임
        # person3에 먼저 도착하는 person을 return. 같이 도착하면 0을 리턴

        dist1 = abs(z - x)
        dist2 = abs(z - y)

        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        elif dist1 == dist2:
            return 0


