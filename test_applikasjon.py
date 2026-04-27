import pytest 

from applikasjon import BigLetter

def test_BigLetter():
    assert BigLetter("Jeg") == "JEG"
    assert BigLetter("mEg") == "MEG"
    assert BigLetter("deg") == "DEG"
    assert BigLetter("") == ""
    


def test_addisjon_feil_input(): 
    with pytest.raises(TypeError): 
        BigLetter(123)