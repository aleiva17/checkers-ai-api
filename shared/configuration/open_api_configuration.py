from fastapi.openapi.utils import get_openapi


def custom_open_api(routes):
    return get_openapi(
        title="Checkers AI",
        version="1.0.0",
        description="Introducing Checker AI, your key to unlocking strategic supremacy in the game of checkers. "
                    "Harness the power of artificial intelligence to uncover the next best move effortlessly.",
        routes=routes
    )
