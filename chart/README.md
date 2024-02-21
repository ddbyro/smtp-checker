
# SMTP Checker Helm Chart

This Helm chart deploys the SMTP Checker application on a Kubernetes cluster.

## Prerequisites

- Kubernetes 1.12+
- Helm 3.0+

## Installing the Chart

To install the chart with the release name `my-release`:

```bash
helm install my-release ./chart
```

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```bash
helm uninstall my-release
```

## Configuration

The following table lists the configurable parameters of the SMTP Checker chart and their default values.

| Parameter            | Description                      | Default                           |
|----------------------|----------------------------------|-----------------------------------|
| `replicaCount`       | Number of replicas               | `1`                               |
| `image.repository`   | Image repository                 | `<image repository>/smtp-checker` |
| `image.tag`          | Image tag                        | `1.0.0`                           |
| `image.pullPolicy`   | Image pull policy                | `IfNotPresent`                    |
| `config.smtp_server` | SMTP server                      | `smtp.gmail.com`                  |
| `config.smtp_port`   | SMTP port                        | `587`                             |
| `config.sleep_time`        | sleep_time before checking again | `30`                              |

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,

```bash
helm install my-release ./chart --set image.tag=2.0.0
```
