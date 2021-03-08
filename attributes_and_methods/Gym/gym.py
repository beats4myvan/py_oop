# from attributes_and_methods.project.equipment import Equipment
# from attributes_and_methods.project.exercise_plan import ExercisePlan
# from attributes_and_methods.project.subscription import Subscription
# from attributes_and_methods.project.trainer import Trainer
# from attributes_and_methods.project.customer import Customer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ''
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                current_subscription = subscription
                result += f"{current_subscription.__repr__()}\n"
                customer_id = current_subscription.customer_id
                trainer_id = current_subscription.trainer_id
                exercise_id = current_subscription.exercise_id
                for customer in self.customers:
                    if customer.id == customer_id:
                        result += f"{customer.__repr__()}\n"
                for trainer in self.trainers:
                    if trainer.id == trainer_id:
                        result += f"{trainer.__repr__()}\n"
                for exercise in self.plans:
                    if exercise.id == exercise_id:
                        current_exercise = exercise
                        equipment_id = current_exercise.equipment_id
                        for equipment in self.equipment:
                            if equipment.id == equipment_id:
                                result += f"{equipment.__repr__()}\n"
                        result += f"{current_exercise.__repr__()}"
        return result




# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
