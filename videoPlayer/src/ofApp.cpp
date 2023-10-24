#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    
    string filePath_0 = "/Users/zhichengu/Desktop/0.mp4";
    if (videoPlayer0.load(filePath_0)) {
//        videoPlayer0.play();
    }
    
    string filePath_1 = "/Users/zhichengu/Desktop/1.mp4";
    if (videoPlayer1.load(filePath_1)) {
//        videoPlayer1.play();
    }

    string filePath_2 = "/Users/zhichengu/Desktop/2.mp4";
    if (videoPlayer2.load(filePath_2)) {
//        videoPlayer2.play();
    }

    string filePath_3 = "/Users/zhichengu/Desktop/3.mp4";
    if (videoPlayer3.load(filePath_3)) {
//        videoPlayer3.play();
    }

    string filePath_4 = "/Users/zhichengu/Desktop/4.mp4";
    if (videoPlayer4.load(filePath_4)) {
//        videoPlayer4.play();
    }

    string filePath_5 = "/Users/zhichengu/Desktop/5.mp4";
    if (videoPlayer5.load(filePath_5)) {
//        videoPlayer5.play();
    }

    string filePath_6 = "/Users/zhichengu/Desktop/6.mp4";
    if (videoPlayer6.load(filePath_6)) {
//        videoPlayer6.play();
    }

    string filePath_7 = "/Users/zhichengu/Desktop/7.mp4";
    if (videoPlayer7.load(filePath_7)) {
//        videoPlayer7.play();
    }

    string filePath_8 = "/Users/zhichengu/Desktop/8.mp4";
    if (videoPlayer8.load(filePath_8)) {
//        videoPlayer8.play();
    }

    string filePath_9 = "/Users/zhichengu/Desktop/9.mp4";
    if (videoPlayer9.load(filePath_9)) {
//        videoPlayer9.play();
    }

}

//--------------------------------------------------------------
void ofApp::update(){
    videoPlayer0.update();
    videoPlayer1.update();
    videoPlayer2.update();
    videoPlayer3.update();
    videoPlayer4.update();
    videoPlayer5.update();
    videoPlayer6.update();
    videoPlayer7.update();
    videoPlayer8.update();
    videoPlayer9.update();
}

//--------------------------------------------------------------
void ofApp::draw(){
    ofBackground(0);
    
    videoPlaying(videoPlayer3);
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    if (key == 'f' || key == 'F') {
        ofToggleFullscreen();
    }
}

//--------------------------------------------------------------
void ofApp::videoPlaying(ofVideoPlayer videoPlayer){
    videoPlayer.play();
    
    ofPushMatrix();
    ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
    ofRotateDeg(270);
    int modifyY = (1920 - 1080)/2;
    ofSetColor(255);
    videoPlayer.draw(-ofGetWidth()/4 - 60, -ofGetHeight()/2 - modifyY, 1080, 1920);
    ofPopMatrix();
}
