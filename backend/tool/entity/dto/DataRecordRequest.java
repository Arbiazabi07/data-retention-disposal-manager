package com.internship.tool.entity.dto;

import jakarta.validation.constraints.*;
import lombok.Data;

import java.time.LocalDate;

@Data
public class DataRecordRequest {

    @NotBlank(message = "Name is required")
    @Size(max = 200, message = "Name must be under 200 characters")
    private String name;

    @Size(max = 2000, message = "Description too long")
    private String description;

    @NotBlank(message = "Data type is required")
    private String dataType;

    private String owner;

    private String department;

    @NotNull(message = "Retention years is required")
    @Min(value = 1, message = "Retention must be at least 1 year")
    @Max(value = 100, message = "Retention cannot exceed 100 years")
    private Integer retentionYears;

    @NotNull(message = "Created date is required")
    private LocalDate createdDate;
}