#! /bin/bash
hugo
git add -A
git commit -a -m "wy-cs site update $(date --date='%Y-%m-%d %H:%M')"
git push -u gh-pages master
