{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "97a8f9ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Question 1\n",
    "\n",
    "#    Task 1\n",
    "#    - Create a function that would swap the value of x and y using only x and y as variables.\n",
    "#    - x and y must be numeric.\n",
    "#    - Return -1 if x and y is not numeric, and\n",
    "#    - print the swapped values if both x and y are numeric.\n",
    "# function swap with 2 arguments, x and y        \n",
    "\n",
    "def swap(x, y):\n",
    "    # arguments x and y in [int, float] must be numeric either integer or float, if not, to return -1\n",
    "    if not (type(x) in [int, float] and type(y) in [int, float]):\n",
    "        return -1\n",
    "    print(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c8bc3d4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Task 2\n",
    "# Invoke the function \"swap\" using the following scenarios:\n",
    "# - \"Apple\", 10\n",
    "swap(\"Apple\", 10)\n",
    "# to call out the function swap using \"Apple\", 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2af72708",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9 17\n"
     ]
    }
   ],
   "source": [
    "# Invoke the function \"swap\" using the following scenarios:\n",
    "# - 9, 17\n",
    "swap(9, 17) \n",
    "# to call out the function swap using 9, 17"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
