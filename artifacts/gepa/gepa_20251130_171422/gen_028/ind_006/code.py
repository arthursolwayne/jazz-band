
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0), # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=85, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25), # G
    # Bar 2, beat 4 (F7)
    pretty_midi.Note(velocity=85, pitch=64, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0), # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - sparse, expressive, starts in bar 2
# Motif: F (64) -> Ab (67) -> C (60) -> Eb (62) -> F (64)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25),
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5),
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5), # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=85, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75), # G
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=85, pitch=64, start=4.125, end=4.5), # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5), # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5), # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue melody, with space and tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.375),
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.625),
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75),
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0),
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.125),
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=60, start=4.25, end=4.375),
    pretty_midi.Note(velocity=110, pitch=62, start=4.375, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0), # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=85, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25), # G
    # Bar 4, beat 4 (F7)
    pretty_midi.Note(velocity=85, pitch=64, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0), # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0), # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Resolve the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75),
    pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.125),
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.25),
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5),
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.625),
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.75),
    pretty_midi.Note(velocity=110, pitch=60, start=5.75, end=5.875),
    pretty_midi.Note(velocity=110, pitch=62, start=5.875, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue pattern
for i in range(3):
    start = 3.0 + i * 1.5
    drum_notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.25),
        pretty_midi.Note(velocity=60, pitch=42, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=60, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=60, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=60, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=60, pitch=42, start=start + 1.5, end=start + 1.875),
        pretty_midi.Note(velocity=60, pitch=42, start=start + 1.875, end=start + 2.25),
        pretty_midi.Note(velocity=60, pitch=42, start=start + 2.25, end=start + 2.625),
        pretty_midi.Note(velocity=60, pitch=42, start=start + 2.625, end=start + 3.0),
    ])

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('wayne.mid')
