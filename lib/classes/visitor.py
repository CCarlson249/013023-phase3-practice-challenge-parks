from .trip import Trip

class Visitor:

    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name =name
    
    def getname(self):
        return self._name
    
    def setname(self, name):
        if not hasattr(self, "_name") and isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
    
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def nationalparks(self):
        return list(set([trip.national_park for trip in self.trips()]))

    name = property(getname, setname)