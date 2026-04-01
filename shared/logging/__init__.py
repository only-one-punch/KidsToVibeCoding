"""统一日志配置模块"""
import logging
import sys
from datetime import datetime
from typing import Any
import json


class JSONFormatter(logging.Formatter):
    """JSON 格式日志格式化器"""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # 添加额外字段
        if hasattr(record, "extra"):
            log_data["extra"] = record.extra
        
        # 添加异常信息
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_data, ensure_ascii=False)


def setup_logging(
    service_name: str,
    log_level: str = "INFO",
    log_format: str = "json"
) -> logging.Logger:
    """
    配置日志系统
    
    Args:
        service_name: 服务名称
        log_level: 日志级别
        log_format: 日志格式 (json/text)
    
    Returns:
        配置好的 Logger
    """
    logger = logging.getLogger(service_name)
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # 清除已有的 handlers
    logger.handlers.clear()
    
    # 创建 console handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(getattr(logging, log_level.upper()))
    
    if log_format == "json":
        formatter = JSONFormatter()
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """获取 Logger 实例"""
    return logging.getLogger(name)
