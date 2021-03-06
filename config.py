class Config:
    gamma = 1.00
    eps = 0.1
    critic_lr = 1e-3
    policy_lr = 1e-3
    batch_size = 1000
    n_samples_per_state = 1
    normalize_advantages = True
    learn_std = False
