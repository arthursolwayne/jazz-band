
import pretty_midi

# Create a MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Create tension with rhythm and dynamics
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=KICK, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=KICK, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # C7 on beat 2 (1.875s), E7 on beat 4 (3.0s)
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # C7
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=80, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=84, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # E7
    pretty_midi.Note(velocity=90, pitch=80, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=84, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=88, start=3.0, end=3.375),
]

piano.notes.extend(piano_notes)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=47, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=70, pitch=45, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=70, pitch=46, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=70, pitch=48, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=70, pitch=47, start=3.375, end=3.75), # G#
    pretty_midi.Note(velocity=70, pitch=46, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=70, pitch=45, start=4.125, end=4.5),  # E
]

bass.notes.extend(bass_notes)

# Dante on sax: a short, angular motif — 4 notes over 1.5s
# F, G#, Bb, Ab — a question in the key of F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.6875, end=1.875), # G#
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=2.0625, end=2.25), # Ab
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # C7
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=80, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=84, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # E7
    pretty_midi.Note(velocity=90, pitch=80, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=88, start=4.5, end=4.875),
]

piano.notes.extend(piano_notes)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=48, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=70, pitch=47, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=70, pitch=46, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=70, pitch=45, start=4.125, end=4.5),   # E
    pretty_midi.Note(velocity=70, pitch=44, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=70, pitch=45, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=70, pitch=46, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=70, pitch=47, start=5.625, end=6.0),  # F#
]

bass.notes.extend(bass_notes)

# Dante on sax: continuation of the motif, now with a slight variation
# F, G#, Ab, Bb — a subtle inversion of the original
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.1875, end=3.375), # G#
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.5625), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=3.5625, end=3.75), # Bb
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C7
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=80, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=84, start=4.875, end=5.25),
]

piano.notes.extend(piano_notes)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=45, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=70, pitch=44, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=70, pitch=43, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=70, pitch=44, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=70, pitch=45, start=5.625, end=6.0),   # E
]

bass.notes.extend(bass_notes)

# Dante on sax: resolution of the motif — return to F, with a slight crescendo
# F, Bb, G#, F — a subtle resolution, not perfect, but full of tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.0625), # G#
    pretty_midi.Note(velocity=110, pitch=71, start=5.0625, end=5.25), # F (crescendo)
]

sax.notes.extend(sax_notes)

# Drums in bar 4: same pattern as bar 1
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=KICK, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=HIHAT, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=KICK, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Add all instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
