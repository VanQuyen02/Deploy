from pathlib import Path

class LoggingConfig:
    ROOT_DIR = Path(__file__).parent.parent
    LOG_DIR = ROOT_DIR / "logs"

    @staticmethod
    def create_log_dir():
        LoggingConfig.LOG_DIR.mkdir(parents=True, exist_ok=True)

# Ensure the log directory is created when the module is imported
LoggingConfig.create_log_dir()
