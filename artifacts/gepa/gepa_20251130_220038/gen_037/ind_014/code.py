
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Fm with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0), # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping on bar 2
piano_notes = [
    # Fm7 (F, Ab, C, Eb) on beat 2 (start=2.25)
    pretty_midi.Note(velocity=95, pitch=87, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=95, pitch=84, start=2.25, end=2.375), # Ab
    pretty_midi.Note(velocity=95, pitch=81, start=2.25, end=2.375), # C
    pretty_midi.Note(velocity=95, pitch=80, start=2.25, end=2.375), # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in Fm, short and melodic
sax_notes = [
    # Start of motif on beat 1 (start=1.5)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.5), # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping on bar 3
piano_notes = [
    # Fm7 on beat 2 (start=3.75)
    pretty_midi.Note(velocity=95, pitch=87, start=3.75, end=3.875), # F
    pretty_midi.Note(velocity=95, pitch=84, start=3.75, end=3.875), # Ab
    pretty_midi.Note(velocity=95, pitch=81, start=3.75, end=3.875), # C
    pretty_midi.Note(velocity=95, pitch=80, start=3.75, end=3.875), # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    # Continue the motif on beat 1 (start=3.0)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5), # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0), # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping on bar 4
piano_notes = [
    # Fm7 on beat 2 (start=5.25)
    pretty_midi.Note(velocity=95, pitch=87, start=5.25, end=5.375), # F
    pretty_midi.Note(velocity=95, pitch=84, start=5.25, end=5.375), # Ab
    pretty_midi.Note(velocity=95, pitch=81, start=5.25, end=5.375), # C
    pretty_midi.Note(velocity=95, pitch=80, start=5.25, end=5.375), # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif, resolve it
sax_notes = [
    # Finish the motif on beat 1 (start=4.5)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0), # C
]

for note in sax_notes:
    sax.notes.append(note)

# Drums in Bar 3 and 4 (3.0 - 6.0s)
# Same pattern as Bar 1
for i in range(3):
    for note in drum_notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + 3.0 * i,
            end=note.end + 3.0 * i
        )
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
