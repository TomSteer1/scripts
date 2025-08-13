FROM amazon/aws-cli

COPY bashrc /root/.bashrc
COPY start.sh /
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]
