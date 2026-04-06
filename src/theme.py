APP_CSS = """
<style>
    :root {
        --bg-main: #05010a;
        --bg-panel: rgba(20, 8, 24, 0.88);
        --bg-soft: rgba(255, 255, 255, 0.05);
        --line: rgba(255, 82, 130, 0.24);
        --text-main: #fff4f8;
        --text-soft: #f3b8c9;
        --red: #ff315c;
        --pink: #ff4fd8;
        --hot: #ff7aa8;
        --glow: 0 0 32px rgba(255, 79, 216, 0.22);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(255, 49, 92, 0.18), transparent 28%),
            radial-gradient(circle at top right, rgba(255, 79, 216, 0.15), transparent 24%),
            linear-gradient(180deg, #09020f 0%, #040107 100%);
        color: var(--text-main);
        font-family: "Segoe UI Variable Display", "Bahnschrift", "Segoe UI", sans-serif;
    }

    html {
        scroll-behavior: smooth;
    }

    body,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stSidebar"] > div:first-child {
        scroll-behavior: smooth;
        overscroll-behavior-y: contain;
    }

    * {
        scrollbar-width: thin;
        scrollbar-color: rgba(255, 79, 216, 0.55) rgba(255, 255, 255, 0.05);
    }

    *::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    *::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 999px;
    }

    *::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, rgba(255, 49, 92, 0.85), rgba(255, 79, 216, 0.85));
        border-radius: 999px;
        border: 2px solid rgba(13, 4, 17, 0.55);
    }

    *::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, rgba(255, 101, 142, 0.95), rgba(255, 107, 225, 0.95));
    }

    #MainMenu,
    header[data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        display: none !important;
    }

    [data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, rgba(28, 7, 20, 0.98), rgba(11, 3, 14, 0.98));
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"][aria-expanded="true"] {
        min-width: 21rem;
        max-width: 21rem;
    }

    [data-testid="stSidebar"][aria-expanded="false"] {
        min-width: 0;
        max-width: 0;
        background: transparent;
        border-right: none;
        box-shadow: none;
        overflow: hidden;
    }

    [data-testid="stSidebar"] > div:first-child {
        background:
            radial-gradient(circle at top, rgba(255, 79, 216, 0.08), transparent 22%),
            linear-gradient(180deg, rgba(28, 7, 20, 0.98), rgba(11, 3, 14, 0.98));
    }

    [data-testid="stSidebar"] * {
        color: var(--text-main) !important;
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        background: transparent;
    }

    [data-testid="collapsedControl"] {
        display: none;
    }

    .control-panel {
        margin-bottom: 1rem;
        padding: 1rem 1rem 0.9rem;
        border-radius: 24px;
        border: 1px solid rgba(255, 96, 154, 0.2);
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02)),
            rgba(23, 7, 21, 0.9);
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.04),
            0 18px 36px rgba(255, 49, 92, 0.12);
    }

    .control-kicker {
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.18rem;
        text-transform: uppercase;
        color: #ff87b5;
        margin-bottom: 0.4rem;
    }

    .control-title {
        font-size: 1.5rem;
        font-weight: 900;
        line-height: 1;
        text-transform: uppercase;
        font-family: "Arial Black", "Bahnschrift SemiBold", sans-serif;
        background: linear-gradient(90deg, #ffffff 0%, #ff88b8 45%, #ff53d6 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent !important;
        margin-bottom: 0.5rem;
    }

    .control-copy {
        font-size: 0.92rem;
        color: var(--text-soft);
        line-height: 1.45;
        margin-bottom: 0.2rem;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
        scroll-padding-top: 1.2rem;
        content-visibility: auto;
        contain-intrinsic-size: 1px 1200px;
        transform: translateZ(0);
    }

    .hero-shell {
        position: relative;
        overflow: hidden;
        padding: 2rem;
        border: 1px solid var(--line);
        border-radius: 28px;
        background:
            linear-gradient(145deg, rgba(255, 49, 92, 0.16), rgba(255, 79, 216, 0.08)),
            rgba(18, 6, 20, 0.88);
        box-shadow: var(--glow);
        margin-bottom: 1.25rem;
    }

    .hero-shell::after {
        content: "";
        position: absolute;
        inset: auto -10% -60% auto;
        width: 240px;
        height: 240px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(255, 79, 216, 0.22), transparent 68%);
    }

    .eyebrow {
        letter-spacing: 0.24rem;
        text-transform: uppercase;
        color: var(--hot);
        font-size: 0.76rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }

    .hero-title {
        margin: 0;
        line-height: 0.95;
        font-size: clamp(2.3rem, 5vw, 4.6rem);
        font-weight: 900;
        text-transform: uppercase;
        font-family: "Arial Black", "Bahnschrift SemiBold", sans-serif;
        color: var(--text-main);
        text-shadow: 0 0 24px rgba(255, 79, 216, 0.25);
    }

    .hero-title .accent {
        display: inline-block;
        background: linear-gradient(90deg, #ff5a5f 0%, #ff55a3 52%, #ffa6cf 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }

    .hero-copy {
        max-width: 760px;
        color: var(--text-soft);
        font-size: 1rem;
        margin-top: 1rem;
        margin-bottom: 0;
    }

    .section-label {
        margin-top: 1.2rem;
        margin-bottom: 0.6rem;
        font-size: 1.05rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.08rem;
        color: #ffd6e4;
    }

    .stButton > button {
        min-height: 3rem;
        border-radius: 16px;
        border: 1px solid rgba(255, 96, 154, 0.24);
        background:
            linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02)),
            rgba(18, 10, 24, 0.92);
        color: var(--text-main);
        font-weight: 800;
        letter-spacing: 0.04rem;
        text-transform: uppercase;
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.04),
            0 10px 24px rgba(255, 49, 92, 0.08);
        transition:
            transform 0.18s ease,
            border-color 0.18s ease,
            box-shadow 0.18s ease,
            background 0.18s ease;
    }

    .stButton > button:hover {
        border-color: rgba(255, 79, 216, 0.45);
        background:
            linear-gradient(180deg, rgba(255,255,255,0.09), rgba(255,255,255,0.03)),
            rgba(26, 12, 30, 0.96);
        box-shadow:
            0 0 0 1px rgba(255, 79, 216, 0.14),
            0 16px 32px rgba(255, 49, 92, 0.14);
        transform: translateY(-1px);
    }

    .stButton > button:focus {
        outline: none;
        border-color: rgba(255, 79, 216, 0.5);
        box-shadow:
            0 0 0 2px rgba(255, 79, 216, 0.16),
            0 14px 30px rgba(255, 49, 92, 0.12);
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, rgba(255, 49, 92, 0.92), rgba(255, 79, 216, 0.92));
        border-color: rgba(255, 151, 191, 0.34);
        box-shadow:
            0 0 0 1px rgba(255,255,255,0.04) inset,
            0 16px 32px rgba(255, 49, 92, 0.2);
    }

    .stButton > button:disabled {
        opacity: 0.48;
        border-color: rgba(255,255,255,0.08);
        background: rgba(255,255,255,0.03);
        box-shadow: none;
        transform: none;
        cursor: not-allowed;
    }

    .spotlight-meta {
        margin-bottom: 0.95rem;
        color: #f1b7ca;
        font-size: 0.92rem;
        font-weight: 700;
        letter-spacing: 0.02rem;
    }

    .update-panel {
        margin-top: 1.4rem;
        padding: 1rem 1.1rem;
        border-radius: 22px;
        border: 1px solid rgba(255, 96, 154, 0.2);
        background:
            linear-gradient(145deg, rgba(255, 49, 92, 0.12), rgba(255, 79, 216, 0.06)),
            rgba(17, 8, 18, 0.88);
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.03),
            0 16px 30px rgba(255, 49, 92, 0.08);
    }

    .update-kicker {
        color: #ff9abe;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.16rem;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }

    .update-copy {
        color: #ffe9f1;
        font-size: 0.98rem;
        line-height: 1.5;
        margin: 0;
    }

    .stMetric {
        border: 1px solid var(--line);
        border-radius: 22px;
        background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
        padding: 0.9rem;
        box-shadow: var(--glow);
    }

    .stMetric label,
    .stMetric [data-testid="stMetricLabel"] {
        color: var(--text-soft) !important;
        text-transform: uppercase;
        letter-spacing: 0.08rem;
    }

    .stMetric [data-testid="stMetricValue"] {
        color: var(--text-main);
    }

    .stSelectbox label,
    .stTextInput label,
    .stMultiSelect label,
    .stSlider label {
        color: var(--text-main) !important;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06rem;
        font-size: 0.77rem;
    }

    .stSelectbox [data-baseweb="select"] > div,
    .stMultiSelect [data-baseweb="select"] > div,
    .stTextInput > div > div > input {
        border-radius: 16px !important;
        border: 1px solid rgba(255, 99, 155, 0.22) !important;
        background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02)) !important;
        box-shadow: 0 10px 24px rgba(255, 49, 92, 0.08);
        transition: all 0.18s ease;
    }

    .stTextInput > div > div > input {
        color: var(--text-main) !important;
        padding-left: 0.95rem;
    }

    .stTextInput > div > div > input::placeholder {
        color: #d991af !important;
    }

    .stSelectbox [data-baseweb="select"] > div:hover,
    .stMultiSelect [data-baseweb="select"] > div:hover,
    .stTextInput > div > div > input:hover,
    .stSelectbox [data-baseweb="select"] > div:focus-within,
    .stMultiSelect [data-baseweb="select"] > div:focus-within,
    .stTextInput > div > div > input:focus {
        border-color: rgba(255, 79, 216, 0.55) !important;
        box-shadow:
            0 0 0 1px rgba(255, 79, 216, 0.18),
            0 0 24px rgba(255, 79, 216, 0.16);
    }

    [data-baseweb="tag"] {
        border-radius: 999px !important;
        border: 1px solid rgba(255, 119, 165, 0.26) !important;
        background: linear-gradient(90deg, rgba(255,49,92,0.18), rgba(255,79,216,0.18)) !important;
        color: #fff3f7 !important;
        font-weight: 700;
    }

    [data-baseweb="select"] input {
        color: var(--text-main) !important;
    }

    .stSlider [data-baseweb="slider"] [role="slider"] {
        background: linear-gradient(180deg, #ffd8e7, #ff78ad) !important;
        border: 2px solid rgba(255,255,255,0.75) !important;
        box-shadow: 0 0 0 6px rgba(255, 79, 216, 0.14);
    }

    .stSlider [data-baseweb="slider"] > div > div {
        background: linear-gradient(90deg, rgba(255, 49, 92, 0.2), rgba(255, 79, 216, 0.16)) !important;
        border-radius: 999px;
        height: 0.4rem !important;
    }

    .stSlider [data-baseweb="slider"] > div > div > div {
        background: linear-gradient(90deg, #ff315c, #ff4fd8) !important;
        border-radius: 999px;
        height: 0.4rem !important;
    }

    .stSlider [data-testid="stTickBar"] {
        color: #e6a1bc !important;
    }

    .stCaption {
        color: #efb4c8 !important;
    }

    .stDataFrame, .st-emotion-cache-1wivap2 {
        border-radius: 20px;
        overflow: hidden;
        scroll-behavior: smooth;
        will-change: scroll-position;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stSidebar"] > div:first-child {
        will-change: scroll-position;
        transform: translateZ(0);
        -webkit-overflow-scrolling: touch;
    }

    @media (max-width: 900px) {
        .block-container {
            padding-top: 1.2rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-shell {
            padding: 1.3rem;
            border-radius: 22px;
        }
    }

</style>
<script>
    (() => {
        if (window.__cwqSmoothScrollInit) return;
        window.__cwqSmoothScrollInit = true;

        const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        if (prefersReducedMotion) return;

        const selectors = [
            '[data-testid="stAppViewContainer"]',
            '[data-testid="stSidebar"] > div:first-child'
        ];

        const stateMap = new WeakMap();

        function getState(element) {
            if (!stateMap.has(element)) {
                stateMap.set(element, {
                    target: element.scrollTop,
                    current: element.scrollTop,
                    frame: null
                });
            }
            return stateMap.get(element);
        }

        function animate(element) {
            const state = getState(element);
            state.current += (state.target - state.current) * 0.14;

            if (Math.abs(state.target - state.current) < 0.5) {
                state.current = state.target;
                element.scrollTop = state.current;
                state.frame = null;
                return;
            }

            element.scrollTop = state.current;
            state.frame = window.requestAnimationFrame(() => animate(element));
        }

        function bindSmoothWheel(element, key) {
            if (!element || element.dataset.smoothWheelBound === "true") return;
            element.dataset.smoothWheelBound = "true";

            const saved = window.sessionStorage.getItem(key);
            if (saved !== null) {
                const y = Number(saved);
                if (!Number.isNaN(y)) {
                    element.scrollTop = y;
                    const state = getState(element);
                    state.current = y;
                    state.target = y;
                }
            }

            element.addEventListener("scroll", () => {
                window.sessionStorage.setItem(key, String(element.scrollTop));
            }, { passive: true });

            element.addEventListener("wheel", (event) => {
                if (event.ctrlKey || Math.abs(event.deltaX) > Math.abs(event.deltaY)) return;
                if (element.scrollHeight <= element.clientHeight) return;

                event.preventDefault();
                const state = getState(element);
                const maxScroll = element.scrollHeight - element.clientHeight;
                const delta = event.deltaY * 0.95;
                state.target = Math.max(0, Math.min(maxScroll, state.target + delta));

                if (!state.frame) {
                    state.frame = window.requestAnimationFrame(() => animate(element));
                }
            }, { passive: false });
        }

        function init() {
            selectors.forEach((selector, index) => {
                const element = document.querySelector(selector);
                bindSmoothWheel(element, `cwq-scroll-${index}`);
            });
        }

        const observer = new MutationObserver(() => init());
        observer.observe(document.body, { childList: true, subtree: true });
        window.addEventListener("load", init, { once: true });
        init();
    })();
</script>
"""
