import json
import streamlit as st
import pandas as pd

from utils.budget_analyzer import analyze_spending, calculate_financial_ratios, generate_recommendations
from utils.visualizations import plot_bar_chart, plot_pie_chart
from utils.financial_coach import FinancialCoach


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


DEFAULT_MONTHLY_INCOME = 5000.0


def run_streamlit_app():
    st.set_page_config(page_title='Personal Finance AI Coach', page_icon='💰', layout='wide')
    st.title('💰 Personal Finance AI Coach')
    st.markdown('Track your expenses, set budgets, and achieve your savings goals.')

    dashboard = FinancialDashboard()

    tab_overview, tab_expenses, tab_budget, tab_goals, tab_advice = st.tabs(
        ['📊 Overview', '💸 Expenses', '📋 Budgets', '🎯 Savings Goals', '🤖 AI Advice']
    )

    with tab_overview:
        st.header('Financial Overview')
        total_expenses = dashboard.get_total_expenses()
        budgets = dashboard.get_budget_summary()
        goals = dashboard.get_savings_goal_summary()

        col1, col2, col3 = st.columns(3)
        col1.metric('Total Expenses', f'${total_expenses:,.2f}')
        col2.metric('Budget Categories', len(budgets))
        col3.metric('Savings Goals', len(goals))

        expenses = dashboard.get_expenses()
        if expenses:
            spending_analysis = analyze_spending(expenses)
            st.subheader('Spending by Category')
            fig = plot_pie_chart(spending_analysis['by_category'], 'Expense Breakdown')
            st.plotly_chart(fig, use_container_width=True)

        if budgets:
            st.subheader('Budget Allocation')
            fig = plot_bar_chart(budgets, 'Budget by Category', 'Category', 'Amount ($)')
            st.plotly_chart(fig, use_container_width=True)

    with tab_expenses:
        st.header('Track Expenses')
        with st.form('add_expense_form'):
            col1, col2 = st.columns(2)
            description = col1.text_input('Description', placeholder='e.g., Groceries')
            amount = col2.number_input('Amount ($)', min_value=0.01, step=0.01)
            if st.form_submit_button('Add Expense'):
                if description:
                    dashboard.add_expense(description, amount)
                    st.success(f'Added expense: {description} - ${amount:.2f}')
                    st.rerun()
                else:
                    st.error('Please enter a description.')

        expenses = dashboard.get_expenses()
        if expenses:
            st.subheader('Expense History')
            df = pd.DataFrame(expenses)
            df.columns = ['Description', 'Amount ($)']
            st.dataframe(df, use_container_width=True)
        else:
            st.info('No expenses recorded yet. Add your first expense above.')

    with tab_budget:
        st.header('Set Budgets')
        with st.form('set_budget_form'):
            col1, col2 = st.columns(2)
            category = col1.text_input('Category', placeholder='e.g., Food')
            budget_amount = col2.number_input('Budget Amount ($)', min_value=0.01, step=0.01)
            if st.form_submit_button('Set Budget'):
                if category:
                    dashboard.set_budget(category, budget_amount)
                    st.success(f'Budget set: {category} - ${budget_amount:.2f}')
                    st.rerun()
                else:
                    st.error('Please enter a category.')

        budgets = dashboard.get_budgets()
        if budgets:
            st.subheader('Current Budgets')
            df = pd.DataFrame(budgets)
            df.columns = ['Category', 'Amount ($)']
            st.dataframe(df, use_container_width=True)
        else:
            st.info('No budgets set yet. Add your first budget above.')

    with tab_goals:
        st.header('Savings Goals')
        with st.form('add_goal_form'):
            col1, col2 = st.columns(2)
            goal_name = col1.text_input('Goal Name', placeholder='e.g., Vacation')
            target_amount = col2.number_input('Target Amount ($)', min_value=0.01, step=0.01)
            if st.form_submit_button('Add Goal'):
                if goal_name:
                    dashboard.add_savings_goal(goal_name, target_amount)
                    st.success(f'Goal added: {goal_name} - ${target_amount:.2f}')
                    st.rerun()
                else:
                    st.error('Please enter a goal name.')

        goals = dashboard.get_savings_goals()
        if goals:
            st.subheader('Your Savings Goals')
            df = pd.DataFrame(goals)
            df.columns = ['Goal', 'Target Amount ($)']
            st.dataframe(df, use_container_width=True)

            fig = plot_bar_chart(
                {g['goal_name']: g['target_amount'] for g in goals},
                'Savings Goals',
                'Goal',
                'Target Amount ($)',
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info('No savings goals set yet. Add your first goal above.')

    with tab_advice:
        st.header('AI Financial Advice')
        expenses = dashboard.get_expenses()
        total_expenses = dashboard.get_total_expenses()

        st.subheader('Spending Recommendations')
        recommendations = generate_recommendations(expenses)
        for rec in recommendations:
            st.info(rec)

        st.subheader('Budget Analysis')
        col1, col2 = st.columns(2)
        income = col1.number_input('Enter your monthly income ($)', min_value=0.0, step=100.0, value=DEFAULT_MONTHLY_INCOME)
        risk_tolerance = col2.selectbox('Risk Tolerance', ['low', 'medium', 'high'])

        if income > 0:
            ratios = calculate_financial_ratios(income, total_expenses)
            if ratios:
                col1, col2, col3 = st.columns(3)
                col1.metric('Monthly Savings', f'${ratios["savings"]:,.2f}')
                col2.metric('Savings Rate', f'{ratios["savings_rate"]}%')
                col3.metric('Expense Ratio', f'{ratios["expense_ratio"]}%')

            user_data = {
                'budget': {
                    'income': [income],
                    'expenses': [total_expenses],
                }
            }
            coach = FinancialCoach(user_data)
            evaluation = coach.evaluate_budget()
            st.info(f'💡 {evaluation["advice"]}')

            st.subheader('Investment Advice')
            advice = coach.investment_advice(risk_tolerance)
            st.success(f'📈 {advice}')


if __name__ == '__main__':
    run_streamlit_app()
