#!/bin/bash

# 날짜 범위: 2024년 12월 4일부터 12월 31일까지
for day in {4..31}; do
  # 날짜 포맷 만들기 (예: 2024-12-04)
  date="2024-12-$(printf "%02d" $day)"

  # 날짜를 커밋 메시지로 사용하여 커밋 만들기
  GIT_COMMITTER_DATE="$date 12:00:00" git commit --allow-empty --date "$date 12:00:00" --author="Hwan seok Kim <kcsss4499@gmail.com>" -m "Update contributions for December $day, 2024"
done