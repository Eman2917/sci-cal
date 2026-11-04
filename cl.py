
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

# Hide Streamlit default UI
st.markdown("""
<style>
#MainMenu, footer, header {
    visibility: hidden;
}

.stApp {
    background: linear-gradient(
        135deg,
        #D5D9DE,
        #AEB6BF
    );
}
</style>
""", unsafe_allow_html=True)


calculator_code = """
<div id="wrapper">

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', system-ui;
}

#wrapper {
    display: flex;
    justify-content: center;
    padding: 10px;
    background: #D5D9DE;
}

/* CALCULATOR BODY */

.calc {
    width: 380px;
    background: linear-gradient(145deg, #E1E4E7, #BFC5CB);
    border: 2px solid #929BA3;
    border-radius: 25px;
    padding: 22px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.30);
}

/* LCD DISPLAY */

.display {
    background: #101820;
    border-radius: 14px;
    padding: 20px 18px;
    min-height: 115px;
    text-align: right;
    margin-bottom: 18px;
    border: 3px solid #343A40;
    box-shadow: inset 0 3px 10px rgba(0,0,0,0.5);
}

.expr {
    color: #AAB8C2;
    font-size: 19px;
    min-height: 24px;
    word-break: break-all;
    letter-spacing: 0.5px;
}

.res {
    color: #FFFFFF;
    font-size: 42px;
    font-weight: 800;
    min-height: 48px;
    word-break: break-all;
    margin-top: 6px;
}

.hint {
    color: #343A40;
    font-size: 11px;
    text-align: center;
    margin-bottom: 12px;
    letter-spacing: 1px;
    font-weight: 700;
}

/* BUTTON GRID */

.grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
}

button {
    height: 58px;
    border: 1px solid #252B30;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.15s;
    outline: none;
    box-shadow: 0 3px 4px rgba(0,0,0,0.18);
}

button:active {
    transform: scale(0.92);
    filter: brightness(0.85);
}

/* NUMBER BUTTONS */

.num {
    background: linear-gradient(#F7F8F9, #D9DEE3);
    color: #202830;
}

.num:hover {
    background: #FFFFFF;
}

/* ORANGE OPERATORS */

.op {
    background: linear-gradient(#F3A04E, #D97820);
    color: #FFFFFF;
    font-size: 22px;
}

.op:hover {
    background: #C76515;
}

/* BLUE SCIENTIFIC BUTTONS */

.sci {
    background: linear-gradient(#438CC5, #21659D);
    color: #FFFFFF;
    font-size: 15px;
}

.sci:hover {
    background: #164F80;
}

/* EQUAL BUTTON */

.eq {
    background: linear-gradient(#F3A04E, #D97820);
    color: white;
    grid-column: span 2;
    font-size: 26px;
}

.eq:hover {
    background: #C76515;
}

/* AC AND DELETE */

.ac {
    background: linear-gradient(#555D65, #343A40);
    color: white;
}

.ac:hover {
    background: #252B30;
}

/* MODE BUTTON */

.mode-btn {
    width: 100%;
    height: 38px;
    background: #343A40;
    color: #FFFFFF;
    border: 1.5px solid #202830;
    border-radius: 10px;
    font-size: 13px;
    margin-bottom: 14px;
    font-weight: 700;
}

.mode-btn:hover {
    background: #21659D;
}

</style>


<div class="calc">

    <!-- DISPLAY -->

    <div class="display">
        <div class="expr" id="expr"></div>
        <div class="res" id="res">0</div>
    </div>

    <div class="hint" id="mode">
        DEG MODE • KEYBOARD ACTIVE ⌨️
    </div>

    <button class="mode-btn" onclick="toggleMode()">
        SWITCH TO RAD / DEG
    </button>


    <!-- SCIENTIFIC KEYPAD -->

    <div class="grid">

        <button class="sci" onclick="add('sin(')">sin</button>
        <button class="sci" onclick="add('cos(')">cos</button>
        <button class="sci" onclick="add('tan(')">tan</button>
        <button class="sci" onclick="add('log(')">log</button>
        <button class="sci" onclick="add('ln(')">ln</button>

        <button class="sci" onclick="add('sqrt(')">√</button>
        <button class="sci" onclick="add('**2')">x²</button>
        <button class="sci" onclick="add('**3')">x³</button>
        <button class="sci" onclick="add('^')">xʸ</button>
        <button class="sci" onclick="add('!')">x!</button>

        <button class="sci" onclick="add('π')">π</button>
        <button class="sci" onclick="add('e')">e</button>
        <button class="num" onclick="add('(')">(</button>
        <button class="num" onclick="add(')')">)</button>
        <button class="ac" onclick="del()">DEL</button>

        <button class="num" onclick="add('7')">7</button>
        <button class="num" onclick="add('8')">8</button>
        <button class="num" onclick="add('9')">9</button>
        <button class="op" onclick="add('/')">÷</button>
        <button class="ac" onclick="clearAll()">AC</button>

        <button class="num" onclick="add('4')">4</button>
        <button class="num" onclick="add('5')">5</button>
        <button class="num" onclick="add('6')">6</button>
        <button class="op" onclick="add('*')">×</button>
        <button class="num" onclick="add('%')">%</button>

        <button class="num" onclick="add('1')">1</button>
        <button class="num" onclick="add('2')">2</button>
        <button class="num" onclick="add('3')">3</button>
        <button class="op" onclick="add('-')">−</button>
        <button class="op" onclick="add('+')">+</button>

        <button class="num" onclick="add('0')">0</button>
        <button class="num" onclick="add('.')">.</button>
        <button class="eq" onclick="calc()">=</button>

    </div>

</div>


<script>

let expr = "";
let isDeg = true;

const exprEl = document.getElementById('expr');
const resEl = document.getElementById('res');
const modeEl = document.getElementById('mode');


function update() {
    exprEl.innerText = expr || "";

    if (expr === "") {
        resEl.innerText = "0";
    }
}


function add(v) {

    if (v === 'π') {
        expr += 'Math.PI';
    }

    else if (v === 'e') {
        expr += 'Math.E';
    }

    else {
        expr += v;
    }

    update();
}


function clearAll() {
    expr = "";
    resEl.innerText = "0";
    update();
}


function del() {
    expr = expr.slice(0, -1);
    update();
}


function toggleMode() {

    isDeg = !isDeg;

    modeEl.innerText =
        (isDeg ? "DEG" : "RAD") +
        " MODE • KEYBOARD ACTIVE ⌨️";
}


function factorial(n) {

    if (n < 0 || !Number.isInteger(n)) {
        throw new Error("Invalid factorial");
    }

    if (n > 170) {
        throw new Error("Number too large");
    }

    let r = 1;

    for (let i = 2; i <= n; i++) {
        r *= i;
    }

    return r;
}


function calc() {

    try {

        if (!expr.trim()) return;

        let e = expr.replace(/\^/g, '**');

        // Scientific functions

        e = e.replace(/sqrt\(/g, 'Math.sqrt(');
        e = e.replace(/log\(/g, 'Math.log10(');
        e = e.replace(/ln\(/g, 'Math.log(');

        // Trigonometric functions

        e = e.replace(
            /sin\(/g,
            isDeg ? '(Math.sin(Math.PI/180*' : '(Math.sin('
        );

        e = e.replace(
            /cos\(/g,
            isDeg ? '(Math.cos(Math.PI/180*' : '(Math.cos('
        );

        e = e.replace(
            /tan\(/g,
            isDeg ? '(Math.tan(Math.PI/180*' : '(Math.tan('
        );

        // Factorial

        e = e.replace(
            /(\d+(?:\.\d+)?)!/g,
            'factorial($1)'
        );

        // Evaluate expression

        let result = Function(
            'factorial',
            '"use strict"; return (' + e + ')'
        )(factorial);

        if (
            typeof result !== 'number' ||
            !Number.isFinite(result)
        ) {
            throw new Error("Invalid calculation");
        }

        result = parseFloat(result.toFixed(10));

        resEl.innerText = result;

        expr = String(result);

        exprEl.innerText = "";

    }

    catch(error) {

        resEl.innerText = "Error";

    }

}


// KEYBOARD SUPPORT

document.addEventListener('keydown', (ev) => {

    const k = ev.key;

    if (
        (k >= '0' && k <= '9') ||
        ['+', '-', '*', '/', '(', ')', '.', '%', '^'].includes(k)
    ) {

        add(k);
        ev.preventDefault();

    }

    else if (k === 'Enter' || k === '=') {

        calc();
        ev.preventDefault();

    }

    else if (k === 'Backspace') {

        del();
        ev.preventDefault();

    }

    else if (k === 'Escape') {

        clearAll();

    }

});


update();

</script>

</div>
"""

# Render calculator
components.html(calculator_code, height=780, scrolling=False)


# FOOTER
st.markdown("""
<div style="
    background:#E8EBEE;
    padding:16px;
    border-radius:15px;
    text-align:center;
    margin-top:10px;
    box-shadow:0 5px 15px rgba(0,0,0,0.12);
    color:#343A40;
">

<b>SCIENTIFIC CALCULATOR</b><br>

<span style="font-size:13px;">

⌨️ <b>Keyboard:</b> Type and press Enter &nbsp;|&nbsp;

🖥️ <b>Display:</b> Black LCD &nbsp;|&nbsp;

🎨 <b>Theme:</b> Casio Classic &nbsp;|&nbsp;

⚙️ <b>Functions:</b> Scientific calculations

</span>

<br><br>

<span style="color:#64748b;font-size:12px;">
Built with Python and Streamlit
</span>

</div>
""", unsafe_allow_html=True)
