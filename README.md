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

## Status

Experimental.
