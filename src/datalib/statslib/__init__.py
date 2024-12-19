# src/datalib/statistics/__init__.py

from .basic_stats import (
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_std,
    calculate_correlation
)

from .statistical_tests import (
    t_test,
    chi_square_test
)
