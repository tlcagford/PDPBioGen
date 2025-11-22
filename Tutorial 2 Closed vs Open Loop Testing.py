# tutorial_2_loop_testing.py
from quantum_healing import HeartHealingTestFramework

# Initialize test framework
test_framework = HeartHealingTestFramework()

# Run comparative analysis
closed_data, open_data = test_framework.download_heart_test_data()
metrics = test_framework.run_comparative_analysis()

# Display results
test_framework.generate_test_report()