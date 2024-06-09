def generate_report(danger_periods, daily_report):
    report = []
    report.append("Danger Periods (PM2.5 > 30):")
    for period in danger_periods:
        report.append(f"Time: {period[0]}, PM2.5: {period[1]}")

    report.append("\nDaily Report:")
    for report_item in daily_report:
        report.append(
            f"Date: {report_item['date']}, Max: {report_item['max']}, Min: {report_item['min']}, Avg: {report_item['avg']}")

    return "\n".join(report)
