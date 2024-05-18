# install latest diffusers
pip install diffusers==0.22.1 transformers

# install ip-adapter
pip install git+https://github.com/tencent-ailab/IP-Adapter.git

curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs

# download the models
cd IP-Adapter
git lfs install
git clone https://huggingface.co/h94/IP-Adapter
mv IP-Adapter/models models
mv IP-Adapter/sdxl_models sdxl_models