1. 

Consider the problem of predicting how well a student does in her second year of college/university, given how well she did in her first year.

Specifically, let x be equal to the number of "A" grades (including A-. A and A+ grades) that a student receives in their first year of college (freshmen year).  We would like to predict the value of y, which we define as the number of "A" grades they get in their second year (sophomore year).

Here each row is one training example. Recall that in linear regression, our hypothesis is:
- hθ(x)=θ0+θ1x

and we use *m* to denote the number of training examples.

| x | y |
| --- | --- |
| 5 | 4 |
| 3 | 4 |
| 0 | 1 |
| 4 | 3 |

For the training set given above, what is the value of *m*?

**Answer: 4**

2.

Many substances that can burn (such as gasoline and alcohol) have a chemical structure based on carbon atoms; for this reason they are called hydrocarbons. A chemist wants to understand how the number of carbon atoms in a molecule affects how much energy is released when that molecule combusts (meaning that it is burned). the chemist obtains the dataset below. In the column on the right, "kJ/mol" is the unit measuring the amount of energy released.

| **Name of molecule** | **Number of hydrocarbons per molecule (x)** | **Heat release when burned (kJ/mol) (y)** |
| --- | --- | --- |
| methane | 1 | -890 |
| ethene | 2 | -1411 |
| ethane | 2 | -1560 |
| propane | 3 | -2220 |
| cyclopropane | 3 | -2091 |
| butane | 4 | -2878 |
| pentane | 5 | -3537 |
| benzene | 6 | -3268 |
| cycloexane | 6 | -3920 |
| hexane | 6 | -4163 |
| octane | 8 | -5471 |
| napthalene | 10 | -5157 |

You would like to use linear regression (*hθ(x) = θ0 + θ1x*) to estimate the amount of energy released (*y*) as a function of the number of carbon atoms (*x*). Which of the following do you think will be the values you obtain for *θ0* and *θ1*? You should be able to select the right answer without actually implementing linear regression.

Options:
- θ0 = -1780.0 ; θ1 = 530.9
- θ0 = -1780.0 ; θ1 = -530.9
- θ0 = -569.6 ; θ1 = -530.9
- θ0 = -596.6 ; θ1 = 530.9

**Reasoning:**

The more carbon (*x*), the more energy is released (*y*). It is estabilished that θ0 is the baseline energy release for this operation, and θ1 will give it the slope. The values for *y* goes down the bigger the *x*, so it is correct to presume it is a negative number.

The *y* also almost doubles the moment *x* gets to double, so it is correct to assume that θ0 is a less-significant number in comparison to θ1.

Checking a quick calculation, using the third option gives a result closer to the actual answer (*h(1) = -890*).
- -1780.0 + -530.9 * 1 = -2,310.9
- -569.6 + -530.9 * 1 = -1,100.5

**Answer: Option 3**

3.

Suppose we set θ0 = -1, θ1 = 2 in the linear regression hypothesis from Q1. What is hθ(6) ?

**Reasoning:**

- hθ(x) = θ0 + θ1 * x
- hθ(6) = -1 + 2 * 6 = -1 + 12 = 11

**Answer: 11**

4.

Let *f* be some function so that 

*f*(θ0,θ1) outputs a number. For this problem, *f* is some arbitrary/unknown smooth function (not necessarily the cost function of linear regression, so *f* may have local optima).

Suppose we use gradient descent to try to minimize *f*(θ0,θ1) as a function of θ0 and θ1. Which of the following statements are true? (Check all that apply.)

[ ] Even if the learning rate α is very large, every iteration of gradient descent will decrease the value of *f*(θ0,θ1).

[x] If θ0 and θ1 are initialized at a local minimum, then one iteration will not change their values.

[x] If the learning rate is too smal, then gradient descent may take a very long time to converge.

[ ] If θ0 and θ1 are initialized so that θ0 = θ1, then by symmetry (because we do simulatenous updates to the two parameters), after one iteration of gradient descent, we will still have θ0 = θ1.

**Answer: Marked as X**

5.

Suppose that for some lienar regression problem (say, predicting housing prices as in the lecture), we have some training set, and for our training set we managed to find some θ0, θ1 such that *J*(θ0,θ1) = 0.
Which of the statements below must then be true? (Check all that apply.)

[ ] For this to be true, we must have θ0 = 0 and θ1 = 0 so that *hθ(x)=0*

[ ] Gradient descent is likely to get stuck at a local minimum and fail to find the global minimum.

[ ] For this to be true, we must have *y*(i) = 0 for every value of *i = 1, 2, ..., m*

[x] Our training set can be fit perfectly by a straight line, i.e., all of our training examples lie perfectly on some straight line.

**Answer: Marked as X**