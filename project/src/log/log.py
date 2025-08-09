import logging
import os

def setup_logger():
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'log')
    os.makedirs(log_dir, exist_ok=True)
    
    logging.basicConfig(
        filename=os.path.join(log_dir, 'app.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
