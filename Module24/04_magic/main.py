# Water + Air = Storm
# Water + Fire = Steam
# Water + Earth = Dirt
# Air + Fire = Lightning
# Air + Earth = Dust
# Fire + Earth = Lava

class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return 'Storm'
        elif isinstance(other, Fire):
            return 'Steam'
        elif isinstance(other, Earth):
            return 'Dirt'
        elif isinstance(other, Gravity):
            return 'Waterfall'
        else:
            return None

    def __radd__(self, other):
        return self + other


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return 'Storm'
        elif isinstance(other, Fire):
            return 'Lightning'
        elif isinstance(other, Earth):
            return 'Dust'
        elif isinstance(other, Gravity):
            return 'Push'
        else:
            return None

    def __radd__(self, other):
        return self + other


class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return 'Steam'
        elif isinstance(other, Air):
            return 'Lightning'
        elif isinstance(other, Earth):
            return 'Lava'
        elif isinstance(other, Gravity):
            return 'Firewall'
        else:
            return None

    def __radd__(self, other):
        return self + other


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return 'Dirt'
        elif isinstance(other, Air):
            return 'Dust'
        elif isinstance(other, Fire):
            return 'Lava'
        elif isinstance(other, Gravity):
            return 'Earthquake'
        else:
            return None

    def __radd__(self, other):
        return self + other


class Gravity:
    def __add__(self, other):
        if isinstance(other, Water):
            return 'Waterfall'
        elif isinstance(other, Air):
            return 'Push'
        elif isinstance(other, Fire):
            return 'Firewall'
        elif isinstance(other, Earth):
            return 'Earthquake'
        else:
            return None

    def __radd__(self, other):
        return self + other


element_1 = Gravity()
element_2 = Fire()

print(element_1 + element_2)


