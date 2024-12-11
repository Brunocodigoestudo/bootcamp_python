from loguru import logger

x = 5
y = 10

logger.add("monitoramento_fluxo")
def soma(x, y):
    logger.info(x)
    logger.info(y)
    logger.info(x,y)
    logger.info(y+x)
    logger.info(x+y)
    return x+y
soma(x,y)
   