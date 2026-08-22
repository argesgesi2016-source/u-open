<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0,
               viewport-fit=cover">

<title>For You ❤️</title>

<style>

/* =====================================================
   RESET
===================================================== */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

html,
body {
    width: 100%;
    height: 100%;
}

body {
    overflow: hidden;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Arial,
        sans-serif;

    color: white;

    background:
        radial-gradient(
            circle at 50% 0%,
            #5d147a 0%,
            #27082f 45%,
            #08000c 100%
        );
}


/* =====================================================
   SCREEN SYSTEM
===================================================== */

.screen {

    position: fixed;

    inset: 0;

    width: 100%;
    height: 100%;

    height: 100dvh;

    display: none;

    align-items: center;
    justify-content: center;

    flex-direction: column;

    text-align: center;

    padding:
        max(25px, env(safe-area-inset-top))
        max(20px, env(safe-area-inset-right))
        max(25px, env(safe-area-inset-bottom))
        max(20px, env(safe-area-inset-left));

    overflow-y: auto;
    overflow-x: hidden;

    animation: screenIn .8s ease;
}

.screen.active {
    display: flex;
}

@keyframes screenIn {

    from {
        opacity: 0;
        transform: scale(.94);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}


/* =====================================================
   TEXT
===================================================== */

h1 {

    width: 100%;
    max-width: 900px;

    font-size:
        clamp(2rem, 8vw, 5rem);

    line-height: 1.1;

    margin-bottom: 20px;
}

p {

    width: 100%;
    max-width: 700px;

    font-size:
        clamp(1rem, 4vw, 1.4rem);

    line-height: 1.6;
}


/* =====================================================
   SCREEN 1 — HEART
===================================================== */

.heart-container {

    position: relative;

    width: min(230px, 60vw);
    height: min(210px, 55vw);

    margin-bottom: 30px;

    animation: heartbeat 1.15s infinite;
}

.heart {

    position: absolute;

    width: 68%;
    height: 68%;

    left: 16%;
    top: 17%;

    background: #ff1744;

    transform: rotate(-45deg);

    box-shadow:
        0 0 25px #ff1744,
        0 0 60px rgba(255,23,68,.8);
}

.heart::before,
.heart::after {

    content: "";

    position: absolute;

    width: 100%;
    height: 100%;

    background: #ff1744;

    border-radius: 50%;
}

.heart::before {

    top: -50%;
    left: 0;
}

.heart::after {

    left: 50%;
    top: 0;
}

.letter {

    position: absolute;

    z-index: 5;

    left: 50%;
    top: 50%;

    transform: translate(-50%, -50%);

    font-size:
        clamp(4rem, 19vw, 7rem);

    font-weight: 900;

    color: white;

    text-shadow:
        0 0 10px white,
        0 0 25px white;
}

.love-text {

    font-size:
        clamp(2rem, 9vw, 4.5rem);

    font-weight: 900;

    animation: glow 1.5s infinite alternate;
}

@keyframes heartbeat {

    0%,
    100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.1);
    }
}

@keyframes glow {

    from {
        text-shadow:
            0 0 10px white;
    }

    to {
        text-shadow:
            0 0 25px #ff4081,
            0 0 55px #ff1744;
    }
}


/* =====================================================
   SCREEN 2 — NEVER GIVE UP
===================================================== */

.never {

    width: 100%;
    max-width: 1000px;

    font-size:
        clamp(1.8rem, 7vw, 5rem);

    font-weight: 900;

    line-height: 1.15;

    word-wrap: break-word;
}

.never span {

    display: inline-block;

    animation: crazy 1.4s infinite;
}

@keyframes crazy {

    0% {
        transform:
            translateY(0)
            rotate(0);
    }

    20% {
        transform:
            translateY(-25px)
            rotate(10deg);
    }

    40% {
        transform:
            translateY(10px)
            rotate(-10deg);
    }

    60% {
        transform:
            translateY(-18px)
            rotate(12deg);
    }

    80% {
        transform:
            translateY(5px)
            rotate(-6deg);
    }

    100% {
        transform:
            translateY(0)
            rotate(0);
    }
}


/* =====================================================
   SCREEN 3 — WEDNESDAY
===================================================== */

.date-card {

    width: min(90vw, 520px);

    margin: 10px 0;

    padding: 20px;

    border: 2px solid #ff4081;

    border-radius: 24px;

    background:
        rgba(255,255,255,.08);

    box-shadow:
        0 0 30px rgba(255,64,129,.35);

    animation:
        floating 3s ease-in-out infinite;
}

.date {

    font-size:
        clamp(1.2rem, 5vw, 1.8rem);

    font-weight: 700;
}

.wednesday {

    margin-top: 8px;

    color: #ff80ab;

    font-size:
        clamp(1.3rem, 5vw, 2rem);

    font-weight: 900;
}

@keyframes floating {

    50% {
        transform:
            translateY(-9px);
    }
}


/* =====================================================
   CAT
===================================================== */

.cat {

    font-size:
        clamp(70px, 20vw, 120px);

    margin-bottom: 15px;

    animation:
        catBounce 1s infinite alternate;
}

@keyframes catBounce {

    from {
        transform:
            translateY(0)
            rotate(-3deg);
    }

    to {
        transform:
            translateY(-15px)
            rotate(3deg);
    }
}


/* =====================================================
   BUTTONS
===================================================== */

button {

    border: none;

    cursor: pointer;

    font-family: inherit;

    font-size:
        clamp(1rem, 4vw, 1.2rem);

    font-weight: 700;

    min-height: 52px;

    padding: 15px 28px;

    border-radius: 50px;

    touch-action: manipulation;

    transition:
        transform .25s ease,
        left .25s ease,
        top .25s ease;
}

button:active {
    transform: scale(.95);
}


/* YES */

.yes {

    background: #ff4081;

    color: white;

    box-shadow:
        0 0 25px #ff4081;
}

.yes:hover {

    transform:
        scale(1.1);
}


/* =====================================================
   YES / NO
===================================================== */

.buttons {

    position: relative;

    width: min(500px, 90vw);

    height: 190px;

    margin-top: 25px;
}

.no {

    position: absolute;

    left: 55%;
    top: 55%;

    background: #555;

    color: white;

    white-space: nowrap;

    transition:
        left .22s ease,
        top .22s ease,
        transform .22s ease;
}


/* =====================================================
   ACTIVITY
===================================================== */

.choice-container {

    width: 100%;
    max-width: 700px;

    display: flex;

    justify-content: center;

    align-items: center;

    flex-wrap: wrap;

    gap: 15px;

    margin-top: 25px;
}

.choice {

    background:
        rgba(255,255,255,.08);

    color: white;

    border:
        2px solid #ff4081;

    min-width: 160px;
}

.choice.selected {

    background: #ff4081;

    transform:
        scale(1.07);

    box-shadow:
        0 0 25px #ff4081;
}

.confirm {

    margin-top: 25px;

    background: #ff4081;

    color: white;

    box-shadow:
        0 0 25px rgba(255,64,129,.6);
}


/* =====================================================
   SELECTS
===================================================== */

select {

    width: min(90vw, 350px);

    min-height: 55px;

    margin: 8px;

    padding: 12px 18px;

    border:
        2px solid #ff4081;

    border-radius: 15px;

    background: #25072f;

    color: white;

    font-size: 16px;

    outline: none;
}


/* =====================================================
   FINAL
===================================================== */

.final-title {

    font-size:
        clamp(2.3rem, 9vw, 6rem);

    animation:
        finalGlow 1.5s infinite alternate;
}

@keyframes finalGlow {

    from {

        transform:
            scale(1);

        text-shadow:
            0 0 10px #ff4081;
    }

    to {

        transform:
            scale(1.05);

        text-shadow:
            0 0 30px #ff1744,
            0 0 70px #ff4081;
    }
}

.instagram {

    width: min(90vw, 450px);

    margin-top: 30px;

    padding: 16px 25px;

    border-radius: 25px;

    background:
        linear-gradient(
            45deg,
            #833ab4,
            #fd1d1d,
            #fcb045
        );

    font-size:
        clamp(.95rem, 4vw, 1.15rem);

    line-height: 1.5;
}


/* =====================================================
   HEART RAIN
===================================================== */

.heart-rain {

    position: fixed;

    inset: 0;

    overflow: hidden;

    pointer-events: none;

    z-index: 1;
}

.falling-heart {

    position: absolute;

    top: -50px;

    animation:
        fall linear forwards;
}

@keyframes fall {

    to {

        transform:
            translateY(110vh)
            rotate(360deg);

        opacity: 0;
    }
}


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 480px) {

    .screen {

        padding-left: 15px;
        padding-right: 15px;
    }

    .never {

        font-size:
            clamp(1.7rem, 8vw, 3rem);
    }

    .date-card {

        padding: 16px;
    }

    .choice-container {

        flex-direction: column;
    }

    .choice {

        width: min(85vw, 300px);
    }

    .buttons {

        width: 92vw;
        height: 200px;
    }
}


/* =====================================================
   LANDSCAPE PHONE
===================================================== */

@media
(max-height: 550px)
and (orientation: landscape) {

    .screen {

        justify-content:
            flex-start;

        padding-top: 15px;
        padding-bottom: 15px;
    }

    .heart-container {

        transform:
            scale(.65);

        margin-bottom:
            -20px;
    }

    .cat {

        font-size: 60px;
    }
}

</style>
</head>


<body>


<!-- =====================================================
     1 — L HEART
===================================================== -->

<section
    class="screen active"
    id="screen1">

    <div class="heart-container">

        <div class="heart"></div>

        <div class="letter">
            L
        </div>

    </div>

    <div class="love-text">
        I LOVE YOU ❤️
    </div>

    <p style="margin-top:15px;">
        Especially the 12th letter of the alphabet.
    </p>

</section>


<!-- =====================================================
     2 — NEVER GIVE UP
===================================================== -->

<section
    class="screen"
    id="screen2">

    <h1>
        Wait...
    </h1>

    <div
        class="never"
        id="neverText">
    </div>

    <p
        id="neverSub"
        style="margin-top:25px;">
    </p>

</section>


<!-- =====================================================
     3 — WEDNESDAY
===================================================== -->

<section
    class="screen"
    id="screen3">

    <h1>
        Maybe this was meant to happen... ✨
    </h1>

    <div class="date-card">

        <div class="date">
            11 July 2007
        </div>

        <div class="wednesday">
            WEDNESDAY
        </div>

    </div>

    <div class="date-card">

        <div class="date">
            21 February 2007
        </div>

        <div class="wednesday">
            WEDNESDAY
        </div>

    </div>

    <p style="margin-top:20px;">

        Two completely different dates...

        <br>

        but both landed on a Wednesday.

        <br><br>

        <strong>
            It's meant to be. ❤️
        </strong>

    </p>

</section>


<!-- =====================================================
     4 — DATE QUESTION
===================================================== -->

<section
    class="screen"
    id="screen4">

    <div class="cat">
        🐱
    </div>

    <h1>
        So...
    </h1>

    <p>
        Will you go on a date with me? ❤️
    </p>

    <div class="buttons">

        <button
            class="yes"
            onclick="yesClicked()">

            YES ❤️

        </button>

        <button
            class="no"
            id="noButton">

            NO 😭

        </button>

    </div>

</section>


<!-- =====================================================
     5 — WHAT TO DO
===================================================== -->

<section
    class="screen"
    id="screen5">

    <h1>
        YAY! ❤️
    </h1>

    <p>
        What would you like to do?
    </p>

    <div class="choice-container">

        <button
            class="choice"
            onclick="
                selectChoice(
                    this,
                    'Kafeing ☕'
                )
            ">

            ☕ Kafeing

        </button>

        <button
            class="choice"
            onclick="
                selectChoice(
                    this,
                    'Dinner 🍝'
                )
            ">

            🍝 Dinner

        </button>

        <button
            class="choice"
            onclick="
                selectChoice(
                    this,
                    'Meet somewhere 📍'
                )
            ">

            📍 Meet somewhere

        </button>

    </div>

    <p
        id="choiceText"
        style="margin-top:25px;">
    </p>

    <button
        class="confirm"
        onclick="showDateScreen()">

        Continue ❤️

    </button>

</section>


<!-- =====================================================
     6 — DATE AND TIME
===================================================== -->

<section
    class="screen"
    id="screen6">

    <h1>
        Pick a day ❤️
    </h1>

    <p>
        Choose a day from August 23rd to 30th.
    </p>

    <select id="daySelect">

        <option value="">
            Choose a day
        </option>

        <option value="August 23">
            August 23
        </option>

        <option value="August 24">
            August 24
        </option>

        <option value="August 25">
            August 25
        </option>

        <option value="August 26">
            August 26
        </option>

        <option value="August 27">
            August 27
        </option>

        <option value="August 28">
            August 28
        </option>

        <option value="August 29">
            August 29
        </option>

        <option value="August 30">
            August 30
        </option>

    </select>


    <h1 style="margin-top:25px;">

        What time? ⏰

    </h1>

    <p>
        Choose a time from 5:00 PM to 7:30 PM.
    </p>

    <select id="timeSelect">

        <option value="">
            Choose a time
        </option>

        <option value="5:00 PM">
            5:00 PM
        </option>

        <option value="5:30 PM">
            5:30 PM
        </option>

        <option value="6:00 PM">
            6:00 PM
        </option>

        <option value="6:30 PM">
            6:30 PM
        </option>

        <option value="7:00 PM">
            7:00 PM
        </option>

        <option value="7:30 PM">
            7:30 PM
        </option>

    </select>

    <button
        class="confirm"
        onclick="finishDate()">

        Confirm ❤️

    </button>

</section>


<!-- =====================================================
     7 — FINAL
===================================================== -->

<section
    class="screen"
    id="screen7">

    <div
        class="heart-rain"
        id="heartRain">
    </div>

    <div
        style="
        position:relative;
        z-index:2;
        width:100%;
        display:flex;
        align-items:center;
        flex-direction:column;
        ">

        <div class="cat">
            🐱❤️
        </div>

        <h1 class="final-title">
            YAY I'M SO HAPPY! ❤️
        </h1>

        <p style="margin-top:25px;">
            This is something you will never regret.
        </p>

        <p style="margin-top:15px;">
            I can't wait. 🥹❤️
        </p>

        <div class="instagram">

            For more information:

            <br>

            Text me on Instagram

            <br>

            <strong>
                @argesmulaj
            </strong>

        </div>

    </div>

</section>



<script>

/* =====================================================
   SCREEN NAVIGATION
===================================================== */

let currentScreen = 1;


/*
   This function is now the ONLY way
   screens change.
*/

function showScreen(number) {

    document
        .querySelectorAll(".screen")
        .forEach(screen => {

            screen.classList.remove("active");

        });

    const target =
        document.getElementById(
            "screen" + number
        );

    if (target) {

        target.classList.add("active");

        currentScreen = number;

    }
}


/* =====================================================
   SCREEN 1
===================================================== */


/*
   Heart stays for 3.5 seconds.
*/

setTimeout(() => {

    showScreen(2);

    startNeverAnimation();

}, 3500);


/* =====================================================
   SCREEN 2
===================================================== */

function startNeverAnimation() {

    const text =
        "I WILL NEVER GIVE UP ON YOU ❤️";

    const element =
        document.getElementById(
            "neverText"
        );

    element.innerHTML = "";

    [...text].forEach(
        (letter, index) => {

            const span =
                document.createElement(
                    "span"
                );

            span.innerText =
                letter === " "
                    ? "\u00A0"
                    : letter;

            span.style.animationDelay =
                (index * .07) + "s";

            element.appendChild(span);

        }
    );


    document.getElementById(
        "neverSub"
    ).innerText =
        "No matter what. No matter how crazy this gets. ❤️";


    /*
       SCREEN 2 lasts exactly 5 seconds
       AFTER it appears.
    */

    setTimeout(() => {

        showScreen(3);

        startWednesdayScreen();

    }, 5000);

}


/* =====================================================
   SCREEN 3
===================================================== */

function startWednesdayScreen() {

    /*
       The Wednesday screen stays visible
       for 7 seconds.
    */

    setTimeout(() => {

        showScreen(4);

        startDateQuestion();

    }, 7000);

}


/* =====================================================
   SCREEN 4
===================================================== */

function startDateQuestion() {

    /*
       Reset the NO button every time
       the screen opens.
    */

    noScale = 1;

    noButton.style.left = "55%";
    noButton.style.top = "55%";
    noButton.style.transform = "scale(1)";

}


/* =====================================================
   NO BUTTON
===================================================== */

const noButton =
    document.getElementById(
        "noButton"
    );

let noScale = 1;


/*
   Move the button somewhere random.
*/

function moveNoButton(event) {

    if (event) {

        event.preventDefault();

    }

    const area =
        document.querySelector(
            ".buttons"
        );

    const areaWidth =
        area.clientWidth;

    const areaHeight =
        area.clientHeight;

    const buttonWidth =
        noButton.offsetWidth;

    const buttonHeight =
        noButton.offsetHeight;


    const maxX =
        Math.max(
            5,
            areaWidth - buttonWidth
        );

    const maxY =
        Math.max(
            5,
            areaHeight - buttonHeight
        );


    const x =
        Math.random() * maxX;

    const y =
        Math.random() * maxY;


    noButton.style.left =
        x + "px";

    noButton.style.top =
        y + "px";


    /*
       Every time they try to touch
       NO, it gets smaller.
    */

    noScale *= .80;

    if (noScale < .12) {

        noScale = .12;

    }

    noButton.style.transform =
        "scale(" + noScale + ")";
}


/*
   LAPTOP / DESKTOP
*/

noButton.addEventListener(
    "mouseenter",
    moveNoButton
);


/*
   PHONE / TABLET
*/

noButton.addEventListener(
    "touchstart",
    moveNoButton,
    {
        passive: false
    }
);


/*
   If someone actually manages
   to click it, it still escapes.
*/

noButton.addEventListener(
    "click",
    moveNoButton
);


/* =====================================================
   YES BUTTON
===================================================== */

function yesClicked() {

    showScreen(5);

}


/* =====================================================
   ACTIVITY
===================================================== */

let selectedChoice = "";


function selectChoice(
    button,
    choice
) {

    document
        .querySelectorAll(".choice")
        .forEach(btn => {

            btn.classList.remove(
                "selected"
            );

        });


    button.classList.add(
        "selected"
    );


    selectedChoice =
        choice;


    document.getElementById(
        "choiceText"
    ).innerText =
        "Perfect choice: " +
        choice +
        " ❤️";

}


/* =====================================================
   CONTINUE TO DATE
===================================================== */

function showDateScreen() {

    if (!selectedChoice) {

        alert(
            "Pick what you want to do first ❤️"
        );

        return;

    }

    showScreen(6);

}


/* =====================================================
   FINAL DATE SELECTION
===================================================== */

function finishDate() {

    const day =
        document.getElementById(
            "daySelect"
        ).value;

    const time =
        document.getElementById(
            "timeSelect"
        ).value;


    if (!day || !time) {

        alert(
            "Pick both a day and a time ❤️"
        );

        return;

    }


    /*
       Everything has been selected.
       Show the final screen.
    */

    showScreen(7);

    createHeartRain();


    /*
       Optional:
       Save the selected date locally.
       This doesn't send anything anywhere.
    */

    localStorage.setItem(
        "dateChoice",
        day
    );

    localStorage.setItem(
        "timeChoice",
        time
    );

    localStorage.setItem(
        "activityChoice",
        selectedChoice
    );

}


/* =====================================================
   HEART RAIN
===================================================== */

function createHeartRain() {

    const container =
        document.getElementById(
            "heartRain"
        );


    /*
       Prevent multiple rain timers.
    */

    if (
        container.dataset.started
        === "true"
    ) {

        return;

    }

    container.dataset.started =
        "true";


    setInterval(() => {

        const heart =
            document.createElement(
                "div"
            );


        heart.className =
            "falling-heart";


        const hearts = [
            "❤️",
            "💖",
            "💕",
            "💗",
            "💘",
            "💝"
        ];


        heart.innerText =
            hearts[
                Math.floor(
                    Math.random()
                    * hearts.length
                )
            ];


        heart.style.left =
            Math.random() * 100
            + "%";


        heart.style.fontSize =
            (
                15 +
                Math.random() * 30
            )
            + "px";


        heart.style.animationDuration =
            (
                3 +
                Math.random() * 4
            )
            + "s";


        container.appendChild(
            heart
        );


        setTimeout(() => {

            heart.remove();

        }, 7500);


    }, 180);

}

</script>

</body>
</html>