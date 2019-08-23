%% Spec examples:
%%
%%   {suites, "tests", amp_SUITE}.
%%   {groups, "tests", amp_SUITE, [discovery]}.
%%   {groups, "tests", amp_SUITE, [discovery], {cases, [stream_feature_test]}}.
%%   {cases, "tests", amp_SUITE, [stream_feature_test]}.
%%
%% For more info see:
%% http://www.erlang.org/doc/apps/common_test/run_test_chapter.html#test_specifications

%% do not remove below SUITE if testing mongoose
{suites, "tests", mongoose_sanity_checks_SUITE}.

{suites, "tests", rdbms_SUITE}.
{suites, "tests", race_conditions_SUITE}.
{suites, "tests", acc_e2e_SUITE}.
{suites, "tests", accounts_SUITE}.
{suites, "tests", adhoc_SUITE}.
{suites, "tests", amp_big_SUITE}.
{suites, "tests", anonymous_SUITE}.
{suites, "tests", bosh_SUITE}.
{suites, "tests", carboncopy_SUITE}.
{suites, "tests", connect_SUITE}.
{suites, "tests", component_SUITE}.
{suites, "tests", disco_and_caps_SUITE}.
{suites, "tests", gdpr_SUITE}.
{suites, "tests", inbox_SUITE}.
{suites, "tests", jingle_SUITE}.
{suites, "tests", last_SUITE}.
{suites, "tests", login_SUITE}.
{suites, "tests", mam_SUITE}.
{suites, "tests", mod_aws_sns_SUITE}.
{suites, "tests", mod_blocking_SUITE}.
{suites, "tests", mod_event_pusher_rabbit_SUITE}.
{suites, "tests", mod_http_notification_SUITE}.
{suites, "tests", mod_http_upload_SUITE}.
{suites, "tests", mod_ping_SUITE}.
{suites, "tests", mod_time_SUITE}.
{suites, "tests", mod_version_SUITE}.

%% Default config reader is:
%% {userconfig, {ct_config_plain, ["test.config"]}}.

%% But we use config with preprocessing:
%%{userconfig, {mim_ct_config, ["test.config"]}}.

{logdir, "ct_report"}.

%% ct_tty_hook will log CT failures to TTY verbosely
%% ct_mongoose_hook will:
%% * log suite start/end events in the MongooseIM console
%% * ensure preset value is passed to ct Config
%% * check server's purity after SUITE
{ct_hooks, [ct_groups_summary_hook, ct_tty_hook, ct_mongoose_hook, ct_progress_hook,
            ct_mim_config_hook,
            ct_markdown_errors_hook,
            {ct_mongoose_log_hook, [ejabberd_node, ejabberd_cookie]},
            {ct_mongoose_log_hook, [ejabberd2_node, ejabberd_cookie]}
           ]}.

%% To enable printing group and case enters on server side
%%{ct_hooks, [{ct_mongoose_hook, [print_group, print_case]}]}.