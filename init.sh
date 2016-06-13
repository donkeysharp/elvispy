#!/bin/bash
#
# Init virtualenv and installs dependencies
# Primary used libraries: fabric and jinja

ENVIRONMENT_NAME='env'

function _error() {
  if [[ $# -eq 0 ]]; then
    echo -e '\e[41m\e[97m[!] _error: One argument must be passed!\e[0m'
    exit
  fi
  echo -e '\e[41m\e[97m'$1'\e[0m'
}

function _print() {
  if [[ $# -eq 0 ]]; then
    _error '[!] _print: One argument must be passed!'
    exit
  fi
  echo -e '\e[32m'$1'\e[0m'
}

function check_virtualenv() {
  echo '[+] Checking virtualenv...'
  virtualenv_path=$(which virtualenv)
  if [[ -z $virtualenv_path ]]; then
    _error 'Virtualenv is not installed or not in your PATH, please install it using Python Pip'
    exit
  fi
  _print 'You have virtualenv '$(virtualenv --version)' installed'
  echo
}

function check_requirements() {
  echo '[+] Checking requirements.txt...'
  if [[ ! -f requirements.txt ]]; then
    _error "[!] requirements.txt file missing, dependencies will not be installed."
    exit
  fi
  _print 'requirements.txt found'
  echo
}

function init_environment() {
  echo '[+] Initializing virtualenv'
  echo
  virtualenv $ENVIRONMENT_NAME
  if [[ $? -ne 0 ]]; then
    _error '[!] Error creating virtual environment.'
    exit
  fi
  echo
  _print 'Virtual environment created successfully!'

  source $ENVIRONMENT_NAME'/bin/activate'

  echo
  echo '[+] Installing dependencies...'
  echo
  pip install -r requirements.txt

  echo
  _print 'Dependencies installed successfully!'
  echo '  In order to activate your environment execute "source env/bin/activate"'
  echo
}

check_virtualenv
check_requirements

init_environment

# if [[ $# -eq 0 ]]; then
# fi
