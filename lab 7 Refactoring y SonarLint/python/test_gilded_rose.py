# -*- coding: utf-8 -*-
import unittest
import sys
import gilded_rose as gr
CONSTANT_CONCIERT_NAME = "Backstage passes to a TAFKAL80ETC concert"
CONSTANT_SULFURAS = "Sulfuras, Hand of Ragnaros"
CONSTANT_BRIED = "Aged Brie"
CONSTANT_CONJURED = "Conjured Mana Cake"

class GildedRoseTest(unittest.TestCase):
    days = 6
    def test_foo(self):
        items = [gr.Item("foo", 0, 0)]
        gilded_rose = gr.GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_items(self):
        items = [
             gr.Brie(CONSTANT_BRIED, sell_in=3, quality=48),
             gr.Item(name="Elixir of the Mongoose", sell_in=3, quality=5),
             gr.Sulfuras(CONSTANT_SULFURAS, sell_in=3, quality=5),
             gr.Backstage(CONSTANT_CONCIERT_NAME, sell_in=3, quality=48),
             gr.Conjured(CONSTANT_CONJURED, sell_in=3, quality=5),  # <-- :O
            ]
        if len(sys.argv) > 1:
            self.days = int(sys.argv[1]) + 1
        for day in range(self.days):
            print("-------- day %s --------" % day)
            print("name, sellIn, quality")
            for item in items:
                print(item)
                if item.sell_in < 0:
                    self.assertIsNotNone(item.quality==0 or item.quality==50, "cumple")
            print("")
            gr.GildedRose(items).update_quality()
        
if __name__ == '__main__':
    unittest.main()
