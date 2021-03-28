from django.test import TestCase
from Lumen.Apps.GestionBotes.models import Botes, Fotos 
# Create your tests here.
class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Botes.object.create(Equipo="Banesto", Pais="ESPAÑA")
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
    

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        bote=Botes.objects.get(id=1)
        EtiquetadeCampo=bote._meta.get_field('Equipo').verbose_name
        print("Method: test_false_is_false.")
        self.assertFalse(EtiquetadeCampo!='Equipo')

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)