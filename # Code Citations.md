# Code Citations

## License: unknown
https://github.com/DanLopess/EcoRoute/tree/c100d675a03eee4b62f7e1b0c0755c8e19ed5dd0/experimental/exp_genetic_algorithm.py

```
create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, 0
```


## License: MIT
https://github.com/colinch4/colinch4.github.io/tree/e311fb0e9d2c623501b943aa5210b9918664873c/_posts/2023/10/01/2023-10-01-17-48-37-392090-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B3%BC-%EC%9C%A0%EC%A0%84-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%A8%EA%BB%98-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%8B%9C%EA%B0%81%ED%99%94.md

```
)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
    toolbox.register("select", tools.
```

