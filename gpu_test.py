import subprocess

def check_gpu():
    print("--- Starting GPU Architecture Test ---")
    try:
        # Running nvidia-smi command from python
        result = subprocess.check_output(["nvidia-smi"], encoding='utf-8')
        print("Success! Your RTX 5080 is visible to Python:")
        print(result)
    except Exception as e:
        print(f"Error: GPU not detected. {e}")

if __name__ == "__main__":
    check_gpu()
