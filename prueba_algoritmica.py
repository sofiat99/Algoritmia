from datetime import datetime, timedelta
import time
import uuid
import random
import multiprocessing

class prueba():
    
    def __init__(self,quantity):
        self.quantity = quantity
        self.__orders_processed = 0
        self.__last_printed_log = datetime.now()
        
    def process(self):
        start_time = time.time()   
        process1 = multiprocessing.Process(target=self.generate_data)
        process1.start()
        process2 = multiprocessing.Process(target=self.generate_data)
        process2.start()
        process2.join()
        delay = time.time() - start_time
        return delay
        
    def __log(self, message):
        print(f"{datetime.now()} > {message}")
        
    def save_data(self,number_generate):
        id,number = number_generate
        self.__orders_processed += 1
        if datetime.now() > self.__last_printed_log:
            self.__last_printed_log = datetime.now() + timedelta(seconds=5)
            self.__log(f"Total orders executed: {self.__orders_processed}/{self.quantity}")
        self.__log(f"Order [{number}] {id} was successfully prosecuted.")
        time.sleep(random.uniform(0,1))
    def generate_data(self):
        integer_list = {i: uuid.uuid4() for i in range(1,self.quantity)}
        list(map(self.save_data, integer_list.items()))
        

if __name__ == "__main__":
    
    data_fake = prueba(5_00)
    delay = data_fake.process()
    print(f"{datetime.now()} > Tiempo de ejecucion: {delay} segundos...")