import os



for i in range(6,10):
    command = f"python main.py --gan mrelgan --model coco-64-{i} --pretrain"
    os.system(command)