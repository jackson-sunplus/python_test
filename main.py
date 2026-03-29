def main(Language: str, AppID: str = "SG-AP-0001", UserType: str = "一般使用者") -> dict:
    # 修正：使用 None 而非 NULL，並且由於已有預設值，通常不需要這個檢查
    if (AppID is None)
        AppID = "SG-AP-0001"
    
    # 修正：宣告變數時需要賦值或使用 None
    UserRole: str = ""  # 初始化變數
    
    if UserType == "應用系統管理員33":
        UserRole = "SysManual"
    else:
        UserRole = "Manual"
    
    return {
        "Language": Language,
        "AppID": AppID,
        "UserRole": UserRole
    }