from Guitarra import Guitarra

class TestGuitarra:
    def __init__(self):
        self.guit = Guitarra()

    def test(self):
        assert self.guit.getNota() == "No hay nota definida"
        assert self.guit.setDedo(12, 19) == False
        assert self.guit.setDedo(5, 0) == True
        assert self.guit.getNota() == "La"

testGuitarra = TestGuitarra()
testGuitarra.test()

