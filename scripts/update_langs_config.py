

template = {
  "en": {
    "ver": 1,
    "displayName": "English"
  },
  "fr": {
    "ver": 1,
    "displayName": "French/Français"
  },
  "id": {
    "ver": 1,
    "displayName": "Indonesian"
  },
  "hi": {
    "ver": 1,
    "displayName": "Hindi/हिन्दी",
    "src": "https://rawcdn.githack.com/zappol/acu/$COMMIT/langs/hi.zip"
  },
  "es": {
    "ver": 2,
    "displayName": "Spanish/Español",
    "src": "https://rawcdn.githack.com/zappol/acu/$COMMIT/langs/es.zip"
  },
  "ko":{
	"ver": 1,
	"displayName": "Korean/한국어"
  },
  "ta":{
    "ver": 1,
    "displayName": "Tamil/தமிழ்",
    "src": "https://rawcdn.githack.com/zappol/acu/$COMMIT/langs/ta.zip"
  },
  "pt":{
    "ver": 1,
    "displayName": "Portuguese/Português",
    "src": "https://rawcdn.githack.com/zappol/acu/$COMMIT/langs/pt.zip"
  },
  "ru":{
    "displayName": "Russian/"
  }
}

import os, json

def get_config_file():
    return os.path.relpath( os.path.join(__file__, "../../langs/config.json"))

def main(ver: int, commit_id: str):
  src_template = 'https://rawcdn.githack.com/zappol/acu/{}/langs/{}.zip'

  for i in template:
      print(i)
      template[i]['ver'] = ver
      template[i]['src'] = src_template.format(commit_id, i)
      print (template.get(i))
    
  with open(get_config_file(), 'w', encoding='utf-8') as f:
    c =  json.dumps(template, ensure_ascii=False, indent=2) #.encode('utf8') 
    # json.dump(template, f, ensure_ascii=False)
    print(c)
    f.write(c)

import sys

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('usage: python me.py [ver] [commit-id]')
    exit

  main(sys.argv[1], sys.argv[2])
  print(os.getcwd())
  print(os.path.realpath(__file__))
  script_path=os.path.realpath(__file__)
  print(os.path.relpath( os.path.join(script_path, "../../langs")))
