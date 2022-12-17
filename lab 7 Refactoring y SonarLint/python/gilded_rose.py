# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self): 
        self.sell_in -= 1
        if 0 <= self.quality < 50: 
            if self.sell_in < 0: 
                self.quality -= 2
            else: 
                self.quality -= 1
        
        if self.quality < 0: 
            self.quality = 0
    
class Brie(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in >=0 and self.quality < 50:
            self.quality += 1
        elif self.quality < 50:
            self.quality += 2

        if self.quality > 50: 
            self.quality = 50


class Sulfuras(Item):
    def update_quality(self):
        # do nothin
        pass

class Conjured(Item):
    def update_quality(self):
        self.sell_in -= 1
        if 0 < self.quality < 50: 
            if self.sell_in < 0: 
                self.quality -= 4
            else: 
                self.quality -= 2

        if self.quality < 0: 
            self.quality = 0


class Backstage(Item):
    def update_quality(self):
        self.sell_in -= 1
        if 6 <= self.sell_in <= 10:
            self.quality += 2
        elif 0 <= self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in < 0:
            self.quality = 0
        else:
            self.quality += 1
        
        if self.quality > 50: 
            self.quality = 50