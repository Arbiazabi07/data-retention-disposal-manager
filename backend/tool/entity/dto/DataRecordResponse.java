package com.internship.tool.entity.dto;

import lombok.Builder;
import lombok.Data;

import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@Builder
public class DataRecordResponse {

    private Long id;
    private String name;
    private String description;
    private String dataType;
    private String owner;
    private String department;
    private String status;
    private Integer retentionYears;
    private LocalDate createdDate;
    private LocalDate expiryDate;
    private String aiDescription;
    private Double aiScore;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}