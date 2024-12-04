// 페이지 로드 후 0.5초 후에 animate 클래스를 추가하여 중앙으로 이동 및 확대 효과 시작
setTimeout(() => {
    document.getElementById('guitarWrapper').classList.add('animate');
}, 500); // 0.5초 후 애니메이션 시작

// 오디오 파일 로드
const string1Sound = new Audio('/static/sounds/kickback.mp3'); // 오디오 파일 경로

// string1에 마우스를 올리면 소리 재생
document.getElementById('string1').addEventListener('mouseover', function() {
    string1Sound.currentTime = 0; // 소리 초기화
    string1Sound.play(); // 소리 재생
});

// string1에서 마우스를 떼면 소리 멈추기
document.getElementById('string1').addEventListener('mouseout', function() {
    string1Sound.pause(); // 소리 멈춤
    string1Sound.currentTime = 0; // 소리 초기화
});

document.addEventListener('click', function (event) {
    const statusInput = document.getElementById('status-input');
    const originalValue = statusInput.value;

    // 입력 필드 외부 클릭 시 상태 저장
    if (!statusInput.contains(event.target)) {
        const newValue = statusInput.value.trim();
        if (newValue !== originalValue) {
            fetch('/update_status', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ status: newValue })
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    alert(data.message);
                }
            })
            .catch(error => console.error('Error updating status:', error));
        }
    }
});


