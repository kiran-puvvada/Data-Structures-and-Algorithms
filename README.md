# Data-Structures-and-Algorithms
#problem Statement
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

#Solution
define a function named twosum and pass the array and target variable as parameters
    1.iterate two  loops, one from 0 to length of array and another from 1 to length of array
    2.In the inner loop write a condition that two indexes shuold not match
       1. In it add two values in that particular indexes and check whether they are equal to target or not
       2. if equal return list of indexes
