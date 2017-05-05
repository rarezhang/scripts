file="temp3_2016_04_14"
datapath="/disk01/pimadata/"
filepath="$datapath$file"
echo "importing file: $filepath"

echo "connecting to MongoDB..."
database="pima"
collection="tweets"
workers=6

mongoimport -d $database -c $collection --numInsertionWorkers $workers --file $filepath

