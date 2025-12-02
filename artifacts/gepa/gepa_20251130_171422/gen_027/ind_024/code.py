
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif on beat 1, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0),  # G#
    pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=80, pitch=45, start=2.125, end=2.25),  # A#
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=80, pitch=48, start=2.375, end=2.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2 (C7)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # C
    # Bar 2, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # F
]
sax.notes.extend(sax_notes)

# Bass: continue walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=3.125, end=3.25),  # D#
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.5),  # F#
    pretty_midi.Note(velocity=80, pitch=54, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=80, pitch=55, start=3.625, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=56, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=80, pitch=58, start=3.875, end=4.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: comp again on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=78, start=3.25, end=3.5),  # F
    # Bar 3, beat 4 (C7)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.625),  # E
    pretty_midi.Note(velocity=80, pitch=60, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=4.875),  # F#
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.125),  # G#
    pretty_midi.Note(velocity=80, pitch=65, start=5.125, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.375),  # A#
    pretty_midi.Note(velocity=80, pitch=68, start=5.375, end=5.5),  # B
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.75, end=5.0),  # E
    # Bar 4, beat 4 (C7)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # C
]
piano.notes.extend(piano_notes)

# Drums: continue with kick, snare, hihat
for i in range(2):
    for note in drum_notes:
        note.start += 1.5 * (i + 1)
        note.end += 1.5 * (i + 1)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
