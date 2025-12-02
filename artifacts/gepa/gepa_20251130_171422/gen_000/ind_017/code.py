
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # G#

    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=56, start=4.125, end=4.5),  # C

    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),  # E

    # Bar 3 - Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # Ab

    # Bar 4 - E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=89, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=91, start=4.5, end=4.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone - short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.5, end=start_time + 1.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.5, end=start_time + 3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.875, end=start_time + 3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 2.25, end=start_time + 3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 2.625, end=start_time + 3.0),
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 2.625, end=start_time + 3.0),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 3.0, end=start_time + 3.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 3.0, end=start_time + 4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 3.375, end=start_time + 4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 3.75, end=start_time + 4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 4.125, end=start_time + 4.5),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 4.125, end=start_time + 4.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 4.5, end=start_time + 4.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 4.5, end=start_time + 6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 4.875, end=start_time + 6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 5.25, end=start_time + 6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 5.625, end=start_time + 6.0)

add_drums(1.5)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
