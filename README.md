
# Ansible Role:  `algernon`

Installs and configure a [algernon](https://github.com/xyproto/algernon) server on varoius linux systems.

Algernon is an stand-alone process to deliver markdown files.


[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bodsch/ansible-algernon/CI)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-algernon)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-algernon)][releases]

[ci]: https://github.com/bodsch/ansible-algernon/actions
[issues]: https://github.com/bodsch/ansible-algernon/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-algernon/releases


## tested operating systems

* Debian 9 / 10
* Ubuntu 18.04 / 20.04
* CentOS 8
* Oracle Linux 8
* Arch Linux

## usage

### default configuration

```yaml
algernon_version: '1.12.12'

algernon_archive_name: "algernon-{{ algernon_version }}-linux.tar.xz"

algernon_system_user: algernon
algernon_system_group: algernon

algernon_bin: /usr/local/bin/algernon

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
