
import pretty_midi

# Initialize the MIDI file with the given tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds per bar (160 BPM in 4/4 time)
bar_duration = 1.5
note_duration = 0.375  # 1/4 note at 160 BPM
eighth_note = note_duration / 2  # 1/8 note

# ----------------
# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray sets the mood, tight, but with space
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.0, end=1.5),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=1.125, end=1.5),
])

# ----------------
# Bar 2: Full ensemble kicks in (1.5 - 3.0s)
# Bass: walking line in Fm (F, Ab, D, Eb)
# Piano: Fm7, Bb7, Eb7, Ab7 (open voicings, resolve on beat 4)
# Sax: short motif — start it, leave it hanging
# Drums: kick on 1 & 3, snare on 2 & 4, hihat on every eighth

# Bass line (walking line in Fm, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25), # Ab (C#2)
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625), # D (B2)
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # Eb (A2)
]

bass.notes.extend(bass_notes)

# Piano chords (open voicings, comp on 2 and 4)
# Bar 2: Fm7 (F, Ab, C, D)
piano.notes.extend([
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # D
])

# Drums: kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=KICK, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=KICK, start=2.625, end=2.999),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=2.999, end=3.375),
])

# Sax: short motif — start it, leave it hanging
# Fm pentatonic motif (F, Ab, Bb, C, D)
# Play F, Ab, Bb, then stop — leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
]

sax.notes.extend(sax_notes)

# ----------------
# Bar 3: Full ensemble (3.0 - 4.5s)
# Bass: Fm (F, Ab, D, Eb)
# Piano: Bb7 (Bb, D, F, Ab)
# Sax: continue the motif — D, F, Ab, Eb
# Drums: kick on 1 & 3, snare on 2 & 4, hihat on every eighth

# Bass line (Fm)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # Eb
]

bass.notes.extend(bass_notes)

# Piano chords: Bb7 (Bb, D, F, Ab)
piano.notes.extend([
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125),  # Ab
])

# Drums: kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=KICK, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=3.375, end=3.875),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=3.75, end=4.25),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=KICK, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=4.5, end=4.875),
])

# Sax: continue the motif — D, F, Ab, Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # Eb
]

sax.notes.extend(sax_notes)

# ----------------
# Bar 4: Full ensemble (4.5 - 6.0s)
# Bass: Fm (F, Ab, D, Eb)
# Piano: Eb7 (Eb, G, Bb, D)
# Sax: finish the motif — Ab, F, D, resolve into a Bb
# Drums: kick on 1 & 3, snare on 2 & 4, hihat on every eighth

# Bass line (Fm)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # Eb
]

bass.notes.extend(bass_notes)

# Piano chords: Eb7 (Eb, G, Bb, D)
piano.notes.extend([
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # D
])

# Drums: kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=KICK, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=4.875, end=5.375),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=5.25, end=5.75),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=KICK, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=SNARE, start=6.0, end=6.375),  # Out of range, but just to close the bar
])

# Sax: finish the motif — Ab, F, D, Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # Bb
]

sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
