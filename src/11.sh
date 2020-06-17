# 1.1.1.
curl -o ../d/file1.csv http://data.gov.ru/sites/default/files/opendata/7107542055-ioszpro/data-2015-03-11T00-00-00-structure-2015-03-11T00-00-00.csv

curl -o ../d/file2.zip https://www.huduser.gov/portal/datasets/hads/hads2013n_ASCII.zip

# 1.1.2.
unzip -o ../d/file2.zip -d ../d/

# 1.1.3.
tail -n 10 ../d/l1.log

# 1.1.4.
head -n 5 ../d/l1.log

# 1.1.5.
mkdir -p ../d/log/l1
cd ../d/log/l1/
split -l 50 ../../l1.log
cd ../../../src/

# 1.1.6.
wc -w ../d/l1.log

# 1.1.7.
wc -l ../d/l1.log

# 1.1.8.
awk -f csv-to-tree.awk ../d/tre.csv

# 1.1.9.
awk -f csv-to-tree.awk ../d/tre.csv | dot -Tjpg > ../d/graph.jpeg
