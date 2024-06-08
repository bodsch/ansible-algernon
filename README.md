
# Ansible Role:  `algernon`

Installs and configure a [algernon](https://github.com/xyproto/algernon) server on varoius linux systems.

Algernon is an stand-alone process to deliver markdown files.


[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-algernon/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-algernon)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-algernon)][releases]
[![Ansible Downloads](https://img.shields.io/ansible/role/d/bodsch/ansible?logo=ansible)][galaxy]

[ci]: https://github.com/bodsch/ansible-algernon/actions
[issues]: https://github.com/bodsch/ansible-algernon/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-algernon/releases
[galaxy]: https://galaxy.ansible.com/ui/standalone/roles/bodsch/algernon/


If `latest` is set for `algernon_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/bin/algernon/${algernon_version}` and later linked to `/usr/bin`.
This should make it possible to downgrade relatively safely.

The algernon archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`.  
By default it is `${HOME}/.cache/ansible/algernon`.  
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `algernon_direct_download` to `true`.


## Requirements & Dependencies

Ansible Collections

- [bodsch.core](https://github.com/bodsch/ansible-collection-core)
- [bodsch.scm](https://github.com/bodsch/ansible-collection-scm)

```bash
ansible-galaxy collection install bodsch.core
ansible-galaxy collection install bodsch.scm
```
or
```bash
ansible-galaxy collection install --requirements-file collections.yml
```

### supported operating systems

* Arch Linux
* Debian based
    - Debian 10 / 11 / 12
    - Ubuntu 20.10 / 22.04

> **RedHat-based systems are no longer officially supported! May work, but does not have to.**


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-algernon/tags)!
    
    
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

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
