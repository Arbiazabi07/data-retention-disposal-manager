package com.internship.tool;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
@Disabled("Requires PostgreSQL, Redis, and mail server — skipped in unit test phase")
class ToolApplicationTests {

	@Test
	void contextLoads() {
	}

}
