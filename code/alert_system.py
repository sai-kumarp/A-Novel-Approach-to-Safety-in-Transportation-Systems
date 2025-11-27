def check_alerts(df):
    """Check for hazard alerts"""

    alerts = df[df["hazard"] == True]

    if len(alerts) == 0:
        print("✔ No hazards detected, all safe.")
    else:
        print("⚠ Hazards Detected:")
        for index, row in alerts.iterrows():
            print(
                f"Vehicle ID: {row['vehicle_id']} | "
                f"Speed: {row['speed']} | "
                f"Temperature: {row['temperature']} → ALERT"
            )
