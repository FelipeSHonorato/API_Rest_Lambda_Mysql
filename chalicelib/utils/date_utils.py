from datetime import datetime, date

# Formula para formatação de data de exibição
def format_date(date_value):
    if isinstance(date_value, date):
        return date_value.strftime('%d/%m/%Y')
    try:
        return datetime.strptime(date_value, '%Y-%m-%d').strftime('%d/%m/%Y')
    except (ValueError, TypeError):
        return "Data inválida"