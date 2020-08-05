# Sample Assert Collection

## Requirements

* ansible >= 2.9

## Install

```
$ mkdir -p collections/ansible_collections/sample
$ git clone https://github.com/sky-joker/sample_assert_collection.git
$ mv sample_assert_collection collections/ansible_collections/sample/assert_collection
```

## Example Playbook

The following is the port check example playbook.

```yaml
---
- name: example playbook
  hosts: all
  collections:
    - sample.assert_collection
  gather_facts: no
  tasks:
    - name: "Listen port check"
      assert_port:
        ports:
          - 22
          - 80
        state: tcp
```

The following is the file check example playbook.

```yaml
---
- name: example playbook
  hosts: all
  collections:
    - sample.assert_collection
  gather_facts: no
  tasks:
    - name: "Check existence of directories"
      assert_file:
        paths:
          - /root
          - /tmp
        state: directory
```
