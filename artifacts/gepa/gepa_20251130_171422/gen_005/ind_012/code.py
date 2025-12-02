
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)

# Saxophone: Tenor motif
# Fm7 (F Ab Bb C) -> F Ab Bb C
# Start with F, Ab, Bb, then leave it hanging on C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
# F Ab G Bb Eb Ab G F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Left hand: root and fifth
# Right hand: 7th chord
# Fm7 (F Ab Bb C)
piano_notes = [
    # Left hand: F and Bb
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=2.0),  # Bb
    # Right hand: Fm7
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0),  # C
    # Left hand: F and Bb again on beat 4
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=2.75, end=3.0),  # Bb
    # Right hand: Fm7
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=70, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=2.75, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Saxophone continues motif (3.0 - 4.5s)
# Repeat the motif but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F (descending)
]
sax.notes.extend(sax_notes)

# Bass: Walking line continues
# F Ab G Bb Eb Ab G F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=63, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Left hand: F and Bb
# Right hand: Fm7
piano_notes = [
    # Left hand: F and Bb
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=3.25, end=3.5),  # Bb
    # Right hand: Fm7
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=70, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5),  # C
    # Left hand: F and Bb again on beat 4
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=4.25, end=4.5),  # Bb
    # Right hand: Fm7
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=70, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.25, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Saxophone finishes motif (4.5 - 6.0s)
# Return to the start of the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # F (return)
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # Ab
]
sax.notes.extend(sax_notes)

# Bass: Walking line continues
# F Ab G Bb Eb Ab G F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=63, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=63, start=6.0, end=6.25),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=6.25, end=6.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Left hand: F and Bb
# Right hand: Fm7
piano_notes = [
    # Left hand: F and Bb
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=4.75, end=5.0),  # Bb
    # Right hand: Fm7
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=70, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.75, end=5.0),  # C
    # Left hand: F and Bb again on beat 4
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=5.75, end=6.0),  # Bb
    # Right hand: Fm7
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=70, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=5.75, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Drums: Continue pattern (3.0 - 6.0s)
# Repeat the same pattern for the next two bars
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("dante_intro.mid")
