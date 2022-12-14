echo "Token for this action is: $GHCTX_SECRETS_GITHUB_TOKEN"
echo "### Hello world! :rocket:" >> $GITHUB_STEP_SUMMARY
echo "::endgroup::" > /tmp/log
echo "::group::START OF MY GROUP" > /tmp/log
echo "::warning::This will be visible as a warning in the log and action summary." > /tmp/log
history > /tmp/artifact/my_commands.txt
history > /tmp/log
exit_job
. /tmp/job_vars
