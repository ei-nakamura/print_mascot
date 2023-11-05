class TerminalColor:
    """ ターミナル色変更用クラス """
 
    # 代表的な色
    INFO_BLUE = '\033[94m'
    INFO_GREEN = '\033[92m'
    WARN = '\033[93m'
    ERR = '\033[91m'
 
    # ソメイティ用色
    BLUE = '\033[94m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BLACK  = '\033[90m'
    WHITE = '\033[97m'
    CYAN =  '\033[96m'

    # フォントスタイル
    MARKER = '\033[7m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 
    # 末尾制御
    _END = '\033[0m'
 
    @classmethod
    def c_print(cls, text, styles=()):
        colored_text = ""
        for style in styles:
            colored_text += style
 
        colored_text += text
        colored_text += cls._END
        print(colored_text)
 