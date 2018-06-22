BEATNAME=burrowbeat
BEAT_DIR=github.com/goomzee
SYSTEM_TESTS=false
TEST_ENVIRONMENT=false
ES_BEATS?=${GOPATH}/src/github.com/elastic/beats
# if using glide to manage vendor dependencies:
#GOPACKAGES=$(shell glide novendor)
# else:
GOPACKAGES=$(shell go list ${BEAT_DIR}/... | grep -v /vendor/)
PREFIX?=.

# Path to the libbeat Makefile
-include $(ES_BEATS)/libbeat/scripts/Makefile

# Initial beat setup
.PHONY: setup
setup:
	make update

.PHONY: git-init
git-init:
	git init
	git add README.md CONTRIBUTING.md
	git commit -m "Initial commit"
	git add LICENSE
	git commit -m "Add the LICENSE"
	git add .gitignore
	git commit -m "Add git settings"
	git add .
	git reset -- .travis.yml
	git commit -m "Add burrowbeat"
	git add .travis.yml
	git commit -m "Add Travis CI"

# This is called by the beats packer before building starts
.PHONY: before-build
before-build:

# Collects all dependencies and then calls update
.PHONY: collect
collect:
