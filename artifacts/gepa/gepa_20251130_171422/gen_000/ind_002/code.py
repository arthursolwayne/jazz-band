
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),  # A

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),  # D

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),  # D#
    pretty_midi.Note(velocity=90, pitch=56, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # E
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0), # C
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0), # E

    # Bar 3 (3.0 - 4.5s)
    # B7 on beat 2
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # G
    # B7 on beat 4
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.5), # B
    pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5), # E
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5), # G

    # Bar 4 (4.5 - 6.0s)
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0), # C
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0), # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - one short motif, make it sing
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # G

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # G

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75), # Snare on 4

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25), # Snare on 4

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75), # Snare on 4
]

# Add hi-hats for bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(4):
        start_time = start + i * 0.375
        end_time = start_time + 0.375
        pretty_midi.Note(velocity=90, pitch=42, start=start_time, end=end_time)

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
