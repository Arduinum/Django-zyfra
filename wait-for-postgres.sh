#!/bin/sh

set -e

host="$1"
name_db="$2"
user="$3"
shift
cmd="$@"

until PGPASSWORD="django228" psql -h "$host" -d "$name_db" -U "$user" -c '\q' 2>&1 >/dev/null; do
  >&2 echo "PostgresQL - sleeping"
  sleep 1
done

>&2 echo "PostgresQL - up"