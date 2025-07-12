This Python utility converts telemetry data from two distinct formats into a unified structure using millisecond timestamps. The data is validated through automated tests to ensure format consistency and timestamp accuracy.
 What It Does
- Converts ISO timestamps to milliseconds.
- Flattens nested fields such as "device" and groups "location" fields.
- Handles missing or malformed values gracefully.
- Outputs unified telemetry objects that match data-result.json.

📦 How to Run
python main.py


This runs all unit tests and validates your conversion logic. If successful, you’ll see:
OK



🧪 Testing
- Format Type 1: Simplified ISO timestamp format.
- Format Type 2: Detailed telemetry with nested metadata.
- Both formats are tested against a golden result stored in data-result.json.

💡 Future Ideas
- Expand to handle arrays of telemetry events.
- Add real-time ingestion via APIs or streams.
- Visualize data in a dashboard (e.g. Streamlit, Fabric).
- Deploy as a microservice or CLI tool.

