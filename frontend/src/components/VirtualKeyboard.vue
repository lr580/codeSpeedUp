<template>
  <div :class="keyboardClass"></div>
</template>

<script>
import Keyboard from "simple-keyboard";
import "simple-keyboard/build/css/index.css";

export default {
  name: "VirtualKeyboard",
  props: {
    keyboardClass: {
      default: "simple-keyboard",
      type: String
    },
    input: {
      type: String
    },
    layout: {
      type: Object,
      default: function() {
        return {
          'default': [
            '` 1 2 3 4 5 6 7 8 9 0 - = {bksp}',
            '{tab} q w e r t y u i o p [ ] \\',
            '{lock} a s d f g h j k l ; \' {enter}',
            '{shift} z x c v b n m , . / {shift}',
            '{ctrl} {win} {alt} {space} {alt} {win} {ctrl}'
          ]
        }
      }
    }
  },
  data() {
    return {
      keyboard: null
    };
  },
  mounted() {
    this.keyboard = new Keyboard(this.keyboardClass, {
      onChange: this.onChange,
      onKeyPress: this.onKeyPress,
      theme: "hg-theme-default hg-layout-default myTheme",
      layout: this.layout,
      display: {
        '{bksp}': "Backspace",
        '{lock}': "Caps Lock",
        '{enter}': "Enter", '{shift}' : "Shift",
        '{space}': "Space", '{tab}':'Tab', '{ctrl}': "Ctrl",'{alt}': "Alt",'{win}': "Win",
        '1': '1 !', '2': '2 @', '3': '3 #', '4': '4 $', '5': '5 %',
        '6': '6 ^', '7': '7 &', '8': '8 *', '9': '9 (', '0': '0 )',
        '-': '- _', '=': '= +',
        '[': '[ {', ']': '] }', '\\': '\\ |',
        ';': '; :', '\'': '\' "', ',': ', <', '.': '. >', '/': '/ ?',
        '`': '` ~',
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
        'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
        'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
        'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'
      },
      buttonTheme: this.blankButtonTheme()
    });
    // 使用 $nextTick 确保键盘实例完全初始化后再设置事件监听
    this.$nextTick(() => {
      this.attachPhysicalKeyboardEvents();
    });
  },
  methods: {
    blankButtonTheme() {
      return [
        { class: "highlight", buttons: " " },
        { class: "spacebar", buttons: "{space}" },
        { class: "small-btn", buttons: "{shift} {ctrl} {alt} {win} {tab} {lock} {bksp} {enter}" }
      ]
    },
    highlightedButtonTheme(button) {
      return [
        { class: "highlight", buttons: button },
        { class: "spacebar", buttons: "{space}" },
        { class: "small-btn", buttons: "{shift} {ctrl} {alt} {win} {tab} {lock} {bksp} {enter}" }
      ]
    },
    onChange(input) {
      this.$emit("onChange", input);
    },
    onKeyPress(button) {
      this.handleKeyPress(button); // 这里可能是你需要添加自定义逻辑的地方
      // 本程序不需要切换键盘的显示
      // if (button === "{shift}" || button === "{lock}") this.handleShift();
      this.$emit("onKeyPress", button);
    },
    handleKeyPress(button) {
      // 更新按键高亮
      this.keyboard.setOptions({
        buttonTheme: this.highlightedButtonTheme(button)
      });
      // Remove highlight after some time
      setTimeout(() => {
        this.keyboard.setOptions({
          buttonTheme: this.blankButtonTheme()
        });
      }, 200);
    },
    handleShift() { // 本程序不需要切换键盘的显示
      let currentLayout = this.keyboard.options.layoutName;
      let shiftToggle = currentLayout === "default" ? "default" : "default"; // 移除了 shift (否则?前是shift)

      this.keyboard.setOptions({
        layoutName: shiftToggle
      });
    },
    attachPhysicalKeyboardEvents() {
      document.addEventListener('keydown', (event) => {
        const keyMapping = this.mapPhysicalKeyToVirtual(event.code);
        if (keyMapping) {
          this.keyboard.handleButtonClicked(keyMapping);
          this.highlightKey(keyMapping);
        }
      });
    },
    mapPhysicalKeyToVirtual(code) {
      const mapping = {
        "KeyQ": "q", "KeyW": "w", "KeyE": "e", "KeyR": "r", "KeyT": "t", "KeyY": "y", "KeyU": "u", "KeyI": "i", "KeyO": "o", "KeyP": "p",
        "KeyA": "a", "KeyS": "s", "KeyD": "d", "KeyF": "f", "KeyG": "g", "KeyH": "h", "KeyJ": "j", "KeyK": "k", "KeyL": "l",
        "KeyZ": "z", "KeyX": "x", "KeyC": "c", "KeyV": "v", "KeyB": "b", "KeyN": "n", "KeyM": "m",
        "Digit1": "1", "Digit2": "2", "Digit3": "3", "Digit4": "4", "Digit5": "5", "Digit6": "6", "Digit7": "7", "Digit8": "8", "Digit9": "9", "Digit0": "0",
        "Space": "{space}", "Enter": "{enter}", "Backspace": "{bksp}", "ShiftLeft": "{shift}", "ShiftRight": "{shift}",
        "Minus": "-", "Equal": "=", "BracketLeft": "[", "BracketRight": "]", "Backslash": "\\",
        "Semicolon": ";", "Quote": "'", "Comma": ",", "Period": ".", "Slash": "/",
        "Tab": "{tab}", 
        "CapsLock": "{lock}", 
        "Escape": "{esc}", 
        "F1": "{f1}", "F2": "{f2}", "F3": "{f3}", "F4": "{f4}",
        "F5": "{f5}", "F6": "{f6}", "F7": "{f7}", "F8": "{f8}",
        "F9": "{f9}", "F10": "{f10}", "F11": "{f11}", "F12": "{f12}",
        "ScrollLock": "{scrolllock}", 
        "PauseBreak": "{pausebreak}",
        "Insert": "{ins}", "Delete": "{del}", "Home": "{home}", "End": "{end}",
        "PageUp": "{pageup}", "PageDown": "{pagedown}",
        "ArrowUp": "{up}", "ArrowDown": "{down}", "ArrowLeft": "{left}", "ArrowRight": "{right}",
        "NumLock": "{numlock}", "NumpadDivide": "/", "NumpadMultiply": "*", "NumpadSubtract": "-", 
        "NumpadAdd": "+", "NumpadEnter": "{enter}", "Numpad1": "1", "Numpad2": "2", "Numpad3": "3",
        "Numpad4": "4", "Numpad5": "5", "Numpad6": "6", "Numpad7": "7", "Numpad8": "8", 
        "Numpad9": "9", "Numpad0": "0", "NumpadDecimal": ".", "Backquote": "` ~",
        "ControlLeft": "{ctrl}", "ControlRight": "{ctrl}",
        "AltLeft": "{alt}", "AltRight": "{alt}",
        "MetaLeft": "{win}", "MetaRight": "{win}"
      };
      return mapping[code];
    },
    highlightKey(button) {
      // 更新按键高亮
      this.keyboard.setOptions({
        buttonTheme: this.highlightedButtonTheme(button)
      });
      setTimeout(() => {
        this.keyboard.setOptions({
          buttonTheme: this.blankButtonTheme()
        });
      }, 200);
    }
  },

  watch: {
    input(input) {
      this.keyboard.setInput(input);
    }
  }
};
</script>

<style>
.hg-theme-default .hg-button {
  transition: background-color 0.3s ease;
}

.highlight {
  background-color: #9ab !important; /* 使用 !important 确保覆盖默认样式 */
}

.hg-standardBtn, .hg-functionBtn {
  height: 2rem !important;
  font-size: 0.65rem;
}

.spacebar {
  width: 50%; /* 空格键占据50%的宽度 */
}

.small-btn {
  width: 6%; /* 其他控制键的宽度较小 */
}

</style>
