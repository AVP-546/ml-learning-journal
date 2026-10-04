# ML Learning Journal

A running record of what I am studying, when, and how, as preparation for **"Scaling Piecewise Deterministic Generative Models to Medical Image Synthesis"** research project at [INESC TEC](https://www.inesctec.pt/).

Two tracks run in parallel:

- **Python** — a hands-on tutorial to get fluent in the language (notes often compare Python with C++, my first language). [Youtube Python Tutorial - Bro Code](https://www.youtube.com/watch?v=ix9cRaBkVe0&t=6760s)
- **Machine Learning** — the Machine Learning Specialization on Coursera (DeepLearning.AI / Stanford, Andrew Ng).

The day-by-day record is in **[LOG.md](LOG.md)**.

## Repository structure

```
.
├── LOG.md                    # dated journal: what, when, how
├── python/
│   ├── basics/               # one script per concept from the tutorial
│   ├── exercises/            # small programs applying the concepts
│   └── notes/                # short written notes (Python vs C++)
└── ml-specialization/
    └── course-1-supervised-learning/   # notes per week
```

## Progress

### Python

| Topic | Files |
| --- | --- |
| Syntax, variables, f-strings | [helloworld.py](python/basics/helloworld.py) |
| Typecasting | [typecasting.py](python/basics/typecasting.py) |
| User input | [input.py](python/basics/input.py) |
| Arithmetic and the `math` module | [m.py](python/basics/m.py), [mathOper.md](python/notes/mathOper.md) |
| If statements | [temp.py](python/basics/temp.py) |
| Logical operators | [logic.md](python/notes/logic.md) |
| Conditional expressions | [conditional_exp.py](python/basics/conditional_exp.py) |

Exercises: [rectangle area](python/exercises/Ex1RecArea.py) · [shopping cart](python/exercises/Ex2ShoppingCart.py) · [madlibs](python/exercises/Ex3madlibs.py) · [circle and sphere](python/exercises/Ex4Circle.py) · [Pythagorean theorem](python/exercises/Ex5PT.py)

### Machine Learning Specialization

| Course | Status | Notes |
| --- | --- | --- |
| 1. Supervised Machine Learning: Regression and Classification | In progress | [Week 1](ml-specialization/course-1-supervised-learning/week-1-introduction.md) |
| 2. Advanced Learning Algorithms | Not started | |
| 3. Unsupervised Learning, Recommenders, Reinforcement Learning | Not started | |

## Running the code

The Python scripts only use the standard library (Python 3):

```bash
python3 python/exercises/Ex1RecArea.py
```

## Author

Afonso Pires — [@AVP-546](https://github.com/AVP-546)
