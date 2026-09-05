from monitor import get_status



def test_normal_status():
    assert get_status(50) == "NORMAL"


def test_warning_status():
    assert get_status(75) == "WARNING"

def test_critical_status():
    assert get_status(95) == "CRITICAL"

