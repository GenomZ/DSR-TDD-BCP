from datetime import datetime, timedelta
import pytest
from SOLUTIONS.water_meter import record_telegrams  # Import your record_telegrams function


@pytest.mark.parametrize("duration_minutes", [1800])
def test_static_telegrams_status(duration_minutes):
    telegrams = record_telegrams(duration_minutes)

    # Check if all static telegrams have status "OK"
    for telegram in telegrams:
        if "Static telegram" in telegram:
            assert "STATUS: OK" in telegram


@pytest.mark.parametrize("duration_minutes", [60])  # Test for 600 minutes
def test_mobile_telegrams_distance(duration_minutes):
    telegrams = record_telegrams(duration_minutes)
    mobile_times = []

    # Extract timestamps of mobile telegrams
    for telegram in telegrams:
        if "Mobile telegram" in telegram:
            timestamp_str = telegram.split(" at ")[1].split(" Volume:")[0]

            mobile_time = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            mobile_times.append(mobile_time)

    # Check distance between mobile telegrams
    for i in range(1, len(mobile_times)):
        time_difference = mobile_times[i] - mobile_times[i-1]
        maximum_difference = timedelta(minutes=1.1)
        minimum_difference = timedelta(minutes=0.9)
        assert minimum_difference <= time_difference <= maximum_difference


@pytest.mark.parametrize("duration_minutes, volume_increase_per_min", [(60, 10)])  # Test for 600 minutes
def test_volume_accu(duration_minutes, volume_increase_per_min):
    telegrams = record_telegrams(duration_minutes)
    volume = 0

    # Check if volume increases by volume_increase_per_min at every mobile telegram
    for telegram in telegrams:
        if "Mobile telegram" in telegram:
            volume_str = telegram.split("Volume: ")[1]
            current_volume = float(volume_str)
            assert current_volume == round(volume + volume_increase_per_min, 1)
            volume = current_volume


@pytest.mark.parametrize("duration_minutes", [600])  # Test for 600 minutes
def test_static_telegrams_count(duration_minutes):
    telegrams = record_telegrams(duration_minutes)
    static_telegrams_count = sum(1 for telegram in telegrams if "Static telegram" in telegram)
    hours = duration_minutes // 60  # Calculate number of hours

    # Check if there are exactly as many static telegrams as hours of the test
    assert static_telegrams_count == hours


@pytest.mark.parametrize("duration_minutes", [1200])  # Test for 600 minutes
def test_mobile_telegrams_count(duration_minutes):
    telegrams = record_telegrams(duration_minutes)

    # Count the number of mobile telegrams
    mobile_telegrams_count = sum(1 for telegram in telegrams if "Mobile telegram" in telegram)

    # Calculate the expected number of mobile telegrams
    expected_telegrams_count = duration_minutes

    # Check if the count of mobile telegrams matches the expected count
    assert mobile_telegrams_count == expected_telegrams_count