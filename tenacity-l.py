from tenacity import retry, stop_after_attempt
import random


@retry(stop=stop_after_attempt(4))
def risky():
    if random.random() < 0.5:
        c += 1
        raise Exception('Error')
    print('its ok')
    print(c)
c=0
risky()