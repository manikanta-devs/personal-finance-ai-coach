HIGH_SPENDING_THRESHOLD = 3000
CATEGORY_SPENDING_THRESHOLD = 0.4


def analyze_spending(data):
    '''Analyzes spending patterns based on input data.'''
    if not data:
        return {}
    total = sum(item['amount'] for item in data)
    by_category = {}
    for item in data:
        category = item.get('description', 'Other')
        by_category[category] = by_category.get(category, 0) + item['amount']
    return {
        'total': total,
        'by_category': by_category,
        'count': len(data),
    }


def calculate_financial_ratios(income, expenses):
    '''Calculates financial ratios like savings rate and debt-to-income ratio.'''
    if income <= 0:
        return {}
    savings = income - expenses
    savings_rate = (savings / income) * 100
    expense_ratio = (expenses / income) * 100
    return {
        'savings': savings,
        'savings_rate': round(savings_rate, 2),
        'expense_ratio': round(expense_ratio, 2),
    }


def generate_recommendations(spending_data):
    '''Generates recommendations for better financial management based on spending patterns.'''
    recommendations = []
    if not spending_data:
        recommendations.append('Start tracking your expenses to get personalized recommendations.')
        return recommendations
    total = sum(item['amount'] for item in spending_data)
    if total > HIGH_SPENDING_THRESHOLD:
        recommendations.append('Your total spending is high. Consider reviewing discretionary expenses.')
    by_category = {}
    for item in spending_data:
        cat = item.get('description', 'Other')
        by_category[cat] = by_category.get(cat, 0) + item['amount']
    for category, amount in by_category.items():
        if total > 0 and (amount / total) > CATEGORY_SPENDING_THRESHOLD:
            recommendations.append(
                f'"{category}" accounts for over 40% of your spending. Look for ways to reduce it.'
            )
    if not recommendations:
        recommendations.append('Your spending looks balanced. Keep it up!')
    return recommendations