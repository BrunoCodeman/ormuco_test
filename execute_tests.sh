declare -a tests=('a' 'b' 'c');

for fn in "${tests[@]}"
do
    printf "\nexecuting tests for question ${fn}\n";
    cd "question_${fn}"
    python -m unittest test.py 
    cd ..
done