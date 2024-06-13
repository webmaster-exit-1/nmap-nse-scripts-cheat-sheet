import subprocess
import re

def run_nmap(nse_script, target, parameters):
    command = f"nmap --script={nse_script} {parameters} {target}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"Error: {error}")
    else:
        print(output)

def load_nse_scripts(file_path):
    nse_scripts = {}
    with open(file_path, 'r') as f:
        content = f.read()

    # Matches the script name and parameters
    matches = re.findall(r'(\w+.nse)\n\n```bash\n(nmap .+?)\n```', content, re.DOTALL)

    for match in matches:
        script, command = match
        parameters = command.replace('nmap ', '').replace('<target>', '').replace(f'--script {script}', '').strip()
        nse_scripts[script] = parameters

    return nse_scripts

def main():
    nse_scripts = load_nse_scripts('path_to_your_cheat_sheet')

    print("Please choose an NSE script:")
    for i, script in enumerate(nse_scripts.keys(), start=1):
        print(f"{i}. {script}")

    choice = int(input("Enter your choice: "))
    target = input("Enter the target: ")

    chosen_script = list(nse_scripts.keys())[choice-1]
    run_nmap(chosen_script, target, nse_scripts[chosen_script])

if __name__ == "__main__":
    main()