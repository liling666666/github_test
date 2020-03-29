# 初始化日志配置
# 导包
import logging.handlers
import os

BASEPATH = os.path.dirname(os.path.abspath(__file__))
headers = {"Content-Type": "application/json"}
emp_id = ""

def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(level=logging.INFO)
    # 创建处理器
    # 控制台显示
    sh = logging.StreamHandler()
    # 文件夹显示,以时间切割
    # 设置日志保存的文件路径
    filename = BASEPATH+"/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                   when="M",
                                                   interval=1,
                                                   backupCount=3)
    # 设置格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 格式器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)












