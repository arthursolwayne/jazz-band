# GRPO (Group Relative Policy Optimization)

## Source
DeepSeekMath paper (arXiv:2402.03300), February 2024

## Loss Function

```
L = - sum_j sum_k ( (pi_theta(a_jk | s_j) / pi_theta_old(a_jk | s_j)) * A_jk )
    + beta * sum_j KL(pi_theta(. | s_j) || pi_theta_old(. | s_j))
```

Where:
- M = number of prompts
- K_j = responses per prompt
- beta = KL divergence penalty coefficient

## Advantage Computation

```
A_jk = R_jk - mean(R_j)
```

Or normalized version:
```
A = (r_i - mean(r)) / std(r)
```

The advantage is **sequence-level**, not per-token. All tokens in a sequence share the same advantage value.

## Gradient Computation Level

**SEQUENCE LEVEL**

From AI Engineering Academy:
> "The importance ratio for a sequence a_{jk} is computed as the product of the ratios for each token in the sequence, reflecting the policy's probability distribution over the entire response."

This means:
- Rewards are computed for complete sequences
- Advantages are computed per-sequence
- The gradient aggregates across all tokens in the sequence
- All tokens get the same reward signal

## Key Innovation

GRPO eliminates the critic/value network by using **group mean as baseline**:
- Generate multiple responses per prompt
- Use mean reward of the group as the baseline
- Advantage = how much better/worse than average

## References

- https://arxiv.org/abs/2402.03300
- https://aiengineering.academy/LLM/TheoryBehindFinetuning/GRPO/
- https://ghost.oxen.ai/why-grpo-is-important-and-how-it-works/
- https://rlhfbook.com/c/11-policy-gradients.html
