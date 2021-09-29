# django_backend

# Installation
  1. 가상환경 생성
  ```
  python -m venv virtualenv
  ```
  2. 패키지 다운
  ```
  pip install -r requirements.txt
  ```
# Database
## Postgresql 사용

```
1. CREATE DATABASE <데이터베이스 이름>;
2. CREATE USER <유저 이름> WITH PASSWORD <패스워드>;
3. ALTER ROLE <유저이름> SET client_encoding TO 'utf8';
   ALTER ROLE <유저이름> SET default_transaction_isolation TO 'read committed'; 
   ALTER ROLE <유저이름> SET TIME ZONE 'Asia/Seoul';
4. GRANT ALL PRIVILEGES ON DATABASE <이터베이스 이름> To <유저 이름>;

```
