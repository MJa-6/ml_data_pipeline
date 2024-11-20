import argparse
import sys
from loguru import logger
from .config import load_config
from .data_loader import DataLoaderFactory
from .data_transform import TransformerFactory


def setup_logger():
    # Configure Loguru logger to log to a file with rotation and also to the console
    logger.add("logs/pipeline.log", rotation="500 MB", backtrace=True, diagnose=True)
    logger.add(
        sys.stderr,
        colorize=True,
        format="<green>{time}</green> <level>{message}</level>",
    )


def main(config_path=None):
    if config_path is None:
        parser = argparse.ArgumentParser(
            description="Run the ML data pipeline with specified configuration."
        )
        parser.add_argument(
            "--config",
            type=str,
            required=True,
            help="Path to the configuration YAML file.",
        )
        args = parser.parse_args()
        config_path = args.config

    # Set up logging
    setup_logger()

    logger.info("Loading configuration settings from {}", config_path)
    config = load_config(config_path)

    # Load data using DataLoaderFactory
    logger.info(
        "Loading data with format: {} from path: {}",
        config.data_loader.file_type,
        config.data_loader.file_path,
    )
    data_loader = DataLoaderFactory.get_data_loader(config.data_loader.file_type)
    data = data_loader.load_data(config.data_loader.file_path)

    # Transform data using TransformerFactory
    logger.info(
        "Transforming data using scaling method: {}",
        config.transformation.scaling_method,
    )
    transformer = TransformerFactory.get_transformer(
        config.transformation.scaling_method
    )
    transformed_data = transformer.transform(data)

    logger.info("Transformation complete. Here's a preview of the transformed data:")
    print(transformed_data.head())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the ML data pipeline.")
    parser.add_argument(
        "--config", type=str, required=True, help="Path to configuration file."
    )
    args = parser.parse_args()
    main(args.config)
