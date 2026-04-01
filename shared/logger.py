"""
统一日志系统
JSON 格式输出，统一字段
"""
import logging
import json
import sys
from datetime import datetime
from typing import Any, Dict
from functools import lru_cache


class JSONFormatter(logging.Formatter):
    """JSON 格式日志格式化器"""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data: Dict[str, Any] = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # 添加异常信息
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        # 添加额外字段
        if hasattr(record, "extra_data"):
            log_data["data"] = record.extra_data
        
        return json.dumps(log_data, ensure_ascii=False)


@lru_cache()
def get_logger(name: str, level: str = "INFO") -> logging.Logger:
    """获取配置好的 logger 实例"""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JSONFormatter())
        logger.addHandler(handler)
    
    return logger


def log_with_data(logger: logging.Logger, level: str, message: str, **kwargs):
    """带额外数据的日志记录"""
    record = logger.makeRecord(
        logger.name,
        getattr(logging, level.upper()),
        "",
        0,
        message,
        (),
        None,
    )
    record.extra_data = kwargs
    logger.handle(record)
