from multi_bracket_validation import __version__
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_version():
    assert __version__ == '0.1.0'

def test_will_return_true_when_brackets_are_matched():
    expected = True
    actual = multi_bracket_validation('()')
    assert expected == actual

def test_will_return_true_when_multiple_brackets_are_matched():
    expected = True
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    assert expected == actual

def test_will_return_false_when_brackets_are_not_matched():
    expected = False
    actual = multi_bracket_validation('(](')
    assert expected == actual

def test_will_return_true_when_input_is_empty():
    expected = True
    actual = multi_bracket_validation('')
    assert expected == actual 

def test_will_return_true_when_input_has_no_brackets():
    expected = True
    actual = multi_bracket_validation('This has no brackets')
    assert expected == actual 

def test_will_return_false_when_brackets_are_out_of_order():
    expected = False
    actual = multi_bracket_validation('{ ( } )')
    assert expected == actual