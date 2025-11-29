# PPO (Proximal Policy Optimization) for RLHF

## Policy Gradient Formula

```
gradient_J(pi_theta) = E_tau~pi_theta [ sum_{i=0}^T gradient_theta log pi_theta(a_i|s_i) * R(tau) ]
```

This decomposes across timesteps - gradient of log-probability for each token, scaled by return.

## Loss Function

```
L_POLICY = min(r_t(theta) * A_t, clip(r_t(theta), 1-epsilon, 1+epsilon) * A_t)
```

Where:
- r_t = probability ratio between new and old policies
- A_t = advantage estimate
- epsilon = clipping parameter (typically 0.2)

## Token vs Sequence Level

From Nathan Lambert's RLHF Book:

**Two approaches exist:**

### 1. Bandit (Sequence-Level)
> "the whole completion as a single action with one scalar reward... multiplying it by the (length-normalized) sum of per-token log-probs, thereby broadcasting the same learning signal to every token."

All tokens receive identical advantage values.

### 2. MDP (Token-Level)
> "enables token-level credit assignment via a value function (V(s_t))... and per-token KL."

Individual tokens get different values through learned value functions.

## What Gets Differentiated

> "only gradient_theta log pi_theta(a_t|s_t) survives"

The log-probability of actions (tokens) with respect to policy parameters. Environment dynamics and rewards do not need to be differentiable.

## Credit Assignment Problem

From RLHF Book:
> "A central assumption in policy gradient optimization is that we can reliably estimate the policy gradient using our chosen method. However, when the problem scales up—for instance, when each trajectory becomes very long or the policy model is extremely large—you must sample many trajectories to obtain an accurate gradient estimate; otherwise, you face high variance."

## Variance Issues

> "Although the gradient estimator in policy gradient algorithms is theoretically unbiased, its variance can be extremely high."

Solutions:
- Baselines/advantage estimation (GAE)
- KL penalties
- Larger batch sizes
- Clipping (PPO's core contribution)

## References

- https://rlhfbook.com/c/11-policy-gradients.html
- https://huggingface.co/blog/NormalUhr/rlhf-pipeline
- https://cameronrwolfe.substack.com/p/proximal-policy-optimization-ppo
- https://arxiv.org/abs/2307.04964 (Secrets of RLHF Part I: PPO)
