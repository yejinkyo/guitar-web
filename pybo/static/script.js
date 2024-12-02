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


