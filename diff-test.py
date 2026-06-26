const handle = conn?.handle ?? '';
  const workspace = conn?.workspace ?? undefined;

  const reposToFetch: string[] = value.selectedRepo
    ? value.selectedRepo.split(',')
    : [];

  await context.sendActivity({
    attachments: [
      buildStatusCard(
        'Search',
        'Accent',
        reposToFetch.length === 0
          ? 'Fetching all pending PRs...'
          : 'Fetching pending PRs for selected repos...',
      ),
    ],
  });
