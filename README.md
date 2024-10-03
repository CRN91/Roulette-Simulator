# Roulette Simulator

<img src="rmimg/Personal.svg" height="28"> <img src="rmimg/Solo.svg" height="28">

A program that simulates many instances of a game of roulette and various betting strategies on it and compiles the results to measure the effectiveness of each betting strategy. A seemingly counter-intuitive endevour, but here it is.

## Usage

Requires Python 3.x

In the main entrance point of `Roulette.py` you can set `thePlayer` variable to an instance of any the inbuilt 'Player' classes or create your own betting strategy by creating a class that inherits the `Player` class.

```Python
if __name__ == "__main__":
    builder = BinBuilder()
    theWheel = Wheel()
    builder.buildBins(theWheel)
    theTable = Table()
    theGame = Game(theWheel,theTable)
    thePlayer = Passenger57(theTable,theWheel)
    sim = Simulator(theGame, thePlayer)
    sim.gather()
```

## About

In sixth form I was recommended a book by my computer science teacher Mr Coppen to learn Object Orientated Programming before starting the A level coursework. I worked on it substantially, it taught me a lot about OOP, but I never finished it. The book was Building Skills in Object-Oriented Design by Steven F. Lott. In this git repo I'd like to finish and fix the program I'd like to fix the program and maybe mess around with it a bit.
