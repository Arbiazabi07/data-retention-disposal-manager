package com.internship.tool.service;

import com.internship.tool.entity.DataRecord;
import jakarta.mail.MessagingException;
import jakarta.mail.internet.MimeMessage;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.Context;

import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class EmailService {

    private final JavaMailSender mailSender;
    private final TemplateEngine templateEngine;

    @Value("${spring.mail.username}")
    private String fromEmail;

    @Async
    public void sendExpiryReminder(String toEmail, List<DataRecord> expiringRecords) {
        try {
            Context context = new Context();
            context.setVariable("records", expiringRecords);

            String htmlContent = templateEngine.process("expiry-reminder", context);

            MimeMessage message = mailSender.createMimeMessage();
            MimeMessageHelper helper = new MimeMessageHelper(message, true, "UTF-8");
            helper.setFrom(fromEmail);
            helper.setTo(toEmail);
            helper.setSubject("Action Required: " + expiringRecords.size()
                    + " data records expiring soon");
            helper.setText(htmlContent, true);

            mailSender.send(message);
            log.info("Expiry reminder sent to: {}", toEmail);

        } catch (MessagingException e) {
            log.error("Failed to send expiry reminder to {}: {}", toEmail, e.getMessage());
        }
    }
}
