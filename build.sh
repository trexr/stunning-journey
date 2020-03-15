
target="*.html"
# if no arguments then build all html files
for file in ${target}
do

  filename=${file%%.*}
  cat templates/top.html ${filename}.html templates/bottom.html > docs/${filename}.html

  pagename=${filename}
  if [ ${filename} = "index" ]; then 
   pagename="home"
  fi;

  # Adds name of page to parent div
  sed -i "" "s/{{FILE_NAME}}/${pagename}/g" docs/${filename}.html
  
  # Set active nav links
  activelink=${pagename}-link
  sed -i "" "s/${activelink}/${activelink} active/g" docs/${filename}.html

  # Log in cli 
  echo "${filename}.html created"
  
  # Other possibility
  # grep -l 'FILE_NAME' docs/${filename}.html | xargs sed -i 's/FILE_NAME/test/g'
  # open docs/${filename}.html
done
