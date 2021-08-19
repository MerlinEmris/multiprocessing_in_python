import unittest
import multiprocess as project


class TestProject(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(project.fib(3), 3)
        self.assertEqual(project.fib(4), 5)
        self.assertEqual(project.fib(5), 8)

    def test_parallel(self):
        self.assertEqual(project.parallel(1, 5)[1][0], [1, 1, 2, 3, 5])

    def test_normal(self):
        self.assertEqual(project.normal(1, 5)[1], [1, 1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
