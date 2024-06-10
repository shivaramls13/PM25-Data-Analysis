from datetime import datetime
from config import PM25_THRESHOLD


def analyze_data(rows):
    """
    Analyze the data to find danger periods and calculate daily statistics.

    Args:
        rows: List of tuples containing device_id, timestamp, and pm25 values.

    Returns:
        A tuple containing:
        - A list of danger periods where PM2.5 level exceeds the threshold.
        - A list of daily statistics including max, min, and average PM2.5 levels.
    """
    danger_periods = []
    daily_stats = {}

    for row in rows:
        device_id, timestamp, pm25 = row
        date_str = timestamp.split('T')[0]
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

        # Record periods where PM2.5 exceeds the threshold
        if pm25 > PM25_THRESHOLD:
            danger_periods.append((timestamp, pm25))
        # Calculate daily statistics
        if date_obj not in daily_stats:
            daily_stats[date_obj] = {'max': pm25, 'min': pm25, 'sum': pm25, 'count': 1}
        else:
            daily_stats[date_obj]['max'] = max(daily_stats[date_obj]['max'], pm25)
            daily_stats[date_obj]['min'] = min(daily_stats[date_obj]['min'], pm25)
            daily_stats[date_obj]['sum'] += pm25
            daily_stats[date_obj]['count'] += 1

    # Generate a daily report
    daily_report = []
    for date, stats in daily_stats.items():
        daily_report.append({
            'date': date,
            'max': stats['max'],
            'min': stats['min'],
            'avg': stats['sum'] / stats['count']
        })

    return danger_periods, daily_report
