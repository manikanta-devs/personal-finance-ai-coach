import streamlit as st

class FinancialCoach:
    def __init__(self):
        # Initialize the financial coach features
        self.budget = {}  # to track budget
        self.expenses = []  # to track expenses

    def add_budget(self, category, amount):
        self.budget[category] = amount
        st.success(f"Added budget for {category}: ${amount}")

    def add_expense(self, amount, category):
        self.expenses.append((amount, category))
        st.success(f"Added expense: ${amount} in {category}")

    def budget_overview(self):
        st.write("### Budget Overview")
        for category, amount in self.budget.items():
            st.write(f"{category}: ${amount}")

    def expense_summary(self):
        st.write("### Expense Summary")
        total = sum(exp[0] for exp in self.expenses)
        st.write(f"Total Expenses: ${total}")
        for exp in self.expenses:
            st.write(f"Expense: ${exp[0]} in {exp[1]}")

    def financial_insights(self):
        # AI-powered insights can be added here
        st.write("### Financial Insights")
        # Simple insights based on expenses can be added here
        for exp in self.expenses:
            st.write(f"Consider revising your spending of ${exp[0]} in {exp[1]}")

# Create a Streamlit application
if __name__ == '__main__':
    st.title('Personal Finance AI Coach')
    coach = FinancialCoach()
    st.sidebar.header('Budget Management')
    category = st.sidebar.text_input('Category')
    budget_amount = st.sidebar.number_input('Budget Amount', min_value=0)
    if st.sidebar.button('Add Budget'):
        coach.add_budget(category, budget_amount)

    st.sidebar.header('Expense Management')
    expense_amount = st.sidebar.number_input('Expense Amount', min_value=0)
    if st.sidebar.button('Add Expense'):
        coach.add_expense(expense_amount, category)

    # Display budget and expense reports
    coach.budget_overview()
    coach.expense_summary()
    coach.financial_insights()