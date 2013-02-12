from buildbot.schedulers.basic import AnyBranchScheduler
from buildbot.schedulers.triggerable import Triggerable
from buildbot.changes.filter import ChangeFilter
from buildbot.process.factory import BuildFactory
from buildbot.steps.master import MasterShellCommand
from buildscripts import steps as buildsteps


project = __opts__['project']


c['schedulers'].append(AnyBranchScheduler(
	name=project,
	change_filter=ChangeFilter(project=project, category='default'),
	builderNames=['{0} source'.format(project)]
))


c["schedulers"].append(Triggerable(
	name="{0} packaging".format(project),
	builderNames=["deb_packaging", "rpm_packaging"]
))


c['builders'].append(dict(
	name='{0} source'.format(project),
	slavenames=['ubuntu1004'],
	factory=BuildFactory(steps=
		buildsteps.svn(__opts__) +
		buildsteps.bump_version(__opts__, setter='cat > cloudstack/version') +
		buildsteps.source_dist(__opts__) +
		buildsteps.trigger_packaging(__opts__) + 
		buildsteps.to_repo(__opts__, types=["deb", "rpm"])
	)
))
