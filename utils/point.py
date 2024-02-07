import random


class Point:
    '''
    Класс Point предназначен для хранения координат вершины на плоскости.

    Реализация проверки пересечения двух отрезков взята с сайта:
    https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def change_position(self, value: float = 0.5) -> 'Point':
        '''
        Меняет позицию точки на плоскости.

        Args:
        value (int/float): Коэффициент для изменения координат.

        Returns:
        Point: Точка с новыми координатами.
        '''
        # Для более плавной анимации, но худшей производительности:
        # sign = random.choice([-1, 1])
        # self.x = self.x + random.random() * sign * value
        # self.y = self.y + random.random() * sign * value

        # Для худшей анимации, но хорошей производительности:
        self.x = random.random() * value
        self.y = random.random() * value
        return self.__class__(self.x, self.y)

    @staticmethod
    def onSegment(p: 'Point', q: 'Point', r: 'Point') -> bool:
        '''
        Даны 3 коллинеарные точки p, q, r.
        Функция проверяет, лежит ли точка q на отрезке pr.

        Args:
        p (Point): Начало отрезка.
        q (Point): Точка, которую надо проверить.
        r (Point): Конец отрезка.

        Returns:
        bool: True если точка q лежит на отрезке pr, иначе False.
        '''
        if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
            return True
        return False

    @staticmethod
    def orientation(p, q, r) -> int:
        '''
        Ориентация упорядоченного триплета (p, q, r).

        Returns:
        0: Collinear points
        1: Clockwise points
        2: Counterclockwise
        '''
        val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
        if val > 0:
            return 1    # Clockwise orientation
        if val < 0:
            return 2    # Counterclockwise orientation
        return 0        # Collinear orientation

    @staticmethod
    def doIntersect(p1, q1, p2, q2) -> bool:
        '''
        Определяет, пересекаются ли два отрезка p1q1 и p2q2.

        Args:
        p1 (Point): Начало первого отрезка.
        q1 (Point): Конец первого отрезка.
        p2 (Point): Начало второго отрезка.
        q2 (Point): Конец второго отрезка.

        Returns:
        bool: True если отрезки пересекаются, иначе False.
        '''
        # Находим 4 ориентации, необходимые для
        # Общего и особенных случаев
        o1 = Point.orientation(p1, q1, p2)
        o2 = Point.orientation(p1, q1, q2)
        o3 = Point.orientation(p2, q2, p1)
        o4 = Point.orientation(p2, q2, q1)

        # Общий случай
        if ((o1 != o2) and (o3 != o4)):
            return True

        # Особенные случаи

        # p1, q1 и p2 коллинеарные и p2 лежит на отрезке p1q1
        if ((o1 == 0) and Point.onSegment(p1, p2, q1)):
            return True

        # p1, q1 и q2 коллинеарные и q2 лежит на отрезке p1q1
        if ((o2 == 0) and Point.onSegment(p1, q2, q1)):
            return True

        # p2, q2 и p1 коллинеарные и p1 лежит на отрезке p2q2
        if ((o3 == 0) and Point.onSegment(p2, p1, q2)):
            return True

        # p2, q2 и q1 коллинеарные и q1 лежит на отрезке p2q2
        if ((o4 == 0) and Point.onSegment(p2, q1, q2)):
            return True

        return False
