
target="*.html"
# if no arguments then build all html files
for file in ${target}
do
  filename=${file%%.*}
  cat templates/top.html ${filename}.html templates/bottom.html > docs/${filename}.html
  echo "${filename}.html created"

  sed -i "" "s/{{FILE_NAME}}/${filename}/g" docs/${filename}.html
  
  # Other possibility
  # grep -l 'FILE_NAME' docs/${filename}.html | xargs sed -i 's/FILE_NAME/test/g'
  
  open docs/${filename}.html
done
