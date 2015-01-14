class Tracker:

    def __init__(self):
        self.past = []

    def add(self, guess):
        if not self.past or guess != self.past[-1]:
            self.past.append(guess)

    def count(self):
        return len(self.past)

def assess(n, guess):
    return  (False, 'Too low')  if guess < n else \
            (False, 'Too high') if guess > n else \
            (True, 'YAY')

def game(n):
    tracker = Tracker()
    done = False
    while not done:
        guess = int(input('Enter a number: '))
        tracker.add(guess)
        done, why = assess(n, guess)
        print(why)
    return tracker.count()

if __name__ == '__main__':
    import sys
    if '--test' in sys.argv or '-t' in sys.argv:
        assert(assess(17, 10) == (False, 'Too low'))
        assert(assess(17, 20) == (False, 'Too high'))
        assert(assess(17, 17) == (True, 'YAY'))
    else:
        print(game(17))
