let fileUIActions = {
    showFAB: (fid) => (
        {
            type: 'SHOW_FAB',
            payload: fid
        }
    ),
    hideFAB: (fid) => (
        {
            type: 'HIDE_FAB',
            payload: fid
        }
    )
}

export default fileUIActions;
