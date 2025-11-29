# REINFORCE Algorithm (Williams 1992)

## Original Paper

Williams, R.J. (1992). "Simple statistical gradient-following algorithms for connectionist reinforcement learning." Machine Learning, 8, 229-256.

PDF: https://link.springer.com/content/pdf/10.1007/BF00992696.pdf

## What REINFORCE Stands For

**RE**ward **I**ncrement = **N**onnegative **F**actor x **O**ffset **R**einforcement x **C**haracteristic **E**ligibility

## Core Contribution

> "These algorithms, called REINFORCE algorithms, are shown to make weight adjustments in a direction that lies along the gradient of expected reinforcement in both immediate-reinforcement tasks and certain limited forms of delayed-reinforcement tasks, and they do this without explicitly computing gradient estimates or even storing information from which such estimates could be computed."

## The Algorithm

The vanilla policy gradient:
```
gradient_theta J = E [ sum_t gradient_theta log pi_theta(a_t|s_t) * R ]
```

Key insight: You can estimate the gradient of expected reward without differentiating through the reward function itself.

## Historical Context

> "REINFORCE methods were known for high variance on the policy gradients, leading to unstable learning. Basic methods like baselining and other regularization tools (off-policy gradients, actor-critic methods, etc.) all emerged."

Evolution: REINFORCE -> TRPO -> PPO -> GRPO

## Why It Works

The log-derivative trick:
```
gradient_theta E[R] = E[R * gradient_theta log pi_theta]
```

This converts differentiation through an expectation into an expectation of a product - which can be estimated by sampling.

## References

- https://link.springer.com/article/10.1007/BF00992696
- https://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_4_policy_gradient.pdf
