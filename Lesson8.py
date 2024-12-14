#КАК ЭТО ДЕЛАТЬ

import time
import unittest


def measure_time(func):
    def wrapper(*args, **kwargs): #это нечто кажется должно передавать кол-во аргументов
        start_time = time.time() #ну, по крайней мере гугл так сказал
        result = func(*args, **kwargs) #ну если подумать, вроде должно работать
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds.")
        return result
    return wrapper


@measure_time
def slow_function(n):
    time.sleep(n)
    return n


class TestMeasureTimeDecorator(unittest.TestCase):
    def test_slow_function(self):
        result = slow_function(1)
        self.assertEqual(result, 1)

    def test_fast_function(self):
        @measure_time
        def fast_function(x):
            return x + 1

        result = fast_function(10)
        self.assertEqual(result, 11)

if __name__ == "__main__":
    unittest.main()

#три раза не сработало, на помощь пришли форумы с синтаксом и шедевроЧатГпт, пофиксил баги после гпт и вроде как работает
