def grammar_check(sentense):
    try: 
        sentence.endswith(".")
        sentence[0].isupper()
    except NotCapitalizedError:
        return NotCapitalizedError
        
    except NoFullStopError:
        return NoFullStopError


def test_grammar_check():
    import pytest
    assert grammar_check("I am fine.")
    with pytest.raises(NotCapitalizedError):
        grammar_check("i am not fine.")
    with pytest.raises(NotCapitalizedError):
        grammar_check("i am not fine either")
    with pytest.raises(NoFullStopError):
        grammar_check("I forgot to end the sentence") 

test_grammar_check()
