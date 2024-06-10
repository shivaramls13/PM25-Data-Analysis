def generate_report(danger_periods, daily_report):
    """
    Generate a textual report from the analyzed data.

    Args:
        danger_periods: List of periods where PM2.5 levels exceeded the threshold.
        daily_report: List of dictionaries containing daily max, min, and average PM2.5 levels.

    Returns:
        A string containing the formatted report.
    """
    report = []

    # Add danger periods to the report
    report.append("Danger Periods (PM2.5 > 30):")
    for period in danger_periods:
        report.append(f"Time: {period[0]}, PM2.5: {period[1]}")

    # Add daily statistics to the report
    report.append("\nDaily Report:")
    for report_item in daily_report:
        report.append(
            f"Date: {report_item['date']}, Max: {report_item['max']}, Min: {report_item['min']}, Avg: {report_item['avg']}")

    return "\n".join(report)
