import logging
from contextlib import asynccontextmanager

import project.analyze_password_strength_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="Password Strength Checker API",
    lifespan=lifespan,
    description="Based on the user's requirements and the information gathered, the task involves creating an endpoint in a FastAPI application that performs comprehensive password strength analysis. The analysis will consider various factors including the password's length, complexity (incorporating uppercase and lowercase letters, numbers, and special characters), and adherence to recommended security practices (such as avoiding sequential or repeated characters). Additionally, the endpoint will check the password against known data breaches and common passwords lists to further ensure its robustness. \n\nThe endpoint will return a score indicating the password's strength (categorized as weak, medium, or strong) and provide actionable suggestions for improving password security if necessary. To implement this, the tech stack will include Python for programming, FastAPI as the API framework, PostgreSQL for database needs (if storing analysis results or user data is required), and Prisma as the ORM for efficient database interactions. \n\nThe implementation strategy will leverage the `passlib` library for hashing and validating password strength, and the `pydantic` library for data validation within FastAPI. Additionally, integration with APIs that offer data breach checks and common password lists will be necessary to enhance the analysis. \n\nA sample implementation approach for the FastAPI endpoint was previously provided, focusing on basic criteria like password length. The solution will expand on this by integrating complexity checks and the comparison with data breach and common password lists to offer a more sophisticated password strength validation system.",
)


@app.post(
    "/password/analyze",
    response_model=project.analyze_password_strength_service.PasswordStrengthAnalysisResponse,
)
async def api_post_analyze_password_strength(
    password: str,
) -> project.analyze_password_strength_service.PasswordStrengthAnalysisResponse | Response:
    """
    Analyzes the submitted password for complexity, breach history, and common patterns to return a strength score.
    """
    try:
        res = project.analyze_password_strength_service.analyze_password_strength(
            password
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
