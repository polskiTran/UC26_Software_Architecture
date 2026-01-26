# [Assignment 1](https://github.com/lunarlunarll123/Arch_Assignment01)

## Prerequisite
- Make sure `git` and `java` is installed and in `PATH`
```shell
git --version
java -version
```

## Download code maat SCM tool
- Download `.jar` if not found in `assignment1/tools/`
```shell
cd assignment1/tools/
curl -L -O https://github.com/adamtornhill/code-maat/releases/download/v1.0.4/code-maat-1.0.4-standalone.jar
```

- Invoke maat tool to check if it's working
```shell
java -jar code-maat-1.0.4-standalone.jar -l log.txt -c git -a summary
```
## Download `cloc` tool
- Check if `cloc`  is installed
```shell
cloc --version
```
- Install `cloc`
```shell
sudo apt update
sudo apt install cloc
```

## Clone the repo to be analyzed 
- We are choosing `vLLM` for this project
```shell
cd assignment1/
git clone https://github.com/vllm-project/vllm.git
cd vllm/
```

- Consider the last 12 months as period our case study
```shell
git checkout `git rev-list -n 1 --before="2026-01-26" main`
```

## Generate analysis
- generate log file for maat code tool
```shell
cd vllm/
git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat --before=2026-01-26 > vllm_evo.log
mv vllm_evo.log /workspaces/UC26_Software_Architecture/assignment1/logs
```
- run the log file through maat tool
```shell
cd assignment1/

# summary
java -jar tools/code-maat-1.0.4-standalone.jar -l logs/vllm_evo.log -c git -a summary 

# revisions/effort
java -jar tools/code-maat-1.0.4-standalone.jar -l logs/vllm_evo.log -c git -a revisions > logs/vllm_freqs.csv 
```
    - Make sure in `vllm_freqs.csv` there's nothing before `entity,n-revs` so that it's a correct csv file

- cloc tool
```shell
cd vllm/

# summary 
cloc . 

# complexity 
cloc ./ --unix --by-file --csv --quiet --report-file=logs/vllm_lines.csv 
```

- Merge the data
```shell
cd assignment1/
python scripts_4/merge_comp_freqs.py logs/vllm_freqs.csv logs/vllm_lines.csv > logs/results.csv
```

## Python notebook analysis report
- Install `uv`
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Install the dependencies
```shell
uv sync
```

- Install the kernel for ipynb
```shell
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=SoftwareArchitecture_assignment1
```

- In the ipynb file selct the `SoftwareArchitecture_assignment1` kernel from selct kernel button
    - Need the jupyter extention on vscode installed
    - Also might need to close and open the ipynb file or delete `.venv` file and reran the above command to see the desire kernel