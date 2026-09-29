# os_security.py
import os
import stat

def main():
    secure_file = "secret_config.json"
    
    # ล้างไฟล์ read-only เดิมจากการรันครั้งก่อนหน้า (ถ้ามี)
    if os.path.exists(secure_file):
        os.chmod(secure_file, 0o666)
        os.remove(secure_file)
        
    # 1. สร้างไฟล์ตามปกติ
    with open(secure_file, "w") as f:
        f.write("{'api_key': '12345XYZ'}")
    print(f"Created {secure_file}.")
    
    # 2. ล็อกไฟล์ด้วย OS chmod (Change Mode)
    # 0o400 ในระบบฐานแปด: User อ่านได้ (4), Group (0) และ Others (0) ไม่มีสิทธิ์เข้าถึง
    print("Locking file permissions to Read-Only (00400)...")
    os.chmod(secure_file, 0o400)
    print(f"New Permissions: {stat.filemode(os.stat(secure_file).st_mode)}")
    
    # 3. พยายามเขียนทับไฟล์ด้วยเจตนาร้าย
    print("\nAttempting to overwrite the file...")
    try:
        with open(secure_file, "a") as f:
            f.write("\nMALICIOUS HACKER DATA")
        print("Success! Data written.")
    except PermissionError as e:
        print(f">>> [OS KERNEL BLOCKED] PermissionError: {e}")
        print(">>> The Operating System successfully protected the file!")

if __name__ == "__main__":
    main()