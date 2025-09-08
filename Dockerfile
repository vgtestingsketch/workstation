# Используйте актуальную версию Odoo
FROM odoo:18.0

# Копируем кастомные модули в контейнер
USER root
COPY custom_addons /mnt/custom_addons
RUN chown -R odoo:odoo /mnt/custom_addons && \
    find /mnt/custom_addons -type d -exec chmod 755 {} \; && \
    find /mnt/custom_addons -type f -exec chmod 644 {} \;
USER odoo
