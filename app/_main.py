import os
import sys
import argparse
from loguru import logger
from batch_processor import process_file, run_batch
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import shutil
import uuid
try:
    from fastapi import FastAPI, UploadFile, File
    import uvicorn
    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
INPUT_DIR = os.path.join(DATA_DIR, "input")
OUTPUT_DIR = os.path.join(DATA_DIR, "output")

LOG_DIR = os.path.join(BASE_DIR, "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logger.add(
    os.path.join(LOG_DIR, "pipeline.log"),
    rotation="10 MB",
    retention="14 days",
    level="INFO"
)



def validate_directories():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.listdir(INPUT_DIR):
        logger.warning("Input directory is empty. Nothing to process.")



def run_batch_mode():
    logger.info("Starting OCR batch processing")
    try:
        run_batch()
        logger.success("Batch processing completed successfully")
    except Exception as e:
        logger.exception(f"Batch processing failed: {e}")
        sys.exit(1)



def create_api():
    app = FastAPI(title="OCR Document Pipeline")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    @app.post("/ocr")
    async def ocr_documents(files: List[UploadFile] = File(...)):
        results = []

        for file in files:
            temp_name = f"{uuid.uuid4()}_{file.filename}"
            temp_path = f"data/input/{temp_name}"

            try:
                with open(temp_path, "wb") as buffer:
                    shutil.copyfileobj(file.file, buffer)

                result = process_file(file.filename,temp_path)
                results.append({
                    "file": file.filename,
                    "success": True,
                    "result": result
                })

            except Exception as e:
                results.append({
                    "file": file.filename,
                    "success": False,
                    "error": str(e)
                })

            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)

        return {"results": results}

    return app

def run_api_mode(host: str, port: int):
    if not API_AVAILABLE:
        logger.error("FastAPI not installed. Cannot start API mode.")
        sys.exit(1)

    app = create_api()
    logger.info(f"Starting API server at http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)



def parse_args():
    parser = argparse.ArgumentParser(
        description="OCR + Document Understanding Pipeline"
    )

    parser.add_argument(
        "--mode",
        choices=["batch", "api"],
        default="batch",
        help="Run mode: batch (default) or api"
    )

    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="API host (api mode only)"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="API port (api mode only)"
    )

    return parser.parse_args()


def main():
    args = parse_args()
    validate_directories()

    logger.info(f"Pipeline started in '{args.mode}' mode")

    if args.mode == "batch":
        run_batch_mode()
    elif args.mode == "api":
        run_api_mode(args.host, args.port)
    else:
        logger.error("Invalid mode selected")
        sys.exit(1)


if __name__ == "__main__":
    main()
