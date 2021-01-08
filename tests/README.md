# Test environment

## Execution

Start the docker container:

```bash
 $ docker-compose up -d
```

All possible scenarios will be executed by the following command:

```bash
 $ sh helper/scenario.sh
```

You can also run one specific test case by using the command:

```bash
 $ sh helper/scenario.sh [scenario]
```

Use the verbose argument to enable extended console output:

```bash
 $ sh helper/scenario.sh [scenario] -v
```

Select one of the following scenarios:

- proxy
- receiver
- sender
- shell
- module