from .trip import Trip

class NationalPark:

    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        

    def getname(self):
        return self._name
        
    def setname(self, name):
         if isinstance(name, str) and not hasattr(self, "_name"):
             self._name = name
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = {}
        for trip in self.trips():
            visitor = trip.visitor
            if visitor in visitors:
                visitors[visitor] += 1
            else:
                visitors[visitor] = 1

        best_visitor = max(visitors, key=visitors.get)
        return best_visitor


    name = property(getname, setname)