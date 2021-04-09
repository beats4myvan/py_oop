def get_consumers_total_cost(self):
        children_results = ['--- Child {i + 1} monthly cost: {child.get_monthly_expense():.2f}$' for (i, child) in enumerate(self.children)  
        return [
            *children_results,
            f'--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in self.appliances):.2f}$',
        ]