# Good-Enough AR Glasses Metric

The minimum spec combination for AR glasses to function as a genuine daily-driver screen replacement, something you can wear all day and that could meaningfully replace your screens.

The score is a **weakest-link metric**: a single failing spec drags the whole product down, regardless of how good the others are.

```
score = min(nits/3000, fov/50, ppd/30, battery/8, 40/weight)
```

A score of 1.0 means the device hits every threshold. Above 1.0 means it exceeds them. The goal is to track progress over time and see when something finally crosses the line.

## Targets

| Metric | Good-Enough Target |
|---|---|
| Brightness | 3,000 nits to-eye |
| Field of View | 50° horizontal |
| Weight | 40g |
| Battery Life | 8 hours active display use |
| PPD | 30 pixels per degree |

## Devices

| Device | Year | Nits (to-eye) | FoV (°) | Weight (g) | Battery (h) | PPD | Score |
|---|---|---|---|---|---|---|---|
