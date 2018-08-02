#! /usr/bin/env bash

git clone https://github.com/kewlfft/ansible-aur.git ~/.ansible/plugins/modules/aur
ansible-playbook -i hosts playbook.yml
