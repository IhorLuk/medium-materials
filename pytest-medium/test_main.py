from main import func

def test_func():
    assert "Start program" == func()
    
def test_fail_func():
    assert "Fail start" == func()