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

### [`test-01.py`](test-01.py) 

This test explores using system prompt to guide the user prompt.

```
The canine-lover tweeted:
"A purple hound trots by,
Wagging tail and witty grin,
Quirky, unique friend."
```

### [`test-02.py`](test-02.py) 

Generates a TLDR summary from a long-form article.

```
             Here is the TL;DR of the article:

1. A soft launch helps game studios test stability, performance, core game fun, and retention before a full launch.
2. It is crucial to prioritize goals for a soft launch based on resource constraints.
3. Monitoring key metrics like FPS, crash rates, latency, D0 completion rates, D1-D7 retention, and D30 retention helps determine the game's performance.
4. Ensuring the core game loop is fun and engaging leads to high retention rates in the long run.
5. Soft launches can be beneficial for testing the game's stability, core loops, and retention before going live in the market.

Please note: This summary is based on the content of the article provided. It does not represent the viewpoint of the AI or the original authors.
```

### [`test-03.py`](test-03.py) 

This test explores the interpretation of tabular data to understand what formats are or are not interpreted by the LLM.

```py
df = pandas.read_excel(
    "data/rt-2023-simple.xlsx", 
    sheet_name='Rio Tinto Production Summary',
)
table = df.to_markdown(tablefmt="github", index=False)
print(table)
# ...
{
    "role": "user",
    "content": f"""
        Consider the following commodity production table. 
        What is the 2023 Iron Ore production?
        ----
        {table}
    """
},
```
```
| Principal Commodities   | Unnamed: 1   |    2022-Q4 |   2023-Q3 |   2023-Q4 |   2022 Total |   2023 Total |
|-------------------------|--------------|------------|-----------|-----------|--------------|--------------|
| Alumina                 | ('000 t)     |  1940.92   |  1897.43  |  1919.17  |     7543.75  |     7537     |
| Aluminium               | ('000 t)     |   782.858  |   828.477 |   846     |     3009.21  |     3272     |
| Bauxite                 | ('000 t)     | 13180.8    | 13939.9   | 15097.8   |    54618     |    54618.7   |
| Borates                 | ('000 t)     |   141.23   |   126.801 |   111.253 |      531.743 |      495.373 |
| Copper - mined          | ('000 t)     |   131.292  |   155.114 |   146.173 |      521.147 |      562.417 |
| Copper - refined        | ('000 t)     |    51.0363 |    34.125 |    46.072 |      209.218 |      175.234 |
| Iron Ore                | ('000 t)     | 78415.2    | 73240.5   | 76514.1   |   283247     |   290171     |
| Titanium dioxide slag   | ('000 t)     |   323.473  |   246.811 |   275.178 |     1199.66  |     1110.51  |
*************http://localhost:8000/v1*************
 

The provided table gives information about various commodities' production data up to 2022-Q4 (2022 total) and 2023-Q3 for some commodities. Iron Ore production data for 2023-Q4 (which would be the full 2023 Iron Ore production) isn't included in this table. 

The latest complete information given is 2022 Total Iron Ore production which is 283247 thousand tonnes. To find the 2023 Iron Ore production, you'd need additional data not provided in this table.
```

Interestingly, the model has interpreted the unnamed column and the `('000 t)` notation to mean _thousand tonnes_. It has not however interpretted the year total columns - it assumes the year-quarter columns are cumulative.

## Ref

- https://github.com/GoogleCloudPlatform/localllm