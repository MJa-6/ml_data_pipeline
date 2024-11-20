from invoke import task

@task
def test(ctx):
    """Run all tests with pytest."""
    ctx.run("poetry run pytest tests/")

@task
def lint(ctx):
    """Run ruff to check the code."""
    ctx.run("ruff check src/ml_data_pipeline")

@task
def format(ctx):
    """Automatically format and fix linting issues in the code."""
    ctx.run("ruff format src/ml_data_pipeline")

@task
def type(ctx):
    """Run mypy to check types."""
    ctx.run("poetry run mypy src/ml_data_pipeline")

@task
def docs(ctx):
    """Generate HTML documentation with pdoc."""
    ctx.run("poetry run pdoc src/ml_data_pipeline --output-dir docs")

@task
def run(ctx, config="config/config_dev.yaml"):
    """Run the ML data pipeline."""
    ctx.run(f"poetry run ml-data-pipeline --config {config}")
