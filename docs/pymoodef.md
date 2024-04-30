
<!-- README.md is generated from README.Rmd. Please edit that file -->

# pymoodef: Defining Moodle Elements from Python

[*Moodle*](https://moodle.org/) is a widespread open source learning
platform. It is the official teaching support platform of the University
of Granada (Spain), where we develop this package.

The goal of the `pymoodef` package is to harness the power of Python to
make defining *Moodle* elements easier. In particular, this first
version is focused on the definition of questions for quizzes.

The process is as follows: we define the questions in Python, from the
definition, we generate an xml file that we can import directly into
*Moodle*.

What does this package provide? On the one hand, we have simplified the
process of manually defining the questions, considering only the
essential parameters for each type. On the other hand, the package
offers an infrastructure that allows the automatic or semi-automatic
generation of questions from Python: to define a question we simply need
to include a row in a a csv file or an *Excel* file.

The rest of this document is structured as follows: First, the general
process of defining questions is presented. Next, we show the types of
questions considered and how to define them. Finally, the document ends
with conclusions.

# Question definition process

One of the main objectives considered in the package design has been to
simplify the definition of the questions. To do this, we have considered
for each question the default values that we use most frequently and we
only have to define the specific components of the question:

- statement,
- an optional image and
- answers.

We do not even have to define the type, only, in some cases, indicate
some additional detail, such as the orientation of the presentation of
the answers. The type is deduced from the definition.

Questions are defined within the framework of a *category* (*Moodle*
concept). In its definition we have included the general configuration
parameters for all questions.

Therefore, the definition process is as follows:

1.  Define the category (and general characteristics).

2.  Define questions.

3.  Generate the xml file with the result.

4.  Import the xml file from *Moodle*.

As a result, the questions are added to the question bank within the
category and can be used directly in the definition of quizzes. If we
need to configure a specific aspect of a question, it can be done there.

In this section we are going to show the first three points of this
process.

## Define the category and general characteristics

To define a category we use a configuration ini file, where the category
and other general characteristics of all the questions are indicated.

Below are the parameters that are defined next to the question category.

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

In addition to the category name in the `category` parameter, we define
the `copyright` and `license` parameters that will appear between
comments in the xml file associated with each question, as can be seen
below.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="category">
    <category> <text>$course$/top/Initial test</text> </category>
    <info format="html"> <text></text> </info>
    <idnumber></idnumber>
  </question>
<question type="...">
...
<questiontext format="html">
  <text><![CDATA[
     <!-- Copyright © 2024 Universidad de Granada -->
     <!-- License Creative Commons Attribution-ShareAlike 4.0 -->
     ... ]]></text>
...
</questiontext>
...
</question>
</quiz>
```

Questions have a name, which is displayed as a summary in the *Moodle*
question bank. We compose the name from the number of the question, the
type of question that we have deduced and the beginning of its
statement. For example, below is a generated question name.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
...  
<question type="multichoice">
<name> <text>q_001_multichoice_what_are_the_basic_arithmetic_operations</text> </name>
...
</question>
</quiz>
```

Using the parameter `first_question_number`, the number that will be
assigned to the first question is defined, with a three-digit format.
This number will increase for each question.

For each question we can indicate feedback text for cases in which the
answer is correct, partially correct or incorrect: The corresponding
values are provided by the `correct_feedback`,
`partially_correct_feedback` and `incorrect_feedback` parameters.

Finally, each question stem can include an image. Sometimes the images
we use have very different sizes and require a prior transformation to
homogenize their presentation. This transformation can be carried out
automatically by indicating it using the parameter `adapt_images`
(default is `False`). Using the parameters `width` and `height` we
indicate the size of the resulting image. It is advisable to test this
functionality and adjust the size accordingly by viewing the result when
defining a questionnaire in *Moodle*. **The original images are not
modified**, only those that are embedded in the xml file.

## Define questions

We can define the questions in bulk using a csv file or an *Excel* file.
Below is the structure of the files and how to use them for generating
the result.

### File structure

In the included examples, the files have the following columns.

``` csv
type, question, image, image_alt, answer, a_1, a_2, a_3
```

We can add as many additional columns as we consider necessary. The
names of the additional columns are not important, for example we can
follow the same criteria: `a_4`, `a_5`, etc.

In that file, we can include rows using a text editor, Python or some
tool to edit csv or *Excel* files in spreadsheet format.

Below is the content of the csv and *Excel* files included in this
package.

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

The type of question is deduced from the statement and the answers. The
`type` column is used to distinguish between two types of questions and
also to indicate the presentation of the answers. It can have three
values: empty, `h` or any other value different from those two. In the
above example it is `x`, that is, the third case: As we will see in the
next section, it indicates that it is not a `multichoice` question and
that the values are not displayed horizontally (`h` value).

The question statement is defined by the column `question`.

An image can be shown after statement. Using the column `image` we
indicate the file that contains it: To include an image, simply include
its location based on the location of the question definition file; in
the examples the images are in the same folder as the question file
(`divide.png` and `ops.png`). Each image must have a description that is
indicated by the `image_alt` column.

Finally we define the answers to the question. Using the column `answer`
we indicate the first one. If necessary, we can indicate the rest in a
variable way with the column names we want, as many as we need to
include.

There are types of questions in which two string values must be
indicated for each answer. The criterion we have adopted to include two
values in a cell is to use a separator and define them in a single
string, the separator is `<|>`: It can be seen in the definition of some
of the previous questions, for example, `Addition<|>+` or `1.33<|>0.03`.

### Generation using a csv file or an *Excel* file

If we place files for questions, `questions.csv` or `questions.xlsx`,
and `questions.ini` in the same folder (files can have any name but it
must be the same for the questions, csv or xlsx, and for the
configuration, ini), we can generate file `questions.xml` (also in the
same folder) in the following way.

``` bash
$ python -m pymoodef tests/questions.csv 
```

For *Excel* files the definition is carried out in the same way.

``` bash
$ python -m pymoodef tests/questions.xlsx
```

We can also indicate the xml file that we want to be generated, as shown
below.

``` bash
$ python -m pymoodef tests/questions.csv result.xml
```

By default, csv files with columns separated by “,” are considered. In
case of using “;” as a separator, simply add a “2” after the file name,
as shown below for file `tests/questions1.csv`.

``` bash
$ python -m pymoodef tests/questions1.csv2
```

## Generated xml file

The generated file is the one that we can import from *Moodle* in the
*Question Bank* section.

If we have included images, the file size increases considerably because
they are embedded in xml (not referenced).

The definition file for a single question is shown below.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="category">
    <category> <text>$course$/top/Initial test</text> </category>
    <info format="html"> <text></text> </info>
    <idnumber></idnumber>
  </question>
  <question type="multichoice">
<name> <text>q_001_multichoice_what_are_the_basic_arithmetic_operations</text> </name>
<questiontext format="html">
  <text><![CDATA[
     <!-- Copyright © 2024 Universidad de Granada -->
     <!-- License Creative Commons Attribution-ShareAlike 4.0 -->
     <p>What are the basic arithmetic operations?</p>]]></text>
     
</questiontext>
<generalfeedback format="html"> <text></text> </generalfeedback>
<defaultgrade>1.0000000</defaultgrade>
<penalty>0.5</penalty>
<hidden>0</hidden>
<idnumber></idnumber>
<single>true</single>
<shuffleanswers>true</shuffleanswers>
<answernumbering>abc</answernumbering>
<showstandardinstruction>0</showstandardinstruction>
<correctfeedback format="moodle_auto_format"> <text>Correct.</text> </correctfeedback>
<partiallycorrectfeedback format="moodle_auto_format"> <text></text> </partiallycorrectfeedback>
<incorrectfeedback format="moodle_auto_format"> <text>Incorrect.</text> </incorrectfeedback>
<answer fraction="100" format="html">
   <text>Addition, subtraction, multiplication and division.</text>
   <feedback format="html"> <text>Correct.</text> </feedback>
</answer>
<answer fraction="-50.000000000000000" format="html">
   <text>Addition and subtraction.</text>
   <feedback format="html"> <text>Incorrect.</text> </feedback>
</answer>
<answer fraction="-50.000000000000000" format="html">
   <text>Addition, subtraction, multiplication, division and square root.</text>
   <feedback format="html"> <text>Incorrect.</text> </feedback>
</answer>
</question>
</quiz>
```

# Kind of questions

We have simplified and generalized the definition process for 9 types of
questions, so that we do not even have to indicate the type to define
them, it is deduced from the definition: It depends on the value of the
`answer` column. In some cases a character in the `type` column is used
to distinguish between two types whose definition is identical or to
indicate the orientation of the answers (horizontal or vertical), as we
will see below. We dedicate a section to each type with the names that
are generated in the xml file.

## `essay`

Only includes the question statement with or without an image (the
`answer` field is empty). The answer to the question is made through
free text. Below is an example that we had shown before.

| type | question                         | image | image_alt | answer | a_1 | a_2 | a_3 |
|------|----------------------------------|-------|-----------|--------|-----|-----|-----|
|      | Describe the addition operation. |       |           |        |     |     |     |

## `truefalse`

The `answer` field contains the correct answer. If this is one of the
literals corresponding to the boolean values (`'True'` or `'False'`),
nothing else needs to be indicated. Here is an example.

| type | question                                         | image | image_alt | answer | a_1 | a_2 | a_3 |
|------|--------------------------------------------------|-------|-----------|--------|-----|-----|-----|
|      | The square root is a basic arithmetic operation. |       |           | False  |     |     |     |

## `numerical`

If the value of field `answer` is a number with or without decimal
places, or a vector of two numbers, it is a `numerical` question.

In this type of questions we only have to indicate correct values of the
answer. If, instead of a value, we indicate a vector of two values, the
second number represents the margin of error in which the answer is
accepted as valid. Below are two examples.

| type | question                       | image | image_alt | answer         | a_1 | a_2 | a_3 |
|------|--------------------------------|-------|-----------|----------------|-----|-----|-----|
|      | What is the result of SQRT(4)? |       |           | 2              | -2  |     |     |
|      | What is the result of 4/3?     |       |           | 1.33\<\|\>0.03 |     |     |     |

## `shortanswer`

If only field `answer` is defined and it is not a boolean or numeric
value, it is of type `shortanswer`, for example:

| type | question                                         | image | image_alt | answer   | a_1 | a_2 | a_3 |
|------|--------------------------------------------------|-------|-----------|----------|-----|-----|-----|
|      | What basic operation does it have as a + symbol? |       |           | Addition |     |     |     |

## `multichoice`

If field `answer` and the rest of the answers are of type string, it is
of type `multichoice`. The content of field `answer` is the correct
answer. Here is an example.

| type | question                                  | image | image_alt | answer                                              | a_1                       | a_2                                                              | a_3 |
|------|-------------------------------------------|-------|-----------|-----------------------------------------------------|---------------------------|------------------------------------------------------------------|-----|
|      | What are the basic arithmetic operations? |       |           | Addition, subtraction, multiplication and division. | Addition and subtraction. | Addition, subtraction, multiplication, division and square root. |     |

## `ordering`

Type `ordering` is defined as type `multichoice`. To distinguish it, we
assign the column `type` a value other than empty, which is its default
value. If we assign the value `h`, the answers will be presented
horizontally, if it is different from `h`, they will be presented
vertically.

In the example below, the two questions are the same, only the way the
answers are presented changes.

| type | question                                  | image | image_alt | answer | a_1 | a_2 | a_3  |
|------|-------------------------------------------|-------|-----------|--------|-----|-----|------|
| h    | Sort the result from smallest to largest. |       |           | 6/2    | 6-2 | 6+2 | 6\*2 |
| x    | Sort the result from smallest to largest. |       |           | 6/2    | 6-2 | 6+2 | 6\*2 |

## `ddwtos` and `gapselect`

In questions of these types the objective is to fill in the gaps with
the terms indicated. If the variable `type` has the default value (empty
string), the values are filled by dragging and dropping. If we define a
value other than empty in the variable `type`, they are filled by
selecting from a list.

Gaps in the statement are defined by numbers in double brackets, as
shown in the following examples.

| type | question                                                                       | image | image_alt | answer | a_1 | a_2 | a_3 |
|------|--------------------------------------------------------------------------------|-------|-----------|--------|-----|-----|-----|
|      | The symbol for addition is \[\[1\]\], the symbol for subtraction is \[\[2\]\]. |       |           | \+     | \-  |     |     |
| x    | The symbol for addition is \[\[1\]\], the symbol for subtraction is \[\[2\]\]. |       |           | \+     | \-  |     |     |

We have to indicate as many answers as gaps, in the correct order.

## `matching`

If the answers are made up of vectors of pairs of strings, we are in a
type `matching` question. Below we show an example.

| type | question                              | image | image_alt | answer          | a_1                | a_2                    | a_3 |
|------|---------------------------------------|-------|-----------|-----------------|--------------------|------------------------|-----|
|      | Match each operation with its symbol. |       |           | Addition\<\|\>+ | Subtraction\<\|\>- | Multiplication\<\|\>\* |     |

# Conclusions

The `pymoodef` package makes it easy to define questions for *Moodle*
quizzes.

We can define the questions in bulk using a csv or *Excel* file. We have
simplified and generalized the definition so that the types considered
are defined with the same columns.

The functionality offered by the package can be used to manually define
the questions quickly or to define them automatically or
semi-automatically from Python.

The result of the definition process is an xml file that can be imported
directly into the *Moodle* question bank.
