#!/bin/bash
set -exf

function clean_repo() {
    # Since we are writting as root let fix the perms
    sudo chown -R $(id -u):$(id -g) ./ || :
}

function exit_it() {
    clean_repo
}

trap exit_it EXIT
run_tox() {
    only_for_python_targets=$2

    # Running tox, stop as soon as we get a failure
    for i in $(tox -l); do
        # NOTE(chmou): don't run the other tox targets if we just want to
        # validate the underlying DB and then run only the python unittests not
        # the pep8 and other target tox like that
        [[ -n $only_for_python_targets && ${i} != py* ]] && continue

        # NOTE(chmou): We do that cause py27 and py34 testrepository cache is not a
        # compatible format :-(
        rm -rf .testrepository
        echo -e "Running ${MAGENTA}$i${NC}"
        tox -e${i}
    done
}

run_tox

exit 0 # we don't have functional test yet


if [[ ! -d .tox/run_tests ]];then
    mkdir -p .tox
    virtualenv .tox/run_tests
fi

source .tox/run_tests/bin/activate
pip install -U fig

