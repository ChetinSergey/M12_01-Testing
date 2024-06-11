from main import Student
import unittest


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.student_1 = Student('Sergey')
        self.student_2 = Student('Anton')

    def test_walk(self):
        for i in range(10):
            self.student_1.walk()
        self.assertEqual(self.student_1.distance, 500,
                         f'Дистанции не равны [дистанция человека {self.student_1}] != 500')

    def test_run(self):
        for i in range(10):
            self.student_2.run()
        self.assertEqual(self.student_2.distance, 1000,
                         f'Дистанции не равны [дистанция человека {self.student_2}] != 1000')

    def test_greater(self):
        for i in range(10):
            self.student_1.walk()
            self.student_2.run()
        self.assertGreater(self.student_1.distance, self.student_2.distance,
                           f'Идущий человек - {self.student_1.name} должен преодолеть дистанцию меньше, '
                           f'чем бегущий человек - {self.student_2.name}')

    def test_less(self):
        for i in range(100):
            self.student_1.walk()
            self.student_2.run()
        self.assertLess(self.student_2.distance, self.student_1.distance,
                        f'Бегущий человек - {self.student_2.name} должен преодолеть дистанцию больше, '
                        f'чем идущий человек - {self.student_1.name}')


if __name__ == '__main__':
    unittest.main()
