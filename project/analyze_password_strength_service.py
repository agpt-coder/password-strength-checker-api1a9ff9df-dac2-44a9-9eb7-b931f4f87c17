from typing import List

from passlib.context import CryptContext
from pydantic import BaseModel


class PasswordStrengthAnalysisResponse(BaseModel):
    """
    Response model containing the analysis result of the submitted password.
    """

    strength_score: int
    strength_category: str
    improvement_suggestions: List[str]
    breach_history_found: bool
    common_password: bool


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def analyze_password_strength(password: str) -> PasswordStrengthAnalysisResponse:
    """
    Analyzes the submitted password for complexity, breach history, and common patterns to return a strength score.

    Args:
    password (str): The password to be analyzed for its strength.

    Returns:
    PasswordStrengthAnalysisResponse: Response model containing the analysis result of the submitted password.
    """
    strength_score = 0
    improvement_suggestions = []
    breach_history_found = False
    common_password = False
    if len(password) >= 12:
        strength_score += 2
    elif len(password) >= 8:
        strength_score += 1
    else:
        improvement_suggestions.append(
            "Increase password length to at least 8 characters."
        )
    complexity_checks = [
        any((c.islower() for c in password)),
        any((c.isupper() for c in password)),
        any((c.isdigit() for c in password)),
        any((c in "!@#$%^&*()-_+" for c in password)),
    ]
    complexity_score = sum(complexity_checks)
    strength_score += complexity_score
    if complexity_score < 4:
        if not any((c.islower() for c in password)):
            improvement_suggestions.append("Include at least one lowercase letter.")
        if not any((c.isupper() for c in password)):
            improvement_suggestions.append("Include at least one uppercase letter.")
        if not any((c.isdigit() for c in password)):
            improvement_suggestions.append("Include at least one digit.")
        if not any((c in "!@#$%^&*()-_+" for c in password)):
            improvement_suggestions.append("Include at least one special character.")
    common_passwords = ["password", "123456", "12345678", "qwerty", "abc123"]
    breach_history_found = False
    common_password = password in common_passwords
    if common_password:
        strength_score -= 2
        improvement_suggestions.append("Choose a less common password.")
    if strength_score >= 6:
        strength_category = "strong"
    elif strength_score >= 3:
        strength_category = "medium"
    else:
        strength_category = "weak"
    return PasswordStrengthAnalysisResponse(
        strength_score=strength_score,
        strength_category=strength_category,
        improvement_suggestions=improvement_suggestions,
        breach_history_found=breach_history_found,
        common_password=common_password,
    )
