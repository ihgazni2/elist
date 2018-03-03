pip3 uninstall elist
git rm -r dist
git rm -r build
git rm -r elist.egg-info
rm -r dist
rm -r build
rm -r elist.egg-info
git add .
git commit -m "remove old build"
#git push origin master
