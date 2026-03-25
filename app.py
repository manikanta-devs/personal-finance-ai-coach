import json
from datetime import date
from utils.age_calculator import calculate_age, years_to_retirement, retirement_date

class FinancialDashboard:
    def __init__(self, storage_file='data.json'):
        self.storage_file = storage_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {'expenses': [], 'budgets': [], 'savings_goals': []}

    def save_data(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_expense(self, description, amount):
        self.data['expenses'].append({'description': description, 'amount': amount})
        self.save_data()

    def set_budget(self, category, amount):
        self.data['budgets'].append({'category': category, 'amount': amount})
        self.save_data()

    def add_savings_goal(self, goal_name, target_amount):
        self.data['savings_goals'].append({'goal_name': goal_name, 'target_amount': target_amount})
        self.save_data()

    def get_expenses(self):
        return self.data['expenses']

    def get_budgets(self):
        return self.data['budgets']

    def get_savings_goals(self):
        return self.data['savings_goals']

    def get_total_expenses(self):
        return sum(exp['amount'] for exp in self.data['expenses'])

    def get_budget_summary(self):
        return {budget['category']: budget['amount'] for budget in self.data['budgets']}

    def get_savings_goal_summary(self):
        return {goal['goal_name']: goal['target_amount'] for goal in self.data['savings_goals']}

    def get_age_summary(self, date_of_birth, retirement_age=65):
        """
        Return an age-based financial planning summary.

        Parameters:
        date_of_birth (date): The user's date of birth.
        retirement_age (int): The target retirement age (default is 65).

        Returns:
        dict: A summary containing current age, years to retirement, and retirement date.
        """
        return {
            'current_age': calculate_age(date_of_birth),
            'years_to_retirement': years_to_retirement(date_of_birth, retirement_age),
            'retirement_date': retirement_date(date_of_birth, retirement_age).isoformat(),
        }

# Example usage:
if __name__ == '__main__':
    dashboard = FinancialDashboard()
    dashboard.add_expense('Groceries', 50.00)
    dashboard.set_budget('Food', 200.00)
    dashboard.add_savings_goal('Vacation', 1500.00)
    print('Total Expenses:', dashboard.get_total_expenses())
    print('Budgets:', dashboard.get_budget_summary())
    print('Savings Goals:', dashboard.get_savings_goal_summary())
    dob = date(1990, 6, 15)
    print('Age Summary:', dashboard.get_age_summary(dob))
