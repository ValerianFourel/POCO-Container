# Starting the script
echo "Downloading Source Code"
cd ..
git clone https://github.com/saidwivedi/POCO.git
cd POCO
conda create -n poco python=3.8
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge
pip install -r requirements.txt

####

echo "Downloading the Data"
mkdir data
mv ../POCO-Container/getPoco.py ./data/getPoco.py
cd data

python getPoco.py