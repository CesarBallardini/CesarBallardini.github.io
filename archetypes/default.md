+++
date = '{{ time.Now.Format .params.dateFormat }}'
draft = false
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
+++
