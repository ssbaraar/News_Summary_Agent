from agents.enhanced_data_acquisition_agent import EnhancedDataAcquisitionAgent
from agents.enhanced_content_analysis_agent import EnhancedContentAnalysisAgent
from agents.enhanced_reporting_agent import EnhancedReportingAgent
import time
from loguru import logger

def main():
    daa = EnhancedDataAcquisitionAgent()
    caa = EnhancedContentAnalysisAgent()
    ra = EnhancedReportingAgent()

    while True:
        try:
            daa.run()
            caa.run()
            ra.run()
            logger.info("Waiting for 15 minutes before next run...")
            time.sleep(900)  # Wait for 15 minutes
        except KeyboardInterrupt:
            logger.info("Agents stopped by user.")
            break
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            logger.info("Retrying in 5 minutes...")
            time.sleep(300)  # Wait for 5 minutes before retrying

if __name__ == "__main__":
    main()