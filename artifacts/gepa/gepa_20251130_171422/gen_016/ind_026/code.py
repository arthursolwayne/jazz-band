
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5s - 3.0s)
# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0), # G#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25), # Db
    # Bar 3: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0), # Gb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif (F - G - Ab - Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.625, end=1.75), # G
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.0), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.125), # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.125, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.375), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=2.375, end=2.5), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.625), # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.75), # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=2.875, end=3.0), # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0s - 4.5s)
# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375), # G#
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5), # B
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75), # Db
    # Bar 4: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5), # F
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5), # Gb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif (F - G - Ab - Bb, then resolution)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125), # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.125, end=3.25), # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.625), # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.625, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=3.875), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=3.875, end=4.0), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.25), # G
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.375), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=4.375, end=4.5), # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5s - 6.0s)
# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=73, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=6.0), # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # Db
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0), # C
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0), # Db
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.625, end=4.75), # G
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.0), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.125), # F
    pretty_midi.Note(velocity=110, pitch=66, start=5.125, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.375), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=5.375, end=5.5), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=5.75), # G
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=5.875), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=5.875, end=6.0), # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(3):
    start = 4.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375), # Kick on 1
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5), # Kick on 3
        pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0), # Snare on 4
        # Hi-hat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 2.25, end=start + 2.625),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 2.625, end=start + 3.0),
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
