[![build-test](https://github.com/darkwizard242/ansible-role-terraforming/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-terraforming/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-terraforming/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-terraforming/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/47756?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47756?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47756?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-terraforming&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-terraforming) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-terraforming&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-terraforming) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-terraforming&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-terraforming) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-terraforming&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-terraforming) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-terraforming?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-terraforming?color=orange&style=flat-square)

# Ansible Role: terraforming

Role to install [terraforming](https://github.com/dtan4/terraforming) on **Debian/Ubuntu** and **EL** systems. Terraforming is capable of exporting resources into terraform code.

## Requirements

Terraforming is a gem and thus, it does require ruby installed. This role automatically installs ruby as well (if it's not already available).

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
ruby_app_debian_package: ruby-full
ruby_app_el_package: ruby
ruby_desired_state: present
terraforming_app: terraforming
terraforming_desired_state: present
terraforming_user_install: no
terraforming_include_dependencies: yes
```

### Variables table:

Variable                          | Description
--------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
ruby_app_debian_package           | Defines the app to install on Debian based systems i.e. **ruby-full**
ruby_app_el_package               | Defines the app to install on Enterprise Linux (Redhat/CentOS) systems i.e. **ruby**
ruby_desired_state                | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.
terraforming_app                  | Defines the app to install on Debian based systems i.e. **terraforming**
terraforming_desired_state        | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the gem. Defaults to `present`.
terraforming_user_install         | Defined to dynamically set whether to install terraforming gem into a user's local gems.
terraforming_include_dependencies | Defined to dynamically set whether to install relative dependencies of terraforming or not.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **terraforming** gem) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.terraforming
```

For customizing behavior of role (i.e. removal of **terraforming** gem) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.terraforming
  vars:
    terraforming_desired_state: absent
```

For customizing behavior of role (i.e. installing **terraforming** without it's required dependencies) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.terraforming
  vars:
    terraforming_include_dependencies: no
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-terraforming/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/), a DevOps/CloudOps Engineer who loves to learn and contribute to Open Source community.
