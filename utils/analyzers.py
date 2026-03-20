# Financial Analysis Utility Functions

def calculate_roi(investment, return_on_investment):
    """
    Calculate the Return on Investment (ROI).
    
    Parameters:
    investment (float): The total investment amount.
    return_on_investment (float): The total return from the investment.
    
    Returns:
    float: The ROI expressed as a percentage.
    """
    return ((return_on_investment - investment) / investment) * 100


def budget_variance(actual_budget, planned_budget):
    """
    Calculate the budget variance.
    
    Parameters:
    actual_budget (float): The actual amount spent.
    planned_budget (float): The budgeted amount.
    
    Returns:
    float: The difference between actual and planned budget.
    """
    return actual_budget - planned_budget


def savings_rate(monthly_income, monthly_savings):
    """
    Calculate the savings rate.
    
    Parameters:
    monthly_income (float): The total income for the month.
    monthly_savings (float): The total savings for the month.
    
    Returns:
    float: The savings rate as a percentage of income.
    """
    return (monthly_savings / monthly_income) * 100


def debt_to_income_ratio(total_debt, monthly_income):
    """
    Calculate the debt-to-income ratio.
    
    Parameters:
    total_debt (float): The total amount of debt.
    monthly_income (float): The total income for the month.
    
    Returns:
    float: The debt-to-income ratio as a percentage.
    """
    return (total_debt / monthly_income) * 100
