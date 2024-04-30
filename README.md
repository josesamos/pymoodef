
<!-- README.md is generated from README.Rmd. Please edit that file -->

# pymoodef

The goal of the `pymoodef` package is to support the definition of
[*Moodle*](https://moodle.org/) questions to be included in the question
bank to define quizzes.

To define the questions for the quizzes we can use the component for
this purpose that includes *Moodle*, based on entering data through
screens. It allows the import and export of questions in various
formats, including xml.

Complementary, using the `pymoodef` package, we can define
questionnaires from python. We have generalized 9 types of questions and
simplified their definition. So, we define a question by including a row
in a csv file or an *Excel* file. The result is an xml file that we
import into *Moodle*. If necessary, some parameter not considered in the
generalization can be defined or adjusted there.

In each question we can include an image that is embedded in xml. We can
set up the size of the images so that they are homogeneous when
displayed in quizzes.

## Installation

``` bash
$ pip install pymoodef
```

## Usage

`pymoodef` can be used to generate *Moodle* question xml files from csv
or *Excel* files:

``` bash
$ python -m pymoodef tests/questions.xlsx result.xml
```

If the name of the result file is not indicated, one is created with the
same name as the input file but with an xml extension in the folder that
contains it.

``` bash
$ python -m pymoodef tests/questions.csv 
```

By default, csv files with columns separated by “,” are considered. In
case of using “;” as a separator, simply add a “2” after the file name,
as shown below for file `tests/questions1.csv`.

``` bash
$ python -m pymoodef tests/questions1.csv2
```

Below is the content of one of the question files used.

| type | question                                                                       | image      | image_alt  | answer                                              | a_1                       | a_2                                                              | a_3         |
|------|--------------------------------------------------------------------------------|------------|------------|-----------------------------------------------------|---------------------------|------------------------------------------------------------------|-------------|
|      | What are the basic arithmetic operations?                                      |            |            | Addition, subtraction, multiplication and division. | Addition and subtraction. | Addition, subtraction, multiplication, division and square root. |             |
|      | Match each operation with its symbol.                                          |            |            | Addition\<\|\>+                                     | Subtraction\<\|\>-        | Multiplication\<\|\>\*                                           |             |
|      | The square root is a basic arithmetic operation.                               |            |            | False                                               |                           |                                                                  |             |
|      | What basic operation does it have as a + symbol?                               |            |            | Addition                                            |                           |                                                                  |             |
|      | The symbol for addition is \[\[1\]\], the symbol for subtraction is \[\[2\]\]. |            |            | \+                                                  | \-                        |                                                                  |             |
| x    | The symbol for addition is \[\[1\]\], the symbol for subtraction is \[\[2\]\]. |            |            | \+                                                  | \-                        |                                                                  |             |
| h    | Sort the result from smallest to largest.                                      |            |            | 6/2                                                 | 6-2                       | 6+2                                                              | 6\*2        |
| x    | Sort the result from smallest to largest.                                      |            |            | 6/2                                                 | 6-2                       | 6+2                                                              | 6\*2        |
|      | What is the result of SQRT(4)?                                                 |            |            | 2                                                   | -2                        |                                                                  |             |
|      | What is the result of 4/3?                                                     |            |            | 1.33\<\|\>0.03                                      |                           |                                                                  |             |
|      | Describe the addition operation.                                               |            |            |                                                     |                           |                                                                  |             |
|      | What basic operation has the symbol shown in the figure as its symbol?         | divide.png | Operation  | Division                                            |                           |                                                                  |             |
| x    | Place the name of the operations as they appear in the figure.                 | ops.png    | Operations | Addition                                            | Multiplication            | Division                                                         | Subtraction |

The configuration can be defined using an ini file with the same name as
the questions csv or *Excel* file located in the same folder. Finally,
the ini configuration file is displayed.

``` ini
[DEFAULT]
category = Initial test
first_question_number = 1
copyright = Copyright © 2024 Universidad de Granada
license = License Creative Commons Attribution-ShareAlike 4.0
correct_feedback = Correct.
partially_correct_feedback = Partially correct.
incorrect_feedback = Incorrect.
adapt_images = True
width = 800
height = 600
```

The result obtained is an xml file of questions that can be imported
directly into *Moodle*.

## Contributing

Interested in contributing? Check out the contributing guidelines.
Please note that this project is released with a Code of Conduct. By
contributing to this project, you agree to abide by its terms.

## License

`pymoodef` was created by Jose Samos. It is licensed under the terms of
the MIT license.

## Credits

`pymoodef` was created with
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the
`py-pkgs-cookiecutter`
[template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
