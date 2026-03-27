def validate_status(status: str) -> bool:
    return status in ["new", "in_progress", "done"]