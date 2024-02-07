#!/usr/bin/env bash

git push origin
[[ "`git remote | grep github`" != "" ]] && git push github || echo "No GitHub secondary repository found"
