export default defineI18nConfig(() => ({
  legacy: false,
  locale: 'en',
  locales: ['en', 'fr'],
  messages: {
    en: {
      todos: {
        edit: 'Edit todo',
        new: 'New todo',
        model: {
          title: 'Title',
          description: 'Description',
          priority: {
            label: 'Priority',
            values: {
              low: 'Low',
              medium: 'Medium',
              high: 'High',
            },
          },
        },
      },
      actions: {
        save: 'Save',
        cancel: 'Cancel',
        delete: 'Delete',
      },
    },
    fr: {
      todos: {
        edit: 'Editer todo',
        new: 'Nouveau todo',
        model: {
          title: 'Titre',
          description: 'Description',
          priority: {
            label: 'Priorité',
            values: {
              low: 'Faible',
              medium: 'Moyenne',
              high: 'Élevée',
            },
          },
        },
      },
      actions: {
        save: 'Sauvegarder',
        cancel: 'Annuler',
        delete: 'Supprimer',
      },
    },

  },
}))
