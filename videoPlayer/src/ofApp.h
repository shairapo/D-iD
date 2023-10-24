#pragma once

#include "ofMain.h"
#include "ofxOsc.h"

#define HOST "192.168.1.72"
#define PORT 9999

class ofApp : public ofBaseApp{

	public:
		void setup();
		void update();
		void draw();

		void keyPressed(int key);

    void video(ofVideoPlayer videoPlayer);
    
    ofVideoPlayer videoPlayer0, videoPlayer1, videoPlayer2, videoPlayer3, videoPlayer4,
                  videoPlayer5, videoPlayer6, videoPlayer7, videoPlayer8, videoPlayer9;

	ofxOscReceiver receiver;
	int number;
		
};
