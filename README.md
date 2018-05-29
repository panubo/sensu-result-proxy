# Sensu Result Proxy

A simple web service to authenticate and proxy Sensu passive check results.

## Running

This runs in a Docker container.

Environment Variable Configuration:

- `CONFIG_FILE` - Location of api authentication config file
- `SENSU_API_URI` - Sensu API eg. `http://localhost:4567/results`
- `DEBUG` - Enable debugging

See the `Makefile` for building, and runtime usage examples.

## Usage example

The standard Sensu `result` JSON must be posted to the endpoint:

```
JSON='{"source": "host2.example.com", "name": "my-process", "output": "all good", "status": 0, "ttl": 9000}'
curl -s -X POST \
 -H 'Content-Type: application/json' \
 -d "${JSON}" \
 http://0.0.0.0:8080/results/13548926e9a2ca72fd4677b6a7a81c6d08763356f053ad088772f9c5a46b3120
```

## Config example

```
---
# SHA256 api key associated with hostname

f61a5940cbfd10aa50667d47c46856b93e0f5acbeab8b538e843924581f218bd:
  source: host1.example.com

1f0df4b5e23e530e10221242a348cc9177def40cc88abbc8d15c918c13e388b3:
  source: host2.example.com
```

Note: the API key must match the following regex `[A-Fa-f0-9]{64}`

## Status

Experimental.
