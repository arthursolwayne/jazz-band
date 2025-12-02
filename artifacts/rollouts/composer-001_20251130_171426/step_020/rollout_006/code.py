
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
    # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    # Snare on beat 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    # Kick on beat 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in Dm, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # E
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # D
    # Bar 2, beat 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # D
    # Bar 3, beat 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # D
    # Bar 3, beat 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5), # D
    # Bar 4, beat 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # D
    # Bar 4, beat 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0), # D
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2, beat 1 (1.5 - 1.875)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # D
    # Bar 2, beat 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # F
    # Bar 2, beat 3 (2.25 - 2.625)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # G
    # Bar 2, beat 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0), # A
    # Bar 3, beat 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # F
    # Bar 3, beat 3 (3.75 - 4.125)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125), # G
    # Bar 3, beat 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5), # A
    # Bar 4, beat 1 (4.5 - 4.875)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875), # D
    # Bar 4, beat 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # F
    # Bar 4, beat 3 (5.25 - 5.625)
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # G
    # Bar 4, beat 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0), # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
