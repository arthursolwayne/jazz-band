
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5),
]

# Add drum notes
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - motif: F Ab Bb G (staccato)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=1.975),  # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=2.125, end=2.225),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5),    # G
]

# Bass - walking line (F, G, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0),   # A
]

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.875 - 2.0)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.0),
]

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - motif variation: F Bb Ab G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.475),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.725),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),    # G
]

# Bass - walking line (Bb, B, C, C#)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=3.125, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.5),   # C#
]

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (3.875 - 4.0)
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.0),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=66, start=3.875, end=4.0),
]

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - motif variation: F Ab Bb G (same as bar 2, but with a rest before the G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=4.975),  # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=5.125, end=5.225),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.5),    # G
]

# Bass - walking line (F, G, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.0),   # A
]

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (5.375 - 5.5)
    pretty_midi.Note(velocity=90, pitch=64, start=5.375, end=5.5),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=67, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=66, start=5.375, end=5.5),
]

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
