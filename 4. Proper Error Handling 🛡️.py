# utils/error_handling.py
class PipelineError(Exception):
    """Base class for pipeline errors"""
    pass

class BlastError(PipelineError):
    """BLAST-specific errors"""
    pass

class AlignmentError(PipelineError):
    """Alignment-specific errors"""
    pass

def robust_pipeline_execution(pipeline_func, max_retries=3):
    """Decorator for robust pipeline execution with retries"""
    def wrapper(*args, **kwargs):
        last_error = None
        for attempt in range(max_retries):
            try:
                return pipeline_func(*args, **kwargs)
            except (BlastError, AlignmentError) as e:
                last_error = e
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
        raise PipelineError(f"Pipeline failed after {max_retries} attempts: {last_error}")
    return wrapper