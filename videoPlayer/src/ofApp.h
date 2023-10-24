#pragma once

#include "ofMain.h"

class ofApp : public ofBaseApp{

	public:
		void setup();
		void update();
		void draw();

		void keyPressed(int key);
    void videoPlaying(ofVideoPlayer videoPlayer);
    
    ofVideoPlayer videoPlayer0, videoPlayer1, videoPlayer2, videoPlayer3, videoPlayer4,
                  videoPlayer5, videoPlayer6, videoPlayer7, videoPlayer8, videoPlayer9;
		
};
