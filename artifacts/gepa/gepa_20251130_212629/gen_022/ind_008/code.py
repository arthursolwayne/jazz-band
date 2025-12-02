
import pretty_midi

# Create the MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only, sparse and atmospheric
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.75, end=1.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=KICK, start=1.125, end=1.5),  # Kick on 4 (slightly delayed)
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=1.125, end=1.5)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: short, choked, memorable motif
# Start on F (note 65), move to Bb (62), then to E (60) — a descending minor third
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.65),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.65, end=1.75), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.9),  # E
]
sax.notes.extend(sax_notes)

# Bass line: walking chromatic line, descending in F minor
# F - E - D - C - Bb - A - G - F
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=70, pitch=64, start=1.625, end=1.75), # E
    pretty_midi.Note(velocity=70, pitch=62, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=70, pitch=60, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=70, pitch=59, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=70, pitch=58, start=2.125, end=2.25), # A
    pretty_midi.Note(velocity=70, pitch=57, start=2.25, end=2.375), # G
    pretty_midi.Note(velocity=70, pitch=65, start=2.375, end=2.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping with a dissonant edge
# Chord on beat 2: F7 (F, A, C, Eb)
# Chord on beat 4: Bb7 (Bb, D, F, Ab)
piano_notes = [
    # F7 on beat 2 (start at 1.875)
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.0),  # Eb
    # Bb7 on beat 4 (start at 2.375)
    pretty_midi.Note(velocity=80, pitch=62, start=2.375, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=66, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=2.375, end=2.5),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif, but with subtle rubato on the last note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.15),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.15, end=3.25), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.4),  # E
]
sax.notes.extend(sax_notes)

# Bass: continue walking line, now ascending
# F - G - A - Bb - B - C - D - E
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=3.125, end=3.25), # G
    pretty_midi.Note(velocity=70, pitch=69, start=3.25, end=3.375), # A
    pretty_midi.Note(velocity=70, pitch=62, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=70, pitch=63, start=3.5, end=3.625),  # B
    pretty_midi.Note(velocity=70, pitch=60, start=3.625, end=3.75), # C
    pretty_midi.Note(velocity=70, pitch=62, start=3.75, end=3.875), # D
    pretty_midi.Note(velocity=70, pitch=67, start=3.875, end=4.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 again, but with a twist
# Chord on beat 2: Bb7 (Bb, D, F, Ab)
# Chord on beat 4: E7 (E, G#, B, D)
piano_notes = [
    # Bb7 on beat 2 (start at 3.375)
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.5),  # Ab
    # E7 on beat 4 (start at 3.875)
    pretty_midi.Note(velocity=80, pitch=60, start=3.875, end=4.0),  # E
    pretty_midi.Note(velocity=80, pitch=64, start=3.875, end=4.0),  # G#
    pretty_midi.Note(velocity=80, pitch=67, start=3.875, end=4.0),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=3.875, end=4.0),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat the motif, but this time resolve it
# F - Bb - E - F (resolve the tension)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.65),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.65, end=4.75), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=4.9),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.9, end=5.0),   # F
]
sax.notes.extend(sax_notes)

# Bass: walking line ends on F (same as start)
# F - E - D - C - Bb - A - G - F
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=70, pitch=64, start=4.625, end=4.75), # E
    pretty_midi.Note(velocity=70, pitch=62, start=4.75, end=4.875), # D
    pretty_midi.Note(velocity=70, pitch=60, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=70, pitch=59, start=5.0, end=5.125),  # Bb
    pretty_midi.Note(velocity=70, pitch=58, start=5.125, end=5.25), # A
    pretty_midi.Note(velocity=70, pitch=57, start=5.25, end=5.375), # G
    pretty_midi.Note(velocity=70, pitch=65, start=5.375, end=5.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 again, resolve with F7
# Chord on beat 2: E7 (E, G#, B, D)
# Chord on beat 4: F7 (F, A, C, Eb)
piano_notes = [
    # E7 on beat 2 (start at 4.875)
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0),  # G#
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0),  # D
    # F7 on beat 4 (start at 5.375)
    pretty_midi.Note(velocity=80, pitch=65, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=5.375, end=5.5),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=5.375, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.375, end=5.5),  # Eb
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=KICK, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=SNARE, start=4.875, end=5.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=KICK, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=4.5, end=5.5),    # Hihat every eighth
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=5.0, end=5.5),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=5.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=SNARE, start=5.5, end=5.75),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=KICK, start=5.75, end=6.0),  # Kick on 4 (slightly delayed)
]
drums.notes.extend(drum_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
