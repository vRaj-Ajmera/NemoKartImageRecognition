# NemoKartImageRecognition
YOLO Object detection training on karts in NemoKart

## Commands

### Training:
```cd yolov5``` folder then run the following:

```python train.py --img 640 --batch 16 --epochs 300 --data ../data.yaml --weights yolov5s.pt```

best.pt is saved in yolov5/runs/train/expX where X is most recent run.

### Validation:
```cd yolov5``` folder then run the following:

```python detect.py --weights runs/train/exp7/weights/best.pt --img 640 --conf 0.25 --source "C:\NemoKartImageRecognition\tests\Race_Screenshots\race50.png"```