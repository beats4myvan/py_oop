# from encapsulation.project.caretaker import Caretaker
# from encapsulation.project.cheetah import Cheetah
# from encapsulation.project.keeper import Keeper
# from encapsulation.project.lion import Lion
# from encapsulation.project.tiger import Tiger
# from encapsulation.project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def is_enough_capacity(self):
        return len(self.animals) < self.__animal_capacity

    def is_enough_budget(self, price):
        return price <= self.__budget

    def is_enough_worker_space(self):
        return len(self.workers) < self.__workers_capacity

    def add_animal(self, animal, price):
        if self.is_enough_budget(price) and not self.is_enough_capacity():
            return f'Not enough space for animal'
        elif not self.is_enough_budget(price):
            return f'Not enough budget'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if self.is_enough_worker_space():
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if self.is_enough_budget(salaries):
            self.__budget -= salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):

        sum_needs = 0
        for animal in self.animals:
            sum_needs += animal.get_needs()
        if not self.is_enough_budget(sum_needs):
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum_needs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_result = f'You have {len(self.animals)} animals\n'
        lions = [lion.__repr__() for lion in self.animals if lion.__class__.__name__ == "Lion"]
        tigers = [tiger.__repr__() for tiger in self.animals if tiger.__class__.__name__ == "Tiger"]
        cheetahs = [cheetahs.__repr__() for cheetahs in self.animals if cheetahs.__class__.__name__ == 'Cheetah']
        amount_of_lions = len(lions)
        amount_of_tigers = len(tigers)
        amount_of_cheetahs = len(cheetahs)
        animals_result += f'----- {amount_of_lions} Lions:\n'
        if lions:
            for lion in lions:
                animals_result += f'{lion}\n'

        animals_result += f'----- {amount_of_tigers} Tigers:\n'
        if tigers:
            for tiger in tigers:
                animals_result += f'{tiger}\n'

        animals_result += f'----- {amount_of_cheetahs} Cheetahs:\n'
        if cheetahs:
            for cheetah in cheetahs:
                if cheetahs.index(cheetah) == len(cheetahs) - 1:
                    animals_result += f"{cheetah}"
                else:
                    animals_result += f"{cheetah}\n"
        return animals_result

    def workers_status(self):
        workers_result = f'You have {len(self.workers)} workers\n'
        keepers = [keeper.__repr__() for keeper in self.workers if keeper.__class__.__name__ == 'Keeper']
        caretakers = [caretaker.__repr__() for caretaker in self.workers if caretaker.__class__.__name__ == 'Caretaker']
        vets = [vet.__repr__() for vet in self.workers if vet.__class__.__name__ == 'Vet']

        workers_result += f'----- {len(keepers)} Keepers:\n'
        if keepers:
            for keeper in keepers:
                workers_result += f'{keeper}\n'

        workers_result += f'----- {len(caretakers)} Caretakers:\n'
        if caretakers:
            for caretaker in caretakers:
                workers_result += f'{caretaker}\n'

        workers_result += f'----- {len(vets)} Vets:\n'
        if vets:
            for vet in vets:
                if vets.index(vet) == len(vets) - 1:
                    workers_result += f"{vet}"
                else:
                    workers_result += f"{vet}\n"
        return workers_result


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
