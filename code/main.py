from data_processing import load_data, clean_data, analyze_data
from alert_system import check_alerts


def main():
    print("🚦 Transportation Safety Monitoring System Started")

    # Step 1: Load data
    data = load_data("transport_data.csv")
    print("📥 Data Loaded")

    # Step 2: Clean data
    cleaned = clean_data(data)
    print("🧹 Data Cleaned")

    # Step 3: Analyze data
    results = analyze_data(cleaned)
    print("📊 Analysis Completed")

    # Step 4: Check alerts
    check_alerts(results)
    print("⚠️ Alert Checking Completed")

    print("✅ System Completed Successfully")


if __name__ == "__main__":
    main()
