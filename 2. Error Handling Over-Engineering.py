# Current: Complex decorator pattern might obscure actual errors
@robust_pipeline_execution
def run_pipeline():
    # Actual implementation buried

# Suggestion: Simpler, more transparent
def run_pipeline_with_retries(config, max_retries=3):
    for attempt in range(max_retries):
        try:
            return execute_pipeline_steps(config)
        except (BlastError, AlignmentError) as e:
            if attempt == max_retries - 1:
                raise PipelineError(f"Failed after {max_retries} attempts: {e}")
            logger.warning(f"Retry {attempt + 1} after error: {e}")