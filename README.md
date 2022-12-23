
# Ansible Role:  `algernon`

Installs and configure a [algernon](https://github.com/xyproto/algernon) server on varoius linux systems.

Algernon is an stand-alone process to deliver markdown files.


[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-algernon/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-algernon)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-algernon)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-algernon/actions
[issues]: https://github.com/bodsch/ansible-algernon/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-algernon/releases
[quality]: https://galaxy.ansible.com/bodsch/algernon

### supported operating systems

* ArchLinux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.04
* RedHat based
    - Alma Linux 8
    - Rocky Linux 8
    - OracleLinux 8

## usage

### default configuration

```yaml
algernon_version: '1.13.0'

algernon_direct_download: false

algernon_system_user: algernon
algernon_system_group: algernon

algernon_service_state: started

algernon_data_directory: /var/www/algernon

algernon_listen_port: 8090
algernon_listen_address: '127.0.0.1'

algernon_config:
  listen:
    address: "{{ algernon_listen_address }}"
    port: "{{ algernon_listen_port }}"
  data_directory: "{{ algernon_data_directory }}"
  cache: "on"
  redis:
    host: 127.0.0.1
```

### redis configuration

```yaml
algernon_config:
  ...
  redis:
    host: 127.0.0.1
    port: 6379
```

### cache configuration

Sets a cache mode.

**The default is `on`.**

| parameter | description |
| :----     | :-----      |
| `on`      | Cache everything |
| `off`     | Disable caching |
| `dev`     | Everything, except Amber, Lua, GCSS, Markdown and JSX |
| `prod`    | Everything, except Amber and Lua |
| `small`   | Like `prod`, but only files <= 64KB |

```yaml
algernon_config:
  ...
  cache: "small"
```
