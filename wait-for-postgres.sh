#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD="django228" psql -h "$host" -d "zyfra_blog_db" -U "django_zyfra" -c '\q' 2>&1 >/dev/null; do
  >&2 echo "PostgresQL - sleeping"
  sleep 1
done

>&2 echo "PostgresQL - up"