import unittest
import game.startgame as g
import game.constants as c
import game.starkiller as s
import pygame

class TestGameMenu(unittest.TestCase):
    def setUp(self):
        print("Se inicia el test")
        self.clock = 0
        c.MENU_AUD = "menu_estrella.mp3"
        c.STATE = "PRUEBA"
        c.MENU_IMG = "menu_estrella.png"
    def tearDown(self):
        print("Se termina el test")
    def test_game_menu(self):
        game = g.game_menu(self.clock)
        self.assertNotEqual(game, "No existe el estado", "test_game_menu incorrecto")