"""Unit tests for the Emotion Detection application."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion_detector function."""

    def test_joy_for_joyful_statement(self):
        """Test that joy is dominant for a joyful statement."""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_for_angry_statement(self):
        """Test that anger is dominant for an angry statement."""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_for_disgusting_statement(self):
        """Test that disgust is dominant for a disgusting statement."""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_for_sad_statement(self):
        """Test that sadness is dominant for a sad statement."""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_for_fearful_statement(self):
        """Test that fear is dominant for a fearful statement."""
        result = emotion_detector('I am really scared about this')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
