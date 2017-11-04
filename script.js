var player,
    time_update_interval = 0;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('video-placeholder', {
        width: 600,
        height: 400,
        videoId: 'WxlB1URFlEU',
        playerVars: {
            color: 'white',
            playlist: 'pf1t7cs9dkc',
	    cc_load_policy: 1
        },
        events: {
            onReady: initialize
        }
    });
}

function initialize(){
    skip_btn = document.getElementById('skip-button');
    skip_btn.onclick = skip;

    continue_btn = document.getElementById('continue-button');
    continue_btn.onclick = not_skip;
}

function show_video(){
    video_el = document.getElementById('video-placeholder');
    video_el.style.display='block';

    overlay_el = document.getElementById('popup');
    overlay_el.style.display='none';
}

function hide_video(){
    video_el = document.getElementById('video-placeholder');
    video_el.style.display = 'none';

    overlay_el = document.getElementById('popup');
    overlay_el.style.display = 'block';

}

function skip() {
    overlay_el = document.getElementById('overlay-on');
    overlay_el.text = 'false';
    answer = document.getElementById('query-answer');
    answer.text = 'skip';
    show_video();
}

function not_skip() {
    overlay_el = document.getElementById('overlay-on');
    overlay_el.text = 'false';
    answer = document.getElementById('query-answer');
    answer.text = 'continue';
    show_video();
}

function is_overlay_on() {
    overlay_el = document.getElementById('overlay-on');
    return overlay_el.text === 'false';
}

function get_answer_text() {
    answer_el = document.getElementById('query-answer');
    return answer_el.text;
}
