#
## 内容
docker exec -it 7c67d7e81e371af5e718a0837fef69aaec7ef6b66ca2e63e401360707791330a bash
cd opt/contest/ABC414
python3 ABC414A.py
python3 ABC414C.py < C_input.txt
python3 ABC414B.py < B_input.txt