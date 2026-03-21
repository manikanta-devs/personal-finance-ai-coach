class FinancialCoach:
    def __init__(self, user_data):
        self.user_data = user_data

    def evaluate_budget(self):
        # Analyze the user's budget and provide feedback
        budget = self.user_data.get('budget', {})
        total_income = sum(budget.get('income', []))
        total_expenses = sum(budget.get('expenses', []))
        balance = total_income - total_expenses

        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'balance': balance,
            'advice': self.budget_advice(balance)
        }

    def budget_advice(self, balance):
        if balance > 0:
            return "Great job! You're saving money. Consider investing."
        elif balance == 0:
            return "You're breaking even. Look for areas to cut back on spending."
        else:
            return "You're in deficit. Create a stricter budget plan."

    def savings_goals(self, target_amount, months):
        monthly_savings_required = target_amount / months
        return monthly_savings_required

    def investment_advice(self, risk_tolerance):
        if risk_tolerance == 'high':
            return "Consider stocks or mutual funds."
        elif risk_tolerance == 'medium':
            return "Look into balanced funds."
        else:
            return "Focus on safer investments like bonds or savings accounts."