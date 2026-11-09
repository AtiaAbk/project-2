"""
Student Result Management Package
"""

from .student import Student
from .result_manager import ResultManager
from .utils import (
    Colors,
    clear_screen,
    print_banner,
    print_success,
    print_error,
    print_warning,
    print_info,
    pause,
    prompt_string,
    prompt_float,
    render_student_table,
)

__all__ = [
    "Student",
    "ResultManager",
    "Colors",
    "clear_screen",
    "print_banner",
    "print_success",
    "print_error",
    "print_warning",
    "print_info",
    "pause",
    "prompt_string",
    "prompt_float",
    "render_student_table",
]

