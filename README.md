# Local LLM

Experiments with local large-language-models.

Prerequisites can be installed via conda `environment.yml` or `requirements.txt` to a virtual env.

```sh
# Download and run
llm run TheBloke/Llama-2-13B-Ensemble-v6-GGUF 8000
python querylocal.py
```

```sh
# Stop
llm ps
llm kill TheBloke/Llama-2-13B-Ensemble-v6-GGUF
```

```sh
# Cleanup
llm rm TheBloke/Llama-2-13B-Ensemble-v6-GGUF
```

## Testing

[`test-01.py`](test-01.py) explores using system prompt to guide the user prompt.

```
The canine-lover tweeted:
"A purple hound trots by,
Wagging tail and witty grin,
Quirky, unique friend."
```

[`test-02.py`](test-02.py) Generates a TLDR summary from a long-form article.

```
             Here is the TL;DR of the article:

1. A soft launch helps game studios test stability, performance, core game fun, and retention before a full launch.
2. It is crucial to prioritize goals for a soft launch based on resource constraints.
3. Monitoring key metrics like FPS, crash rates, latency, D0 completion rates, D1-D7 retention, and D30 retention helps determine the game's performance.
4. Ensuring the core game loop is fun and engaging leads to high retention rates in the long run.
5. Soft launches can be beneficial for testing the game's stability, core loops, and retention before going live in the market.

Please note: This summary is based on the content of the article provided. It does not represent the viewpoint of the AI or the original authors.
```


## Ref

- https://github.com/GoogleCloudPlatform/localllm