import tweepy
import time
import logging
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import requests
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('social_media_agent.log', encoding='utf-8'),
        logging.StreamHandler()
    ],
    encoding='utf-8'
)

@dataclass
class PostResult:
    """Data class to store post results"""
    success: bool
    post_id: Optional[str]
    post_url: Optional[str]
    error_message: Optional[str]
    timestamp: str

class SocialMediaAgent:
    """AI Agent for automating social media posts on X (Twitter)"""
    
    def __init__(self, api_key: str, api_secret: str, access_token: str, access_token_secret: str):
        """
        Initialize the social media agent with API credentials
        
        Args:
            api_key: X API key
            api_secret: X API secret
            access_token: X access token
            access_token_secret: X access token secret
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.api = None
        self.client = None
        self.logger = logging.getLogger(__name__)
        
    def authenticate(self) -> bool:
        """
        Authenticate with X API
        
        Returns:
            bool: True if authentication successful, False otherwise
        """
        try:
          
            auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
            auth.set_access_token(self.access_token, self.access_token_secret)
            self.api = tweepy.API(auth, wait_on_rate_limit=True)
            
            
            self.client = tweepy.Client(
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
                wait_on_rate_limit=True
            )
            
            
            user = self.client.get_me()
            if user.data:
                self.logger.info(f"Authentication successful for user: {user.data.username}")
                return True
            else:
                self.logger.error("Authentication failed - no user data returned")
                return False
                
        except Exception as e:
            self.logger.error(f"Authentication failed: {str(e)}")
            return False
    
    def create_post(self, content: str, media_paths: List[str] = None) -> PostResult:
        """
        Create a post on X
        
        Args:
            content: Text content of the post
            media_paths: List of file paths for media attachments
            
        Returns:
            PostResult: Result of the post creation
        """
        timestamp = datetime.now().isoformat()
        
        try:
            self.logger.info(f"Step 1: Preparing to create post with content: '{content[:50]}...'")
            
         
            if len(content) > 280:
                self.logger.warning(f"Content length ({len(content)}) exceeds 280 characters, truncating...")
                content = content[:277] + "..."
            
            
            media_ids = []
            if media_paths:
                self.logger.info(f"Step 2: Processing {len(media_paths)} media files")
                media_ids = self._upload_media(media_paths)
                if not media_ids and media_paths:
                    self.logger.warning("Media upload failed, posting without media")
            
            # Create the post
            self.logger.info("Step 3: Creating post on X...")
            
            if media_ids:
                response = self.client.create_tweet(text=content, media_ids=media_ids)
            else:
                response = self.client.create_tweet(text=content)
            
            if response.data:
                post_id = response.data['id']
                post_url = f"https://twitter.com/i/web/status/{post_id}"
                
                self.logger.info(f"Step 4: Post created successfully with ID: {post_id}")
                
                
                verification_result = self._verify_post(post_id)
                
                return PostResult(
                    success=True,
                    post_id=post_id,
                    post_url=post_url,
                    error_message=None,
                    timestamp=timestamp
                )
            else:
                self.logger.error("Post creation failed - no response data")
                return PostResult(
                    success=False,
                    post_id=None,
                    post_url=None,
                    error_message="No response data from API",
                    timestamp=timestamp
                )
                
        except tweepy.TooManyRequests:
            error_msg = "Rate limit exceeded. Please wait before posting again."
            self.logger.error(error_msg)
            return PostResult(False, None, None, error_msg, timestamp)
            
        except tweepy.Forbidden:
            error_msg = "Access forbidden. Check your API permissions."
            self.logger.error(error_msg)
            return PostResult(False, None, None, error_msg, timestamp)
            
        except Exception as e:
            error_msg = f"Post creation failed: {str(e)}"
            self.logger.error(error_msg)
            return PostResult(False, None, None, error_msg, timestamp)
    
    def _upload_media(self, media_paths: List[str]) -> List[str]:
        """
        Upload media files to X
        
        Args:
            media_paths: List of file paths to upload
            
        Returns:
            List of media IDs
        """
        media_ids = []
        
        for path in media_paths:
            try:
                if not os.path.exists(path):
                    self.logger.warning(f"Media file not found: {path}")
                    continue
                    
                self.logger.info(f"Uploading media: {path}")
                media = self.api.media_upload(path)
                media_ids.append(media.media_id)
                self.logger.info(f"Media uploaded successfully: {media.media_id}")
                
            except Exception as e:
                self.logger.error(f"Failed to upload media {path}: {str(e)}")
                
        return media_ids
    
    def _verify_post(self, post_id: str) -> bool:
        """
        Verify that a post was successfully created
        
        Args:
            post_id: ID of the post to verify
            
        Returns:
            bool: True if post exists, False otherwise
        """
        try:
            self.logger.info(f"Step 5: Verifying post with ID: {post_id}")
            
 
            time.sleep(2)
            
    
            tweet = self.client.get_tweet(post_id)
            
            if tweet.data:
                self.logger.info(f"Step 6: Post verification successful! Post exists and is accessible")
                self.logger.info(f"Post content: '{tweet.data.text[:50]}...'")
                return True
            else:
                self.logger.error("Post verification failed - post not found")
                return False
                
        except Exception as e:
            self.logger.error(f"Post verification failed: {str(e)}")
            return False
    
    def schedule_post(self, content: str, delay_minutes: int, media_paths: List[str] = None) -> PostResult:
        """
        Schedule a post to be published after a delay
        
        Args:
            content: Post content
            delay_minutes: Minutes to wait before posting
            media_paths: Optional media files
            
        Returns:
            PostResult: Result of the scheduled post
        """
        self.logger.info(f"Scheduling post for {delay_minutes} minutes from now")
        
      
        time.sleep(delay_minutes * 60)
        
       
        return self.create_post(content, media_paths)
    
    def bulk_post(self, posts: List[Dict], delay_between_posts: int = 5) -> List[PostResult]:
        """
        Create multiple posts with delays between them
        
        Args:
            posts: List of dictionaries with 'content' and optional 'media_paths'
            delay_between_posts: Minutes to wait between posts
            
        Returns:
            List of PostResult objects
        """
        results = []
        
        for i, post_data in enumerate(posts):
            self.logger.info(f"Creating post {i+1} of {len(posts)}")
            
            content = post_data.get('content', '')
            media_paths = post_data.get('media_paths', [])
            
            result = self.create_post(content, media_paths)
            results.append(result)
            
          
            if i < len(posts) - 1:
                self.logger.info(f"Waiting {delay_between_posts} minutes before next post...")
                time.sleep(delay_between_posts * 60)
        
        return results
    
    def get_post_analytics(self, post_id: str) -> Dict:
        """
        Get analytics for a specific post
        
        Args:
            post_id: ID of the post
            
        Returns:
            Dictionary with post analytics
        """
        try:
            tweet = self.client.get_tweet(
                post_id, 
                tweet_fields=['public_metrics', 'created_at', 'author_id']
            )
            
            if tweet.data:
                return {
                    'post_id': post_id,
                    'created_at': tweet.data.created_at,
                    'retweet_count': tweet.data.public_metrics.get('retweet_count', 0),
                    'like_count': tweet.data.public_metrics.get('like_count', 0),
                    'reply_count': tweet.data.public_metrics.get('reply_count', 0),
                    'quote_count': tweet.data.public_metrics.get('quote_count', 0)
                }
            else:
                return {'error': 'Post not found'}
                
        except Exception as e:
            return {'error': str(e)}

def main():
    """Demonstration of the AI Social Media Agent"""
    
    # Load environment variables from .env file
    load_dotenv()
 
    # --- DEBUGGING: Print the keys to verify they are loaded ---
    api_key = os.getenv("API_KEY")
    print(f"DEBUG: API_KEY loaded: {api_key[:4]}..." if api_key else "DEBUG: API_KEY not found!")
    api_secret = os.getenv("API_SECRET")
    print(f"DEBUG: API_SECRET loaded: {api_secret[:4]}..." if api_secret else "DEBUG: API_SECRET not found!")
    access_token = os.getenv("ACCESS_TOKEN")
    print(f"DEBUG: ACCESS_TOKEN loaded: {access_token[:4]}..." if access_token else "DEBUG: ACCESS_TOKEN not found!")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    print(f"DEBUG: ACCESS_TOKEN_SECRET loaded: {access_token_secret[:4]}..." if access_token_secret else "DEBUG: ACCESS_TOKEN_SECRET not found!")
    # --------------------------------------------------------

    agent = SocialMediaAgent(
        api_key=os.getenv("API_KEY"),
        api_secret=os.getenv("API_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )
    
   
    print("🔐 Step 1: Authenticating with X API...")
    if not agent.authenticate():
        print("❌ Authentication failed. Please check your credentials.")
        return
    
    print("✅ Authentication successful!")
    

    print("\n📝 Step 2: Creating a single post...")
    post_content = "Hello from my AI Social Media Agent! 🤖 This post was created automatically. #AI #Automation and grateful about the power of AI"
    
    result = agent.create_post(post_content)
    
    if result.success:
        print(f"✅ Post created successfully!")
        print(f"   Post ID: {result.post_id}")
        print(f"   Post URL: {result.post_url}")
        print(f"   Timestamp: {result.timestamp}")
        
        # Step 3: Verify the post
        print(f"\n🔍 Step 3: Post verification completed during creation")
        
        # Step 4: Get post analytics (after a short delay)
        print(f"\n📊 Step 4: Getting post analytics...")
        time.sleep(5)
        analytics = agent.get_post_analytics(result.post_id)
        print(f"   Analytics: {analytics}")
        
    else:
        print(f"❌ Post creation failed: {result.error_message}")
    
    # Step 5: Demonstrate bulk posting
    print(f"\n📚 Step 5: Demonstrating bulk posting...")
    
    bulk_posts = [
        {"content": "First automated post in the series! 🚀 #Automation"},
        {"content": "Second post coming through! 📱 #AI"},
        {"content": "Third and final post in this demo! 🎯 #SocialMedia"}
    ]
    
    # Uncomment to test bulk posting (will create multiple posts)
    # bulk_results = agent.bulk_post(bulk_posts, delay_between_posts=1)
    # 
    # for i, result in enumerate(bulk_results):
    #     if result.success:
    #         print(f"✅ Bulk post {i+1} successful: {result.post_id}")
    #     else:
    #         print(f"❌ Bulk post {i+1} failed: {result.error_message}")


if __name__ == "__main__":
    main()