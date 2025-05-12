let timerInterval; // タイマーのIDを保持する変数（setIntervalを管理）
let remainingTime = 0; // タイマーの初期値（秒数）
const initialTime = remainingTime; // 初期値を保持
let elapsedTime = 0;
let isBreakTime = false; // 現在休憩中かどうかを管理
const breakTime = 60 * 5; // 休憩時間は5分（秒単位）
let savedTime = 0;

// タイマーを表示する関数
function updateDisplay() {
  const minutes = Math.floor(remainingTime / 60);
  const seconds = remainingTime % 60;
  document.getElementById("timer").textContent = //これでtimerの数字を表示させる*/
    `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`; //padStart(2, "0") は数値を2桁に揃えます（例：5 → 05）。textContent を使用して、タイマーの数値をHTMLに反映
}

// 経過時間を表示する関数
function updateElapsedTimeDisplay() {
  const elapsedMinutes = Math.floor(elapsedTime / 60);
  const elapsedSeconds = elapsedTime % 60;
  document.getElementById("elapsed-time").textContent =
    `経過時間: ${String(elapsedMinutes).padStart(2, "0")}:${String(elapsedSeconds).padStart(2, "0")} 経過`;
}

// ページ読み込み時に初期表示
updateDisplay();
updateElapsedTimeDisplay();

// ここにクリックイベントを追加するコードを記述
document.getElementById("increase-minute").addEventListener("click", () => {
    remainingTime += 60;
    updateDisplay();
});

document.getElementById("decrease-minute").addEventListener("click", () => {
    remainingTime = Math.max(remainingTime - 60, 0);
    updateDisplay();
});

document.getElementById("increase-second").addEventListener("click", () => {
    remainingTime += 1;
    updateDisplay();
});

document.getElementById("decrease-second").addEventListener("click", () => {
    remainingTime = Math.max(remainingTime - 1, 0);
    updateDisplay();
});

// タイマーを開始する関数
let lastBreakElapsedTime = 0; // 最後に休憩に入った時点の経過時間

function startTimer() {
  if (timerInterval) return; // タイマーが既に動いている場合は二重開始を防ぐ

  // 作業中メッセージを表示
  document.getElementById("message").textContent = "作業中...";
  document.getElementById("message").style.display = "block"; // メッセージを表示

  timerInterval = setInterval(() => {
    if (remainingTime > 0) {
      remainingTime--; // 残り時間を減らす

      // 作業タイマー中のみ経過時間を増やす
      if (!isBreakTime) {
        elapsedTime++; // 作業タイマーが進むごとに経過時間を加算

        // 経過時間が10秒ごとで、前回の休憩から10秒経過している場合のみ休憩に入る
        if (elapsedTime % 10 === 0 && elapsedTime - lastBreakElapsedTime >= 10) {
          lastBreakElapsedTime = elapsedTime; // 最後の休憩時間を更新
          savedTime = remainingTime; // 現在の作業時間を保存
          isBreakTime = true;
          remainingTime = breakTime; // 休憩時間は5分に設定
          document.getElementById("message").textContent = "休憩！立ちあがろう!"; // 休憩メッセージを表示
        }
      }

      updateDisplay(); // 表示を更新
      updateElapsedTimeDisplay(); // 経過時間を更新
    } else {
      clearInterval(timerInterval); // タイマーを停止
      timerInterval = null;

      if (!isBreakTime) {
        // 作業タイマー終了時の処理
        document.getElementById("message").textContent = "お疲れ様でした！"; // 終了メッセージを表示
        document.getElementById("message").style.display = "block";
        document.getElementById("record-button").style.display = "inline-block"; // 記録ボタンを表示
      } else {
        // 休憩タイマー終了後、作業タイマーに戻る
        isBreakTime = false; // 休憩タイマー終了フラグをリセット
        remainingTime = savedTime; // 休憩前の作業時間を復元
        document.getElementById("message").style.display = "none"; // メッセージを非表示
        updateDisplay(); // タイマーを復元
        updateElapsedTimeDisplay(); // 経過時間を更新

        // 作業タイマーを再スタート
        startTimer(); // 再スタート
      }
    }
  }, 1000); // 1秒ごとに実行
}




// タイマーをリセットする関数
function resetTimer() {
  clearInterval(timerInterval); // タイマーを停止
  timerInterval = null; // タイマーIDをリセット
  isBreakTime = false; // 休憩タイマーも停止
  remainingTime = initialTime; // 残り時間を初期値に戻す
  elapsedTime = 0;
  updateDisplay(); // 表示を更新
  updateElapsedTimeDisplay(); // 経過時間の表示を更新
  document.getElementById("message").style.display = "none"; // メッセージを非表示
}

/* // リスタートする関数
function restartTimer() {
  clearInterval(timerInterval); // タイマーを完全に停止
  timerInterval = null; // タイマーIDをリセット
  isBreakTime = false; // 作業タイマーから再スタート
  remainingTime = initialTime; // 残り時間を初期値に戻す
  updateDisplay(); // 表示をリセット
  document.getElementById("message").style.display = "none"; // メッセージを非表示

  // ボタンを初期状態に戻す
  document.getElementById("start-button").style.display = "inline-block";
  document.getElementById("reset-button").style.display = "inline-block";
} */

// 経過時間を記録する関数
function recordTime() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const titleId = document.querySelector('select[name="title"]').value;

    if (!titleId) {
        alert("タイトルを選択してください");
        return;
    }

    const requestData = {
        elapsed_time: elapsedTime,
        title_id: titleId,
    };

    const clockUrl = document.getElementById('clock-url').dataset.url;

    // デバッグ用のログ
    console.log('Request URL:', clockUrl);
    console.log('CSRF Token:', csrfToken);
    console.log('Request Data:', requestData);

    fetch(clockUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(requestData),
        credentials: 'include'  // credentialsをincludeに変更
    })
    .then(response => {
        console.log('Response status:', response.status);  // レスポンスステータスをログ出力
        if (!response.ok) {
            return response.text().then(text => {  // JSONでなくテキストとして読み込む
                console.log('Error response:', text);  // エラーレスポンスの内容をログ出力
                throw new Error(text || `HTTP error! status: ${response.status}`);
            });
        }
        return response.json();
    })
    .then(data => {
        console.log('Success response:', data);  // 成功レスポンスをログ出力
        alert("時間が記録されました");
        resetTimer();
    })
    .catch(error => {
        console.error("記録エラー:", error);
        alert(`記録に失敗しました。エラー: ${error.message}`);
    });
}