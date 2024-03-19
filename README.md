# Local LLM

Experiments with local large-language-models.

```sh
# Download and run
llm run TheBloke/Llama-2-13B-Ensemble-v6-GGUF 8000
python querylocal.py
----

```sh
# Stop
llm ps
llm kill TheBloke/Llama-2-13B-Ensemble-v6-GGUF
```

```sh
# Cleanup
llm rm TheBloke/Llama-2-13B-Ensemble-v6-GGUF
```

## Ref

- https://github.com/GoogleCloudPlatform/localllm