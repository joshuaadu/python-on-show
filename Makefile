.PHONY: start stop unit_tests

UNIT_TESTS=pytest test
start:
	@docker compose up -d

stop:
	@docker compose down

unit_tests:
	@docker compose exec -T app-test $(UNIT_TESTS)

unit_tests_local:
	@$(UNIT_TESTS)

check_typing:
	@docker compose exec -T app-test mypy .