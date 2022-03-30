

from time import sleep
from progressBar import ProgressBarCLI, ProgressBar

prog_bar = ProgressBar(total=100)

my_bar = ProgressBarCLI(total=10000, prefix='Progress', suffix='Total', length=100)

for _ in range(10000):
    # sleep(1)
    # next(my_bar)
    my_bar.value += 1
    my_bar.print_bar()
