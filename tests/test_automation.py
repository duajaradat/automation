from automation import __version__
from automation.filter import email , main_fun, write_file,phone_num


def test_version():
    assert __version__ == '0.1.0'

def test_phone_numbers():
    text ="Sister follow wide report land find.861-26-5898Especially can south wall need.+1-178-383-0937x54779He final hour painting nature people never rise. Home decide ever kind together dinner."

    expected = ["+11783830937x54779" ,"861265898"]
    actual = phone_num(text)

    assert actual == expected