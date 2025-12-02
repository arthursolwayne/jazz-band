
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
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
# Sax: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.1875),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, measure 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),   # Eb
    pretty_midi.Note(velocity=75, pitch=72, start=1.875, end=2.0),   # F
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75), # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.1875),  # C
    pretty_midi.Note(velocity=80, pitch=54, start=3.1875, end=3.375), # D
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.5625), # Eb
    pretty_midi.Note(velocity=80, pitch=57, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=3.9375),  # G
    pretty_midi.Note(velocity=80, pitch=60, start=3.9375, end=4.125), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=4.3125, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, measure 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.0),   # F
    pretty_midi.Note(velocity=85, pitch=69, start=3.875, end=4.0),   # C
    pretty_midi.Note(velocity=80, pitch=71, start=3.875, end=4.0),   # Eb
    pretty_midi.Note(velocity=75, pitch=72, start=3.875, end=4.0),   # F
]
piano.notes.extend(piano_notes)

# Drums: same pattern as Bar 1
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5, note.end + 1.5)
    drums.notes.append(new_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.1875, end=5.375), # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5625), # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.1875),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=5.1875, end=5.375), # D
    pretty_midi.Note(velocity=80, pitch=72, start=5.375, end=5.5625), # Eb
    pretty_midi.Note(velocity=80, pitch=74, start=5.5625, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=5.75, end=6.0),     # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, measure 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=64, start=5.375, end=5.5625), # F
    pretty_midi.Note(velocity=85, pitch=69, start=5.375, end=5.5625), # C
    pretty_midi.Note(velocity=80, pitch=71, start=5.375, end=5.5625), # Eb
    pretty_midi.Note(velocity=75, pitch=72, start=5.375, end=5.5625), # F
]
piano.notes.extend(piano_notes)

# Drums: same pattern as Bar 1
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 3.0, note.end + 3.0)
    drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
