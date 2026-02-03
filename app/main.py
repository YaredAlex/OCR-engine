import os
import sys
import argparse
from loguru import logger
from batch_processor import process_file, run_batch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logger.add(
    os.path.join(LOG_DIR, "pipeline.log"),
    rotation="10 MB",
    retention="14 days",
    level="INFO"
)


def run_single_document(file_path: str):
    print("starting processing")
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        sys.exit(1)

    logger.info(f"Processing single document: {file_path}")

    try:
        process_file(os.path.basename(file_path), single_path=file_path)
        logger.success("Single document processed successfully")
    except Exception as e:
        logger.exception(f"Single document processing failed: {e}")
        sys.exit(1)


def run_batch_documents():
    logger.info("Starting batch OCR processing")
    try:
        run_batch()
        logger.success("Batch processing completed")
    except Exception as e:
        logger.exception(f"Batch processing failed: {e}")
        sys.exit(1)


# CLI Arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description="OCR + Document Understanding Pipeline"
    )

    parser.add_argument(
        "--mode",
        choices=["batch", "single"],
        required=True,
        help="Run mode: batch or single"
    )

    parser.add_argument(
        "--file",
        help="Path to a single document (required for single mode)"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.mode == "single":
        if not args.file:
            logger.error("Single mode requires --file argument")
            sys.exit(1)
        run_single_document(args.file)

    elif args.mode == "batch":
        run_batch_documents()

    else:
        logger.error("Invalid mode")
        sys.exit(1)

if __name__ == "__main__":
    main()


