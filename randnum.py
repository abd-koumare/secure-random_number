import hmac
from random import SystemRandom

_sys_rand = SystemRandom()


def _generate_uniform_num_str(a, b):
    return str(_sys_rand.uniform(a, b)).replace('.', '')


def generate_random_num_str(length=8):
    _min, _max = 0, 100
    rand_num = _generate_uniform_num_str(_min, _max)
    while len(rand_num[:length]) < length:
        rand_num += _generate_uniform_num_str(_min, _max)

    rand_index = _sys_rand.randint(0, len(rand_num) - length)
    return rand_num[rand_index:rand_index + length]


def constant_time_comparison_str(s1, s2):
    return hmac.compare_digest(bytes(s1), bytes(s2))
